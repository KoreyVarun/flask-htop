from flask import Flask
import os
import time
import subprocess

app = Flask(__name__)

@app.route('/htop')
def htop():
    name = "Korey Varun"
    username = os.getenv("USER") or os.getenv("USERNAME")
    server_time = time.strftime('%Y-%m-%d %H:%M:%S IST', time.localtime())

    # Run the top command and get the output (Linux)
    try:
        top_output = subprocess.check_output("tasklist", shell=True).decode()
    except Exception as e:
        top_output = str(e)

    return f"""
    <h1>System Information</h1>
    <p><strong>Name:</strong> {name}</p>
    <p><strong>Username:</strong> {username}</p>
    <p><strong>Server Time:</strong> {server_time}</p>
    <pre>{top_output}</pre>
    """

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
