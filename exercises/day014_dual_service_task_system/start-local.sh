#!/usr/bin/env bash

set -euo pipefail


DAY14_DIR="$(
    cd "$(dirname "${BASH_SOURCE[0]}")"
    pwd
)"

REPO_ROOT="$(
    cd "$DAY14_DIR/../.."
    pwd
)"


PYTHON_DIR="$REPO_ROOT/exercises/day011_fastapi_crud"
JAVA_DIR="$REPO_ROOT/exercises/day012_springboot_crud"

LOG_DIR="$DAY14_DIR/logs"

mkdir -p "$LOG_DIR"


if [[ -z "${DB_PASSWORD:-}" ]]; then
    echo "Please run:"
    echo "export DB_PASSWORD=your_database_password"
    exit 1
fi

export DB_PASSWORD


echo "Starting Python AI service..."

(
    cd "$PYTHON_DIR"

    nohup python -m uvicorn \
        app.main:app \
        --host 127.0.0.1 \
        --port 8000 \
        > "$LOG_DIR/python.log" 2>&1 &

    echo $! > "$DAY14_DIR/.python.pid"
)


echo "Building Java service..."

(
    cd "$JAVA_DIR"
    mvn -q -DskipTests package
)


echo "Starting Java service..."

(
    cd "$JAVA_DIR"

    nohup java -jar \
        target/day012-springboot-crud-0.0.1-SNAPSHOT.jar \
        > "$LOG_DIR/java.log" 2>&1 &

    echo $! > "$DAY14_DIR/.java.pid"
)


echo "Python AI: http://127.0.0.1:8000"
echo "Java API:  http://127.0.0.1:8080"
