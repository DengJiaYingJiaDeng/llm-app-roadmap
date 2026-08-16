#!/usr/bin/env bash

set -euo pipefail


DAY14_DIR="$(
    cd "$(dirname "${BASH_SOURCE[0]}")"
    pwd
)"


for pid_file in \
    "$DAY14_DIR/.java.pid" \
    "$DAY14_DIR/.python.pid"
do

    if [[ -f "$pid_file" ]]; then

        pid="$(cat "$pid_file")"

        kill "$pid" 2>/dev/null || true

        rm -f "$pid_file"
    fi

done


echo "Local services stopped."
