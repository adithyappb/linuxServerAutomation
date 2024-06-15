#!/bin/bash

PID=$(pgrep -f "application_name")
if [ -n "$PID" ]; then
  gdb -p $PID -ex "set pagination 0" -ex "thread apply all bt" -ex "quit" > /var/log/stack_trace.log
else
  echo "Application is not running."
fi

