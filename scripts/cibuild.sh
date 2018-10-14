#!/bin/bash

# Exit code starts at 0 but is modified if any checks fail
EXIT=0

info()
{
    echo "$(date +'%F %T') |"
}

# Track number of seconds to run script
START=$(date +%s)
echo "$(info) starting build checks."

# Syntax check all python source files
SYNTAX=$(find . -name "*.py" -type f -exec python -m py_compile {} \; 2>&1)
if [[ ! -z $SYNTAX ]]; then
	echo -e "$SYNTAX"
	echo -e "\n$(info) detected one or more syntax errors, failing build."
	EXIT=1
fi

# Check all python source files for PEP 8 compliance, but explicitly
# ignore:
#  - E501: line greater than 80 characters in length
pycodestyle \
    --ignore=E501 \
    ./
RC=$?
if [[ $RC != 0 ]]; then
	echo -e "\n$(info) one or more PEP 8 errors detected, failing build."
	EXIT=$RC
fi

# Run unit tests
python3 manage.py test bands
RC=$?
if [[ $RC !=0 ]]; then
	echo -e "\n$(info) one or more unit tests failed, failing build."
fi
