#!/usr/bin/env bash
set -euo pipefail
shopt -s inherit_errexit

if [[ $# -lt 2 ]]; then
    echo "Usage: $0 <year> <day>"
    exit 1
fi

year="$1"
day=$(printf "%02d" "$2")

# Forgive my hacky build setup
mkdir -p build hidir odir
cd "$year"
ghc -odir ../odir -hidir ../hidir -o ../build/main --make "$day.hs"
cd ..
< "inputs/$year/$day.txt" build/main
