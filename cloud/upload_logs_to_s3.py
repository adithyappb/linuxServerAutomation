import boto3
import os

LOG_DIR = '/var/log/custom_logs'
BUCKET_NAME = 'your-s3-bucket-name'

def upload_logs():
    s3 = boto3.client('s3')
    for log_file in os.listdir(LOG_DIR):
        s3.upload_file(os.path.join(LOG_DIR, log_file), BUCKET_NAME, log_file)

if __name__ == '__main__':
    upload_logs()

