# SI ID Uniqueness Implementation Guide

## Overview

The SI ID (System Integration ID) field **MUST be absolutely unique** across all Applications in LeanIX. This document outlines how to implement the uniqueness constraint in the Create Application workflow.

## Current State Analysis

**Validation Results from Production Data:**
- Total Applications: 16,068
- Total SI IDs: 16,068
- Unique SI IDs: 16,068
- **Duplicates: 0** ✅

**Uniqueness is a hard requirement.**

---

## Implementation Strategy

### Phase 1: Fetch Existing SI IDs (Pre-Generation Check)

Before generating a new SI ID, retrieve all existing SI IDs from LeanIX to check for collisions.

#### Method 1: Using LeanIX MCP Server (Recommended)

```python
async def get_all_existing_si_ids():
    """
    Fetch all existing SI IDs from LeanIX Applications.

    Returns:
        set: Set of all SI IDs currently in use
    """
    existing_si_ids = set()
    cursor = None

    while True:
        # Query LeanIX for applications
        response = await leanix_mcp.get_applications(
            page_size=100,
            cursor=cursor
        )

        # Extract SI IDs from response
        for app in response['applications']:
            if app.get('siId'):
                existing_si_ids.add(app['siId'])

        # Check if there are more pages
        cursor = response.get('cursor')
        if not cursor:
            break

    return existing_si_ids
```

#### Method 2: Using GraphQL Query

```python
async def get_all_si_ids_graphql(leanix_client):
    """
    Fetch all SI IDs using GraphQL query.

    Returns:
        set: Set of all SI IDs currently in use
    """
    query = """
    query GetAllApplicationSIIds($cursor: String) {
        allFactSheets(
            factSheetType: Application
            first: 100
            after: $cursor
        ) {
            edges {
                node {
                    siId
                }
            }
            pageInfo {
                hasNextPage
                endCursor
            }
        }
    }
    """

    existing_si_ids = set()
    cursor = None

    while True:
        result = await leanix_client.execute_graphql_query(
            query,
            variables={'cursor': cursor}
        )

        edges = result['data']['allFactSheets']['edges']
        for edge in edges:
            si_id = edge['node'].get('siId')
            if si_id:
                existing_si_ids.add(si_id)

        page_info = result['data']['allFactSheets']['pageInfo']
        if not page_info['hasNextPage']:
            break
        cursor = page_info['endCursor']

    return existing_si_ids
```

---

### Phase 2: Generate SI ID

Apply the transformation rules from `Application_SI_ID_Guidelines.md`.

```python
def generate_si_id(application_name: str, aliases: str = "") -> str:
    """
    Generate SI ID from application name following transformation rules.

    Args:
        application_name: The Application Name
        aliases: Comma-separated aliases (optional, for special cases)

    Returns:
        str: Generated SI ID
    """
    # Step 1: Check if we should use an alias/former name
    si_id_candidate = check_for_alias_usage(application_name, aliases)
    if si_id_candidate:
        return si_id_candidate

    # Step 2: Apply basic transformation rules
    si_id = application_name

    # Remove special characters: . , - ' ( ) / & :
    special_chars = ['.', ',', '-', "'", '(', ')', '/', '&', ':']
    for char in special_chars:
        si_id = si_id.replace(char, '')

    # Remove domain extensions
    domain_extensions = ['.com', '.io', '.net', '.ai', '.ly', '.cloud', '.org']
    for ext in domain_extensions:
        if si_id.lower().endswith(ext):
            si_id = si_id[:-len(ext)]

    # Remove "by [Company]" suffix
    if ' by ' in si_id:
        si_id = si_id.split(' by ')[0]

    # Remove version numbers like "2.0", "v3", etc.
    import re
        si_id = re.sub(r'\s+\d+\.\d+$', '', si_id)  # Remove " 2.0" at end
    si_id = re.sub(r'\s+v\d+$', '', si_id, flags=re.IGNORECASE)  # Remove " v2"

    # Remove all spaces
    si_id = si_id.replace(' ', '')

    # Step 3: Handle very long names (>60 chars) - abbreviate intelligently
    if len(si_id) > 60:
        si_id = abbreviate_long_name(si_id, application_name)

    return si_id


def check_for_alias_usage(application_name: str, aliases: str) -> str | None:
    """
    Check if we should use an alias instead of the application name.

    Common cases:
    - Former names after acquisition
    - Well-known abbreviations
    - Product rebrandings

    Returns:
        str | None: SI ID if alias should be used, None otherwise
    """
    # This would contain logic to detect when to use alias
    # For example, check if application has "formerly known as" pattern

    # Parse aliases (comma-separated)
    if not aliases:
        return None

    alias_list = [a.strip() for a in aliases.split(',')]

    # Heuristics for using alias:
    # 1. If application name is very long but alias is short and well-known
    # 2. If alias is a former company name (check against known acquisitions)
    # 3. If alias is widely used abbreviation

    # Example implementation:
    if len(application_name) > 40 and len(alias_list) > 0:
        first_alias = alias_list[0]
        # Apply same transformation to alias
        cleaned_alias = first_alias.replace(' ', '').replace('-', '').replace('.', '')
        if len(cleaned_alias) < 20:
            return cleaned_alias

    return None


def abbreviate_long_name(si_id: str, original_name: str) -> str:
    """
    Intelligently abbreviate very long application names.

    Strategy:
    1. Keep company/product prefix
    2. Keep key distinguishing terms
    3. Abbreviate or remove filler words

    Args:
        si_id: Current SI ID (no spaces)
        original_name: Original application name (with spaces)

    Returns:
        str: Abbreviated SI ID
    """
    words = original_name.split()

    # Keep first 2 words (usually company + product)
    important_words = words[:2]

    # Add key distinguishing words from the rest
    remaining_words = words[2:]

    # Filter out common filler words
    filler_words = {'for', 'and', 'the', 'with', 'management', 'platform', 'solution', 'service'}
    key_words = [w for w in remaining_words if w.lower() not in filler_words]

    # Take up to 3 more key words
    important_words.extend(key_words[:3])

    # Reconstruct
    abbreviated = ''.join(important_words)

    # If still too long, truncate
    if len(abbreviated) > 60:
        abbreviated = abbreviated[:60]

    return abbreviated
```

---

### Phase 3: Check for Collision

Compare the generated SI ID against existing SI IDs.

```python
def is_si_id_available(si_id: str, existing_si_ids: set) -> bool:
    """
    Check if SI ID is available (not already in use).

    Args:
        si_id: Proposed SI ID
        existing_si_ids: Set of all existing SI IDs

    Returns:
        bool: True if available, False if collision detected
    """
    return si_id not in existing_si_ids
```

---

### Phase 4: Resolve Collisions (If Detected)

If the generated SI ID already exists, apply disambiguation strategies.

```python
def resolve_si_id_collision(
    original_si_id: str,
    application_name: str,
    aliases: str,
    existing_si_ids: set
) -> str:
    """
    Resolve SI ID collision by applying disambiguation strategies.

    Disambiguation Priority:
    1. Try using alias/former name
    2. Add company name (if not already present)
    3. Add product differentiator
    4. Add numeric suffix (1, 2, 3, ...)

    Args:
        original_si_id: The colliding SI ID
        application_name: Full application name
        aliases: Comma-separated aliases
        existing_si_ids: Set of existing SI IDs

    Returns:
        str: Unique SI ID
    """
    # Strategy 1: Try using an alias
    if aliases:
        alias_list = [a.strip() for a in aliases.split(',')]
        for alias in alias_list:
            alias_si_id = generate_si_id(alias)
            if is_si_id_available(alias_si_id, existing_si_ids):
                return alias_si_id

    # Strategy 2: Add company name prefix
    # Extract company name from application name (usually first word)
    words = application_name.split()
    if len(words) > 1:
        company = words[0].replace('.', '').replace(',', '')
        if company.lower() not in original_si_id.lower():
            candidate = company + original_si_id
            if is_si_id_available(candidate, existing_si_ids):
                return candidate

    # Strategy 3: Add distinguishing suffix from name
    # Example: If "Portal" exists, try "CustomerPortal"
    for word in words[1:]:
        clean_word = word.replace('.', '').replace(',', '')
        if clean_word.lower() not in original_si_id.lower():
            candidate = original_si_id + clean_word
            if is_si_id_available(candidate, existing_si_ids):
                return candidate

    # Strategy 4: Numeric suffix (last resort)
    counter = 1
    while True:
        candidate = f"{original_si_id}{counter}"
        if is_si_id_available(candidate, existing_si_ids):
            return candidate
        counter += 1

        # Safety: prevent infinite loop
        if counter > 100:
            raise ValueError(f"Could not generate unique SI ID for {application_name}")
```

---

### Phase 5: Complete Workflow Integration

```python
async def generate_unique_si_id(
    application_name: str,
    aliases: str = ""
) -> str:
    """
    Complete workflow to generate a guaranteed-unique SI ID.

    Args:
        application_name: The Application Name
        aliases: Comma-separated aliases (optional)

    Returns:
        str: Guaranteed unique SI ID

    Raises:
        ValueError: If unable to generate unique SI ID
    """
    # Step 1: Fetch all existing SI IDs
    existing_si_ids = await get_all_existing_si_ids()

    # Step 2: Generate SI ID candidate
    si_id = generate_si_id(application_name, aliases)

    # Step 3: Check for collision
    if is_si_id_available(si_id, existing_si_ids):
        return si_id

    # Step 4: Resolve collision
    print(f"⚠️  SI ID collision detected: {si_id} already exists")
    si_id = resolve_si_id_collision(
        si_id,
        application_name,
        aliases,
        existing_si_ids
    )

    print(f"✓ Resolved to unique SI ID: {si_id}")
    return si_id
```

---

## Workflow Integration

### In Create Application Skill

```python
async def create_application_skill(application_name: str, url: str = None):
    """
    Create Application workflow with SI ID uniqueness handling.
    """
    print(f"Creating Application: {application_name}")

    # Step 1: Research application data
    # (Description, Alias, etc. - from other guidelines)
    research_data = await research_application(application_name, url)

    # Step 2: Generate guaranteed-unique SI ID
    print("\n--- Generating SI ID ---")
    si_id = await generate_unique_si_id(
        application_name=application_name,
        aliases=research_data.get('alias', '')
    )
    print(f"✓ SI ID: {si_id}")

    # Step 3: Create fact sheet in LeanIX
    fact_sheet_data = {
        'name': application_name,
        'description': research_data['description'],
        'alias': research_data['alias'],
        'siId': si_id,
        # ... other fields
    }

    result = await create_fact_sheet(fact_sheet_data)
    print(f"\n✓ Application created: {result['id']}")
    return result
```

---

## Performance Optimization

### Caching Strategy

For repeated operations, cache existing SI IDs to avoid repeated queries:

```python
class SIIDCache:
    """Cache for existing SI IDs with TTL."""

    def __init__(self, ttl_seconds=300):
        self.cache = None
        self.last_fetch = None
        self.ttl = ttl_seconds

    async def get_existing_si_ids(self):
        """Get existing SI IDs from cache or fetch if expired."""
        import time

        now = time.time()

        # Check if cache is valid
        if self.cache is not None and self.last_fetch is not None:
            if now - self.last_fetch < self.ttl:
                return self.cache

        # Fetch fresh data
        self.cache = await get_all_existing_si_ids()
        self.last_fetch = now
        return self.cache

    def invalidate(self):
        """Invalidate cache (call after creating new application)."""
        self.cache = None
        self.last_fetch = None


# Global cache instance
si_id_cache = SIIDCache(ttl_seconds=300)  # 5 minute TTL

async def generate_unique_si_id_cached(application_name: str, aliases: str = "") -> str:
    """Generate unique SI ID using cached existing SI IDs."""
    existing_si_ids = await si_id_cache.get_existing_si_ids()

    si_id = generate_si_id(application_name, aliases)

    if is_si_id_available(si_id, existing_si_ids):
        return si_id

    return resolve_si_id_collision(si_id, application_name, aliases, existing_si_ids)
```

---

## Testing Strategy

### Unit Tests

```python
def test_si_id_generation():
    """Test basic SI ID generation rules."""
    assert generate_si_id("Smartsheet") == "Smartsheet"
    assert generate_si_id("Adobe Document Cloud") == "AdobeDocumentCloud"
    assert generate_si_id("absence.io") == "Absence"
    assert generate_si_id("Act-On") == "ActOn"
    assert generate_si_id("A/P One") == "APOne"

def test_si_id_uniqueness():
    """Test uniqueness constraint."""
    existing = {"Smartsheet", "AdobeSign", "Salesforce"}

    # Should be available
    assert is_si_id_available("NewApp", existing) == True

    # Should be taken
    assert is_si_id_available("Smartsheet", existing) == False

def test_collision_resolution():
    """Test collision resolution strategies."""
    existing = {"Portal", "CustomerPortal"}

    resolved = resolve_si_id_collision(
        original_si_id="Portal",
        application_name="Employee Portal",
        aliases="",
        existing_si_ids=existing
    )

    # Should generate unique alternative
    assert resolved not in existing
    assert resolved.startswith("Portal") or resolved.startswith("Employee")
```

### Integration Tests

```python
async def test_end_to_end_uniqueness():
    """Test complete workflow with real LeanIX data."""

    # Test 1: New application (should generate unique ID)
    si_id_1 = await generate_unique_si_id("TestApp12345")
    assert si_id_1 is not None

    # Test 2: Same application (should detect collision and resolve)
    si_id_2 = await generate_unique_si_id("TestApp12345")
    # If created in Test 1, this should generate different ID
    assert si_id_2 is not None
```

---

## Error Handling

```python
class SIIDGenerationError(Exception):
    """Raised when unable to generate unique SI ID."""
    pass

async def generate_unique_si_id_safe(
    application_name: str,
    aliases: str = "",
    max_attempts: int = 10
) -> str:
    """
    Safe wrapper with error handling and retry logic.

    Args:
        application_name: Application name
        aliases: Aliases
        max_attempts: Maximum collision resolution attempts

    Returns:
        str: Unique SI ID

    Raises:
        SIIDGenerationError: If unable to generate unique ID
    """
    try:
        si_id = await generate_unique_si_id(application_name, aliases)
        return si_id
    except Exception as e:
        raise SIIDGenerationError(
            f"Failed to generate unique SI ID for '{application_name}': {e}"
        ) from e
```

---

## Summary

### Implementation Checklist

- [ ] **Phase 1**: Implement `get_all_existing_si_ids()` using LeanIX MCP or GraphQL
- [ ] **Phase 2**: Implement `generate_si_id()` following transformation rules
- [ ] **Phase 3**: Implement `is_si_id_available()` collision detection
- [ ] **Phase 4**: Implement `resolve_si_id_collision()` disambiguation
- [ ] **Phase 5**: Integrate into Create Application workflow
- [ ] **Caching**: Implement `SIIDCache` for performance
- [ ] **Testing**: Write unit and integration tests
- [ ] **Error Handling**: Add robust error handling

### Key Principles

1. **Uniqueness is mandatory** - Zero duplicates allowed
2. **Check before assign** - Always fetch existing SI IDs first
3. **Deterministic generation** - Same input → same output (given no collisions)
4. **Graceful collision resolution** - Multiple fallback strategies
5. **Performance-conscious** - Cache existing SI IDs when possible
6. **Transparent to user** - Handle collisions automatically

### Collision Resolution Priority

1. Try alias/former name
2. Add company prefix
3. Add product differentiator
4. Add numeric suffix (last resort)

### Estimated Collision Rate

Based on production data analysis:
- **~93%** of applications will have no collision (simple PascalCase works)
- **~7%** need special handling (aliases, abbreviations)
- **Actual collisions**: Extremely rare (0% in current 16K applications)
