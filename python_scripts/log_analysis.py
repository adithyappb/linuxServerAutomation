import os
import re
from datetime import datetime

LOG_DIR = '/var/log/custom_logs'

def analyze_logs():
    log_summary = {}
    for log_file in os.listdir(LOG_DIR):
        with open(os.path.join(LOG_DIR, log_file)) as file:
            content = file.read()
            log_summary[log_file] = {
                'error_count': len(re.findall(r'ERROR', content)),
                'warning_count': len(re.findall(r'WARNING', content))
            }
    return log_summary

if __name__ == '__main__':
    summary = analyze_logs()
    timestamp = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
    report_file = f'/var/log/log_analysis_{timestamp}.json'
    with open(report_file, 'w') as file:
        json.dump(summary, file)

