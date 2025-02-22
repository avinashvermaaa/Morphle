from flask import Flask
import os
import subprocess
from datetime import datetime
import pytz

app = Flask(__name__)
@app.route('/http')
def htop():
    full_name = "avinash"
    username = os.getenv("USER") or os.getenve("USERNAME")
    ist_time = datetime.now(pytz.timezone('Asia/Kolkata')).strftime('%y-%m-%d %H:%M:%S IST')
    top_output = subprocess.getoutput("top -b -n 1 | head -10")
    response = f"""
    <h1>System Info</h1>
    <p><b>Name:</b> {full_name}</p>
    <p><b>Username:</b> {username}</p>
    <p><b>Server Time (IST):</b> {ist_time}</p>
    <h2>Top Command Output:</h2>
    <pre>{top_output}</pre>
    """
    return response

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
