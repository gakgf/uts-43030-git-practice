#!/usr/bin/env bash
set -euo pipefail
python /app/todo.py | tee /tmp/tasks.txt
python /app/todo-test.py 2>&1 | tee /tmp/tests.txt
bash /app/update_index.sh /tmp/tasks.txt /tmp/tests.txt
echo 'Task manager tests and report completed successfully.'
