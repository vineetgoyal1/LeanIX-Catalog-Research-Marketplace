# Marketing Language Filter - V2 Workflow Update

## Problem

Descriptions extracted from provider websites often contain marketing buzzwords like:
- "seamless integration"
- "transforms business operations"
- "enhance productivity"
- "streamline workflows"
- "enterprise-grade security"

These phrases are not factual and should be removed or rewritten.

## Solution

Added 3-layer marketing language detection and removal:

### Layer 1: Perplexity Query Instructions

**File**: `lib/parallel_researcher.py`

Updated `_get_description_query()` to explicitly instruct Perplexity to avoid marketing language:

```
NO marketing language: avoid "seamless", "enhance", "transform", "streamline", "empower", "revolutionary", "cutting-edge", "enterprise-grade", "best-in-class", "leading", "innovative", "powerful"

Use neutral verbs: "provides", "offers", "includes", "supports", "allows"

Example of marketing vs factual:
❌ "transforms business operations through seamless integration"
✅ "integrates with business tools to automate tasks"
```

### Layer 2: Fact Checker Detection

**File**: `lib/fact_checker.py`

Added marketing buzzword detection:

1. **MARKETING_BUZZWORDS list** - 30+ common marketing terms
2. **detect_marketing_language()** method - Scans text for buzzwords using regex word boundaries
3. **Updated description verification query** - Flags detected buzzwords and provides rewriting examples

```python
MARKETING_BUZZWORDS = [
    "seamless", "seamlessly",
    "transform", "transforms", "transforming",
    "enhance", "enhances", "enhancing",
    "streamline", "streamlines", "streamlining",
    "empower", "empowers", "empowering",
    "revolutionary", "cutting-edge",
    "enterprise-grade", "best-in-class",
    "leading", "innovative", "powerful",
    # ... and more
]
```

When marketing language is detected, the fact-checker generates a verification query that:
- Lists the specific buzzwords found
- Provides rewriting examples for each
- Asks Perplexity to rewrite the description factually

### Layer 3: Verification Agent Review

**File**: `WORKFLOW_V2.md`

Updated Step 2.5 (Description verification) to include marketing language check:

```
Agent action:
  1. Compare which is more accurate to official website
  2. Check for marketing buzzwords
  3. Remove marketing language if present
```

## Rewriting Rules

| Marketing Language | Factual Replacement |
|-------------------|---------------------|
| "seamless integration" | "integrates with" |
| "transforms operations" | "automates operations" or "changes how operations work" |
| "enhance productivity" | "increases output" or "reduces time for tasks" |
| "streamline workflows" | "simplifies workflows" or "automates workflows" |
| "enterprise-grade" | (remove this qualifier) |
| "cutting-edge" | "recent" or "current" |
| "powerful" | Describe what it actually does |
| "leading" | (remove this qualifier) |
| "innovative" | (remove or describe the specific innovation) |
| "revolutionary" | (remove or describe what changed) |

## Example Transformation

### Before (Marketing):
```
TeamSmart AI is an intelligent AI agent platform that transforms business operations
through autonomous task execution and continuous learning. The platform features
autonomous decision-making, seamless integration with existing tools, real-time
analytics, and enterprise-grade security. It targets modern teams and businesses
seeking to streamline workflows and enhance productivity through AI-powered automation.
```

**Marketing buzzwords detected**: transforms, seamless, enterprise-grade, streamline, enhance

### After (Factual):
```
TeamSmart AI is a platform that provides access to multiple AI models including
ChatGPT, Claude, Gemini, and Perplexity Search. It offers pre-built AI assistants
for professional services such as legal, accounting, and psychology tasks. The
platform integrates with business tools to automate workflows and includes analytics
and security features. It targets teams and businesses using AI for task automation.
```

**Marketing buzzwords detected**: None

**Key differences**:
- ❌ "transforms business operations" → ✅ "automate workflows"
- ❌ "seamless integration" → ✅ "integrates with business tools"
- ❌ "enterprise-grade security" → ✅ "includes security features"
- ❌ "streamline workflows" → ✅ "automate workflows"
- ❌ "enhance productivity" → ✅ "using AI for task automation"

## Testing

To verify the filter is working:

1. Create a provider with known marketing language on their website
2. Check if Perplexity's initial extraction avoids buzzwords (Layer 1)
3. If buzzwords slip through, fact checker should detect them (Layer 2)
4. Verification agent should flag and rewrite (Layer 3)

Expected result: Final description should be purely factual with zero marketing language.

## Customization

To add more buzzwords to detect, edit `lib/fact_checker.py`:

```python
MARKETING_BUZZWORDS = [
    # ... existing buzzwords ...
    "your-new-buzzword",
    "another-buzzword",
]
```

The detection is case-insensitive and uses word boundaries to avoid partial matches.
