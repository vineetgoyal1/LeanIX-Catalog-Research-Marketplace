#!/bin/bash
# Post-creation review script for Application fact sheets
# Verifies that workflow was followed correctly

set -e

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

if [ $# -lt 2 ]; then
    echo "Usage: ./review_application.sh FACT_SHEET_ID APP_NAME"
    echo "Example: ./review_application.sh 12345-abc-def \"TeamSmart AI\""
    exit 1
fi

FACT_SHEET_ID=$1
APP_NAME=$2
DATE=$(date +%Y-%m-%d)
EXEC_DIR="executions/${APP_NAME// /_}_${DATE}"

echo "========================================================================"
echo "APPLICATION CREATION REVIEW"
echo "========================================================================"
echo "Fact Sheet ID: $FACT_SHEET_ID"
echo "Application: $APP_NAME"
echo "Execution Directory: $EXEC_DIR"
echo ""

# Check 1: Execution directory exists
echo "1. Checking Execution Directory..."
if [ ! -d "$EXEC_DIR" ]; then
    echo -e "${RED}❌ FAIL: Execution directory not found: $EXEC_DIR${NC}"
    echo "   Create directory with: mkdir -p \"$EXEC_DIR\""
    exit 1
fi
echo -e "${GREEN}✓ Execution directory exists${NC}"
echo ""

# Check 2: Checklist exists
echo "2. Checking EXECUTION_CHECKLIST.md..."
if [ ! -f "$EXEC_DIR/EXECUTION_CHECKLIST.md" ]; then
    echo -e "${RED}❌ FAIL: EXECUTION_CHECKLIST.md not found${NC}"
    echo "   Copy template: cp EXECUTION_CHECKLIST_TEMPLATE.md \"$EXEC_DIR/EXECUTION_CHECKLIST.md\""
    exit 1
fi
echo -e "${GREEN}✓ Checklist file exists${NC}"

# Check 3: Matrix completed
echo "3. Checking Hosting Type Evaluation Matrix..."
if grep -q "__/10" "$EXEC_DIR/EXECUTION_CHECKLIST.md"; then
    echo -e "${RED}❌ FAIL: Evaluation matrix not completed${NC}"
    echo "   All 6 hosting types must be scored"
    exit 1
fi
echo -e "${GREEN}✓ Matrix completed (all 6 types scored)${NC}"
echo ""

# Check 4: Final fields exist
echo "4. Checking final_fields.json..."
if [ -f "$EXEC_DIR/final_fields.json" ]; then
    echo -e "${GREEN}✓ final_fields.json exists${NC}"
else
    echo -e "${YELLOW}⚠️  Warning: final_fields.json not found (should be saved for reference)${NC}"
fi
echo ""

# Check 5: Run validation script
echo "5. Running Validation Script..."
if [ -f "$EXEC_DIR/final_fields.json" ]; then
    python lib/validate_application.py \
        --checklist "$EXEC_DIR/EXECUTION_CHECKLIST.md" \
        --fields "$EXEC_DIR/final_fields.json"
    VALIDATION_RESULT=$?
else
    python lib/validate_application.py \
        --checklist "$EXEC_DIR/EXECUTION_CHECKLIST.md"
    VALIDATION_RESULT=$?
fi

if [ $VALIDATION_RESULT -ne 0 ]; then
    echo -e "${RED}❌ FAIL: Validation script found errors${NC}"
    exit 1
fi
echo ""

# Check 6: Hosting matrix file
echo "6. Checking hosting_matrix.md..."
if [ -f "$EXEC_DIR/hosting_matrix.md" ]; then
    echo -e "${GREEN}✓ hosting_matrix.md exists${NC}"
else
    echo -e "${YELLOW}⚠️  Warning: hosting_matrix.md not found (recommended for audit trail)${NC}"
fi
echo ""

# Summary
echo "========================================================================"
echo "REVIEW SUMMARY"
echo "========================================================================"
echo -e "${GREEN}✓ Execution directory exists${NC}"
echo -e "${GREEN}✓ Checklist completed${NC}"
echo -e "${GREEN}✓ Matrix completed (all 6 types scored)${NC}"
echo -e "${GREEN}✓ Validation passed${NC}"
echo ""
echo -e "${GREEN}✅ APPLICATION CREATION FOLLOWED WORKFLOW CORRECTLY${NC}"
echo ""
echo "Fact Sheet URL:"
echo "https://demo-eu-10.leanix.net/ltlsCollectionTesting/factsheet/Application/$FACT_SHEET_ID"
echo ""
echo "Execution record saved in: $EXEC_DIR"
echo ""
