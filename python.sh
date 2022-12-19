#!/usr/bin/env bash
set -euo pipefail
shopt -s inherit_errexit

if [[ $# -lt 2 ]]; then
    echo "Usage: $0 <year> <day>"
    exit 1
fi

year="$1"
day="$2"
repo="$(dirname "$(realpath "$0")")"

PYTHONPATH="$repo/$year${PYTHONPATH:+:PYTHONPATH}" python -c \
    'import sys; from runner import run; run(year=int(sys.argv[1]), day=int(sys.argv[2]))' \
    "$year" "$day"
exit $?
