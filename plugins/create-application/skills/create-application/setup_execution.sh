#!/bin/bash
# Setup script for creating a new Application execution
# Creates directory structure and templates for the agent to complete

if [ $# -lt 1 ]; then
    echo "Usage: ./setup_execution.sh \"Application Name\""
    echo "Example: ./setup_execution.sh \"TeamSmart AI\""
    exit 1
fi

APP_NAME=$1
DATE=$(date +%Y-%m-%d)
EXEC_DIR="executions/${APP_NAME// /_}_${DATE}"

echo "========================================================================"
echo "APPLICATION EXECUTION SETUP"
echo "========================================================================"
echo "Application: $APP_NAME"
echo "Date: $DATE"
echo "Execution Directory: $EXEC_DIR"
echo ""

# Create execution directory
echo "Creating execution directory..."
mkdir -p "$EXEC_DIR"
echo "✓ Created: $EXEC_DIR"

# Copy checklist template
echo "Copying execution checklist template..."
cp EXECUTION_CHECKLIST_TEMPLATE.md "$EXEC_DIR/EXECUTION_CHECKLIST.md"
echo "✓ Created: $EXEC_DIR/EXECUTION_CHECKLIST.md"

# Generate hosting matrix
echo "Generating hosting type evaluation matrix..."
python lib/generate_matrix.py "$APP_NAME" > "$EXEC_DIR/hosting_matrix.md"
echo "✓ Created: $EXEC_DIR/hosting_matrix.md"

# Create placeholder for final fields
echo "Creating placeholder for final fields..."
cat > "$EXEC_DIR/final_fields.json" << 'EOF'
{
  "siId": "",
  "category": "businessApplication",
  "webpageUrl": "",
  "hostingType": "",
  "hostingDescription": "",
  "ssoStatus": "",
  "pricingType": "",
  "productCategory": "",
  "alias": "",
  "description": "",
  "collectionStatus": "inReview",
  "deprecated": "No",
  "asOfDate": ""
}
EOF
echo "✓ Created: $EXEC_DIR/final_fields.json (template)"

# Create README for this execution
cat > "$EXEC_DIR/README.md" << EOF
# Application Execution: $APP_NAME
**Date**: $DATE
**Fact Sheet ID**: [TO BE FILLED]

## Workflow Steps

1. **Complete EXECUTION_CHECKLIST.md**
   - Read all 11 guidelines
   - Execute parallel research
   - Document all findings

2. **Complete hosting_matrix.md**
   - Score all 6 hosting types (0-10)
   - Provide reasoning for each score
   - Make final decision with confidence level

3. **Save research data** (optional but recommended):
   - research_perplexity.json - Raw Perplexity response
   - research_webfetch.json - Raw WebFetch responses

4. **Update final_fields.json**
   - Fill in all field values
   - Ensure correct enum values (deprecated="No", category="businessApplication")

5. **Run validation**:
   \`\`\`bash
   python ../lib/validate_application.py \\
     --checklist EXECUTION_CHECKLIST.md \\
     --fields final_fields.json
   \`\`\`

6. **Create fact sheet** (after validation passes)

7. **Run post-creation review**:
   \`\`\`bash
   cd ..
   ./lib/review_application.sh [FACT_SHEET_ID] "$APP_NAME"
   \`\`\`

## Files in This Directory

- \`EXECUTION_CHECKLIST.md\` - Main checklist (complete this first)
- \`hosting_matrix.md\` - Hosting type evaluation matrix (complete this)
- \`final_fields.json\` - Final field values for LeanIX (update this)
- \`research_perplexity.json\` - (optional) Raw Perplexity data
- \`research_webfetch.json\` - (optional) Raw WebFetch data
- \`verification_report.md\` - (optional) Detailed source comparison

## Validation Commands

Before creating the fact sheet:
\`\`\`bash
# Run validation
python ../lib/validate_application.py \\
  --checklist EXECUTION_CHECKLIST.md \\
  --fields final_fields.json

# All checks should pass before proceeding
\`\`\`

After creating the fact sheet:
\`\`\`bash
# Run post-creation review
cd ..
./lib/review_application.sh [FACT_SHEET_ID] "$APP_NAME"
\`\`\`
EOF
echo "✓ Created: $EXEC_DIR/README.md"

echo ""
echo "========================================================================"
echo "SETUP COMPLETE"
echo "========================================================================"
echo ""
echo "Next steps:"
echo "1. cd $EXEC_DIR"
echo "2. Complete EXECUTION_CHECKLIST.md"
echo "3. Complete hosting_matrix.md"
echo "4. Run validation:"
echo "   python ../lib/validate_application.py \\"
echo "     --checklist EXECUTION_CHECKLIST.md \\"
echo "     --fields final_fields.json"
echo ""
echo "5. After validation passes, create the fact sheet"
echo "6. Run review:"
echo "   cd .. && ./lib/review_application.sh [FACT_SHEET_ID] \"$APP_NAME\""
echo ""
