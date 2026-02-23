# Application Execution Records

This directory contains execution records for each Application fact sheet created.

Each execution should have its own subdirectory named: `ApplicationName_YYYY-MM-DD`

## Required Files Per Execution:

1. **EXECUTION_CHECKLIST.md** (mandatory) - Copy from EXECUTION_CHECKLIST_TEMPLATE.md and complete
2. **hosting_matrix.md** (mandatory) - Generate with `python lib/generate_matrix.py "App Name"`
3. **research_perplexity.json** (optional) - Raw Perplexity research data
4. **research_webfetch.json** (optional) - Raw WebFetch research data
5. **verification_report.md** (optional) - Detailed comparison of sources
6. **final_fields.json** (mandatory) - Final field values uploaded to LeanIX

## Example Structure:

```
executions/
├── TeamSmart_AI_2026-02-22/
│   ├── EXECUTION_CHECKLIST.md
│   ├── hosting_matrix.md
│   ├── research_perplexity.json
│   ├── research_webfetch.json
│   ├── verification_report.md
│   └── final_fields.json
├── Salesforce_2026-02-23/
│   ├── EXECUTION_CHECKLIST.md
│   ├── hosting_matrix.md
│   └── final_fields.json
```

## Usage:

Before creating an Application, create the execution directory:

```bash
APP_NAME="Application Name"
DATE=$(date +%Y-%m-%d)
EXEC_DIR="executions/${APP_NAME// /_}_${DATE}"

mkdir -p "$EXEC_DIR"
cp EXECUTION_CHECKLIST_TEMPLATE.md "$EXEC_DIR/EXECUTION_CHECKLIST.md"
python lib/generate_matrix.py "$APP_NAME" > "$EXEC_DIR/hosting_matrix.md"
```

Then complete the checklist and matrix before creating the fact sheet.

## Validation:

After completing execution, run validation:

```bash
python lib/validate_application.py \
  --checklist "$EXEC_DIR/EXECUTION_CHECKLIST.md" \
  --fields "$EXEC_DIR/final_fields.json"
```

## Audit Trail:

These execution records serve as:
- Proof that workflow was followed correctly
- Audit trail for data quality
- Reference for future applications
- Training material for new agents
- Evidence for compliance reviews
