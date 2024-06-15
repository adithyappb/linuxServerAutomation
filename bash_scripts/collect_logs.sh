#!/bin/bash

LOG_DIR="/var/log/custom_logs"
mkdir -p $LOG_DIR

# Collect logs from Apache
cp /var/log/apache2/*.log $LOG_DIR/

# Collect logs from MySQL
cp /var/log/mysql/*.log $LOG_DIR/

# Collect system logs
cp /var/log/syslog $LOG_DIR/

