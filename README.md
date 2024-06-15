## Linux Server Administration and Troubleshooting Automation

## Overview:
This project automates key Linux server administration tasks including log collection, stack trace analysis, configuration management, and system monitoring.

## Features
1) Log Collection and Analysis: Automates log collection, rotation, and archival. Provides tools for log analysis and summary report generation.
2) Stack Trace Navigation: Captures and visualizes stack traces from crashing applications.
3) Configuration Management: Backs up, edits, and restores configuration files. Automates configuration deployment across servers using Ansible.
4) System Monitoring: Sets up monitoring with Prometheus and Grafana, integrates alerting mechanisms via Slack.

## Requirements
1) Python 3.x
2) Bash
3) Ansible
4) Prometheus
5) Grafana
6) Docker
7) Node.js

## Setup
## Install dependencies:
./install_dependencies.sh

## Configure Ansible:
Update the ansible/hosts file with your server details.

## Run scripts:
1) Log collection: ./scripts/collect_logs.sh
2) Stack trace capture: ./scripts/capture_stack_trace.sh
3) Configuration management: ansible-playbook ansible/playbook.yml
4) Monitoring setup: ./scripts/setup_monitoring.sh

## Usage
1) Log Collection and Analysis:
2) Run ./scripts/collect_logs.sh to collect logs.
3) Logs are stored in /var/log/myapp/.

## Stack Trace Navigation:
1) Capture stack traces with ./scripts/capture_stack_trace.sh.
2) View stack traces on the web interface at http://localhost:8000.

## Configuration Management:
Deploy configurations with ansible-playbook ansible/playbook.yml.

## System Monitoring:
1) Access Prometheus at http://localhost:9090.
2) View Grafana dashboards at http://localhost:3000.
