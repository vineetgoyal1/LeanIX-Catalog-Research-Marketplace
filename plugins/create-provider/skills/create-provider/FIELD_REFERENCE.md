# Field Reference for LeanIX Fact Sheet Types

This document lists all available fields for each fact sheet type in your LeanIX workspace. These fields were discovered using the `discover` command.

**Last Updated**: 2026-02-17

---

## Provider (66 fields)

### Key Fields for Catalog Research
- `aliases` - Alternative provider names (comma-separated)
- `homePageUrl` - Provider's official website URL
- `headquartersAddress` - Physical headquarters address
- `providerCategory` - Provider category (enum - check LeanIX for valid values)
- `description` - Provider description
- `yearFounded` - Year the provider was founded

### Contact Information
- `phone` - Contact phone number
- `supportEMail` - Support email address
- `supportPageURL` - Support page URL
- `contactUsPageURL` - Contact page URL

### Additional URLs
- `announcementPageUrl` - Announcements/news page
- `rssFeedUrl` - RSS feed URL

### Location
- `city` - City location
- `country` - Country location
- `headQuarters` - Headquarters information

### Status & Metadata
- `providerStatus` - Provider status
- `providerExternalId` - External system ID
- `lxCatalogStatus` - LeanIX catalog status
- `lxState` - LeanIX state (e.g., DRAFT)
- `formerName` - Previous name(s)
- `deprecated` - Deprecation flag
- `deprecationReason` - Reason for deprecation

### Collection Information
- `collectionStatus` - Data collection status
- `collectionComment` - Collection comments
- `asOfDate` - As-of date for data

### Regional Link Counts
- `aeCountsOfLinks` - Asia/Middle East link counts
- `auCountsOfLinks` - Australia link counts
- `brCountsOfLinks` - Brazil link counts
- `caCountsOfLinks` - Canada link counts
- `chCountsOfLinks` - Switzerland link counts
- `deCountsOfLinks` - Germany link counts
- `euCountsOfLinks` - Europe link counts
- `hoCountsOfLinks` - Hong Kong link counts
- `jpCountsOfLinks` - Japan link counts
- `sgCountsOfLinks` - Singapore link counts
- `ukCountsOfLinks` - UK link counts
- `usCountsOfLinks` - US link counts
- `totalCountsOfLinksOnCustomer` - Total customer links

### Relations
- `relProviderToITComponent` - Relation to IT components
- `relProviderToProductFamily` - Relation to product families
- `relProviderToLTLSRequest` - Relation to LTLS requests
- `relToChild` - Child relationships
- `relToParent` - Parent relationships

### System Fields (Read-Only)
- `id` - Unique identifier
- `name` - Provider name
- `displayName` - Display name
- `fullName` - Full name
- `type` - Type (Provider)
- `status` - Status (ACTIVE/ARCHIVED)
- `level` - Hierarchy level
- `completion` - Completion percentage
- `createdAt` - Creation timestamp
- `updatedAt` - Last update timestamp
- `rev` - Revision number
- `permissions` - User permissions
- `permittedReadACL` - Read access control
- `permittedWriteACL` - Write access control
- `subscriptions` - User subscriptions
- `tags` - Tags
- `documents` - Attached documents
- `comments` - Comments
- `category` - Category
- `lxMilestones` - Milestones
- `lxExcludeFromQuota` - Exclude from quota flag
- `lxTransformationsFutureFactSheet` - Future transformations
- `naFields` - Not available fields

---

## Application (98 fields)

### Key Fields
- `alias` - Application alias
- `description` - Application description
- `webpageUrl` - Application webpage
- `provider` - Provider reference

### Alias Fields (Integration Systems)
- `MDCAAliasAppl` - MDCA alias
- `MSEntraAliasAppl` - Microsoft Entra alias
- `NetskopeAliasAppl` - Netskope alias
- `OktaAliasAppl` - Okta alias
- `SAPAliasAppl` - SAP alias
- `SBOMAliasAppl` - SBOM alias
- `ServiceNowAliasAppl` - ServiceNow alias
- `WalkMeAliasAppl` - WalkMe alias
- `ZscalerAliasAppl` - Zscaler alias

### URLs & Access
- `apiUrl` - API endpoint URL
- `loginUrl` - Login page URL
- `SSOURL` - Single sign-on URL
- `complianceUrl` - Compliance documentation URL
- `gdprUrl` - GDPR documentation URL
- `greenComplianceUrl` - Green compliance URL
- `privacyPolicyUrl` - Privacy policy URL
- `securityPageUrl` - Security information URL
- `statusPageUrl` - Status page URL
- `termsOfServiceUrl` - Terms of service URL
- `pricingUrl` - Pricing information URL

### Hosting Information
- `hostingType` - Hosting type (Cloud/On-Premise)
- `hostingDescription` - Hosting description
- `hostingURL` - Hosting URL

### Pricing & Categories
- `pricingType` - Pricing model
- `productCategory` - Product category
- `g2Categories` - G2 categories
- `nonSaasCategory` - Non-SaaS category
- `domain` - Application domain

### SSO & Integration
- `ssoProvider` - SSO provider
- `ssoStatus` - SSO status
- `statusSSO` - SSO status
- `integrationCapabilities` - Integration capabilities

### Classification & Security
- `classificationLevel` - Data classification level
- `discoverySource` - How the app was discovered

### Log4Shell Vulnerability Tracking
- `logFourShellAdditionalInformation` - Additional info
- `logFourShellRemediationStatus` - Remediation status
- `logFourShellResearchComments` - Research comments
- `logFourShellStatusAsOfDate` - Status date
- `logFourShellUrls` - Related URLs

### Collection & Status
- `collectionStatus` - Data collection status
- `collectionComment` - Collection comments
- `completionStatus` - Completion status
- `maintenanceFlag` - Maintenance flag
- `lxCatalogStatus` - Catalog status

### External IDs
- `applicationExternalId` - External system ID
- `providerExternalId` - Provider external ID
- `siId` - SI ID
- `targetSystem` - Target system

### Relations
- `relApplicationToITComponent` - Relation to IT components
- `relApplicationToProductFamily` - Relation to product families
- `relToPredecessorApplication` - Predecessor application
- `relToSuccessorApplication` - Successor application
- `relToChild` - Child relationships
- `relToParent` - Parent relationships

### Regional Link Counts
- Same as Provider (aeCountsOfLinks through totalCountsOfLinksOnCustomer)

### System Fields (Read-Only)
- Similar to Provider (id, name, displayName, status, etc.)

---

## ProductFamily (64 fields)

### Key Fields
- `baseName` - Base product name
- `description` - Product family description
- `productWebsite` - Official product website
- `productFamilyType` - Type of product family
- `aliases` - Alternative product names

### Lifecycle Management
- `lifecyclePolicyName` - Lifecycle policy name
- `lifecyclePolicyDesc` - Lifecycle policy description
- `lifecyclePolicyUrl` - Policy documentation URL
- `lifecycleUrl` - General lifecycle URL
- `loginRequiredForLifecycleData` - Login required flag

### Phase Dates
- `plan` - Plan phase date
- `phaseIn` - Phase in date
- `phaseOut` - Phase out date
- `endOfSale` - End of sale date
- `endOfLife` - End of life date
- `endOfExtendedSupportOffering` - Extended support end date
- `dateFormat` - Date format specification

### Version & Release Information
- `latestProductVersionInTheCatalog` - Latest version in catalog
- `productVersioningFormat` - Version numbering format
- `releaseCycle` - Release cycle information
- `generalMaintenance` - General maintenance info
- `availableEditionsList` - List of available editions

### Support
- `supportType` - Type of support offered

### Status & Assessment
- `active` - Active status flag
- `productRetirementStatus` - Retirement status
- `coverageStatus` - Coverage status
- `assessmentCategory` - Assessment category
- `maintenanceFlag` - Maintenance flag

### Collection & Research
- `collectionStatus` - Data collection status
- `potentialSourcesOfData` - Data sources
- `assumptionsAndExceptions` - Assumptions and exceptions

### External IDs
- `productFamilyExternalId` - External system ID

### Relations
- `relProductFamilyToProvider` - Relation to providers
- `relProductFamilyToApplication` - Relation to applications
- `relProductFamilyToITComponent` - Relation to IT components
- `relProductFamilyToTBMCategory` - Relation to TBM categories
- `relProductFamilyToTechnopediaTechStack` - Relation to tech stacks
- `relToChild` - Child relationships
- `relToParent` - Parent relationships

### System Fields (Read-Only)
- `id` - Unique identifier
- `name` - Product family name
- `displayName` - Display name
- `fullName` - Full name
- `type` - Type (ProductFamily)
- `status` - Status (ACTIVE/ARCHIVED)
- `level` - Hierarchy level
- `completion` - Completion percentage
- `createdAt` - Creation timestamp
- `updatedAt` - Last update timestamp
- `rev` - Revision number
- `permissions` - User permissions
- `permittedReadACL` - Read access control
- `permittedWriteACL` - Write access control
- `subscriptions` - User subscriptions
- `tags` - Tags
- `documents` - Attached documents
- `comments` - Comments
- `category` - Category
- `lxState` - LeanIX state (e.g., DRAFT)
- `lxMilestones` - Milestones
- `lxExcludeFromQuota` - Exclude from quota flag
- `lxTransformationsFutureFactSheet` - Future transformations
- `naFields` - Not available fields
- `asOfDate` - As-of date

---

## ITComponent (123 fields)

### Key Fields
- `baseName` - Base component name
- `version` - Version number
- `edition` - Edition (e.g., Enterprise, Community)
- `componentType` - Type of component
- `componentFamily` - Component family
- `componentWebsite` - Official website
- `description` - Component description

### Alias Fields (Integration Systems)
- `MDCAAlias` - MDCA alias
- `MSEntraAlias` - Microsoft Entra alias
- `NetskopeAlias` - Netskope alias
- `OktaAlias` - Okta alias
- `SAPAlias` - SAP alias
- `SBOMAlias` - SBOM alias
- `ServiceNowAlias` - ServiceNow alias
- `WalkMeAlias` - WalkMe alias
- `ZscalerAlias` - Zscaler alias
- `countServicenowAlias` - Count of ServiceNow aliases

### Lifecycle Management
- `lifecycle` - Current lifecycle phase
- `lxVendorLifecycle` - Vendor lifecycle status
- `lxVendorLifecycleComment` - Lifecycle comments
- `lifeCycleLastChecked` - Last lifecycle check date
- `countOfLifecycles` - Number of lifecycle entries

### Lifecycle Policy
- `lifecyclePolicyName` - Policy name
- `lifecyclePolicyDesc` - Policy description
- `lifecyclePolicyUrl` - Policy documentation URL
- `DoesLifecyclePolicyExists` - Policy exists flag
- `DoesVersionHaveActiveSupport` - Active support flag

### End of Life (EOL) Information
- `IsEndOfLifeFromPolicy` - EOL from policy flag
- `IsPhaseOutFromPolicy` - Phase out flag
- `endOfSaleDate` - End of sale date
- `endOfSaleDateUrl` - EOL information URL
- `endOfLifeDateUrl` - EOL date URL

### Support Information
- `supportType` - Type of support
- `IsPaidSupportAvailAfterEndOfLife` - Paid support after EOL
- `IsPaidSupportAvailUntilEndOfLife` - Paid support until EOL
- `IsPaidSupportAvailUntilPhaseOut` - Paid support until phase out
- `lastDateOfPaidSupportAfterEndOfLife` - Last paid support date
- `SupportDateUrlPostEndOfLife` - Support date URL

### Version Information
- `versionType` - Version type (Major, Minor, Patch)
- `versionGroup` - Version grouping
- `versionInformation` - Additional version info
- `latestVersion` - Latest available version
- `countOfSuccessors` - Count of successor versions
- `countOfMajorSuccessors` - Major version successors
- `countOfMinorSuccessors` - Minor version successors
- `countOfPatchSuccessors` - Patch version successors

### Phase Dates & URLs
- `activeDateUrl` - Active date URL
- `planDateUrl` - Plan date URL
- `phaseInDateUrl` - Phase in date URL
- `phaseOutDateUrl` - Phase out date URL
- `announcementURL` - Announcement URL

### Discovery & Coverage
- `discoverySource` - Discovery source
- `discoveryCoverageStatus` - Discovery coverage status
- `cdkCoverageStatus` - CDK coverage status
- `ltlsCoverageStatus` - LTLS coverage status
- `mappedtoCloudockit` - Cloudockit mapping
- `mappedtoLeanIXDiscovery` - LeanIX Discovery mapping
- `ltlsCIMappingDefinedCDK` - CDK mapping defined
- `ltlsCIMappingDefinedLCD` - LCD mapping defined

### Cloud Component Queries
- `hasCloudComponentQueries` - Has cloud queries flag
- `cloudComponentQueries` - Cloud component queries

### Classification & Assessment
- `classificationLevel` - Classification level
- `assessmentCategory` - Assessment category
- `isHostingItc` - Hosting ITC flag
- `maintenanceFlag` - Maintenance flag

### External IDs
- `externalId` - External system ID
- `itComponentExternalId` - IT component external ID
- `productId` - Product ID

### Research & Comments
- `internalResearchComments` - Internal research notes
- `collectionComment` - Collection comments
- `collectionStatus` - Collection status

### Relations
- `relITComponentToApplication` - Relation to applications
- `relITComponentToProvider` - Relation to providers
- `relITComponentToProductFamily` - Relation to product families
- `relITComponentToLTLSRequest` - Relation to LTLS requests
- `relITComponentToTBMCategory` - Relation to TBM categories
- `relITComponentToTechnopediaTechStack` - Relation to tech stacks
- `relToPredecessorITC` - Predecessor component
- `relToSuccessorITC` - Successor component
- `relToChild` - Child relationships
- `relToParent` - Parent relationships

### Regional Link Counts
- Same as Provider (aeCountsOfLinks through totalCountsOfLinksOnCustomer)

### System Fields (Read-Only)
- Similar to Provider (id, name, displayName, status, etc.)

---

## Usage Notes

### Field Types

**Simple Fields (String/Text):**
- Most fields accept simple string values
- Example: `"description": "Sample description"`

**Enum Fields:**
- Some fields only accept specific values
- Example: `providerCategory` has predefined values
- Error message will show if invalid value is provided

**Relation Fields:**
- Fields starting with `rel` are relationships
- These typically require special handling (not simple strings)

**Read-Only Fields:**
- System fields like `id`, `createdAt`, `updatedAt` cannot be modified
- Attempting to update will fail validation

**Regional Count Fields:**
- Fields ending with `CountsOfLinks` are typically read-only
- These are calculated by LeanIX automatically

### Common Update Patterns

**Provider Updates:**
```bash
# Update provider catalog fields
python main.py update \
  --fact-sheet-id "uuid" \
  --type Provider \
  --fields '{
    "homePageUrl": "https://example.com",
    "aliases": "Name1, Name2, Name3",
    "headquartersAddress": "123 Main St, City, State ZIP, Country",
    "description": "Provider description"
  }'
```

**Application Updates:**
```bash
# Update application details
python main.py update \
  --fact-sheet-id "uuid" \
  --type Application \
  --fields '{
    "webpageUrl": "https://app.example.com",
    "description": "Application description",
    "loginUrl": "https://app.example.com/login"
  }'
```

**ITComponent Updates:**
```bash
# Update IT component lifecycle info
python main.py update \
  --fact-sheet-id "uuid" \
  --type ITComponent \
  --fields '{
    "version": "2.5.1",
    "componentWebsite": "https://component.example.com",
    "lifecyclePolicyUrl": "https://vendor.com/lifecycle"
  }'
```

**ProductFamily Updates:**
```bash
# Update product family details
python main.py update \
  --fact-sheet-id "uuid" \
  --type ProductFamily \
  --fields '{
    "productWebsite": "https://product.example.com",
    "description": "Product family description",
    "lifecyclePolicyUrl": "https://vendor.com/lifecycle",
    "aliases": "Product1, Product2"
  }'
```

### Discovering Custom Fields

If your workspace has custom fields not listed here, use the discover command:

```bash
# Discover fields for any type
python main.py discover --type YourCustomType
```

This will update `field_config.json` with all available fields for that type.

---

## Important Notes

1. **Enum Values**: Some fields like `providerCategory` only accept specific enum values. If you get an "unknown enum value" error, check the LeanIX UI for valid values.

2. **Relations**: Fields starting with `rel` are complex relationship fields. Updating these requires special handling beyond simple string values.

3. **Calculated Fields**: Many count and status fields are automatically calculated by LeanIX and cannot be manually updated.

4. **Custom Fields**: Your workspace may have additional custom fields not in the standard LeanIX schema. Use the `discover` command to find them.

5. **Field Validation**: The tool validates field names before making API calls, so you'll get instant feedback if a field name is invalid.

---

## Maintenance

To refresh the field list (e.g., after workspace schema changes):

```bash
# Re-run discovery for each type
python main.py discover --type Provider
python main.py discover --type Application
python main.py discover --type ITComponent
python main.py discover --type ProductFamily
```

This will update `field_config.json` with the latest fields from your workspace.
