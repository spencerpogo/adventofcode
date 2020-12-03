#!/bin/bash
set -euo pipefail
shopt -s inherit_errexit

if [[ $# -lt 1 ]]; then
    echo "Usage: $0 <day>"
    exit 1
fi

day=$(printf "%02d" $1)
ghc -odir odir -hidir hidir -o build/main --make "$day.hs"
< "$day.txt" ./build/main
