#!/bin/bash
set -euo pipefail
shopt -s inherit_errexit

if [[ $# -lt 1 ]]; then
    echo "Usage: $0 <day>"
    exit 1
fi

python -c 'import sys; from runner import run; run(day=int(sys.argv[1]))' "$1"
exit $?
