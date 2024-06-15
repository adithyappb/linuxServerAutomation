import psutil
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/system_monitor')
def system_monitor():
    cpu_usage = psutil.cpu_percent(interval=1)
    memory_info = psutil.virtual_memory()
    disk_usage = psutil.disk_usage('/')
    return jsonify({
        'cpu_usage': cpu_usage,
        'memory_info': {
            'total': memory_info.total,
            'used': memory_info.used,
            'free': memory_info.free,
            'percent': memory_info.percent
        },
        'disk_usage': {
            'total': disk_usage.total,
            'used': disk_usage.used,
            'free': disk_usage.free,
            'percent': disk_usage.percent
        }
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

