from flask import Flask, render_template_string

app = Flask(__name__)

@app.route('/stack_trace')
def stack_trace():
    with open('/var/log/stack_trace.log') as file:
        stack_trace_content = file.read()
    return render_template_string("""
    <html>
      <body>
        <h1>Stack Trace</h1>
        <pre>{{ stack_trace_content }}</pre>
      </body>
    </html>
    """, stack_trace_content=stack_trace_content)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

