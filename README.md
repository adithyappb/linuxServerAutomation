## Linux Server Administration and Troubleshooting Automation

## Overview:
This project automates key Linux server administration tasks including log collection, stack trace analysis, configuration management, and system monitoring.

## Features
1) Log Collection and Analysis: Automates log collection, rotation, and archival. Provides tools for log analysis and summary report generation.
2) Stack Trace Navigation: Captures and visualizes stack traces from crashing applications.
3) Configuration Management: Backs up, edits, and restores configuration files. Automates configuration deployment across servers using Ansible.
4) System Monitoring: Sets up monitoring with Prometheus and Grafana, integrates alerting mechanisms via Slack.

## Requirements
Python 3.x
Bash
Ansible
Prometheus
Grafana
Docker
Node.js

## Setup
## Install dependencies:
./install_dependencies.sh

## Configure Ansible:
Update the ansible/hosts file with your server details.

## Run scripts:
Log collection: ./scripts/collect_logs.sh
Stack trace capture: ./scripts/capture_stack_trace.sh
Configuration management: ansible-playbook ansible/playbook.yml
Monitoring setup: ./scripts/setup_monitoring.sh

## Usage
Log Collection and Analysis:
Run ./scripts/collect_logs.sh to collect logs.
Logs are stored in /var/log/myapp/.

## Stack Trace Navigation:
Capture stack traces with ./scripts/capture_stack_trace.sh.
View stack traces on the web interface at http://localhost:8000.

## Configuration Management:
Deploy configurations with ansible-playbook ansible/playbook.yml.

## System Monitoring:
Access Prometheus at http://localhost:9090.
View Grafana dashboards at http://localhost:3000.
