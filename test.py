import subprocess
import requests
import time
from client import HeygenClient

# Start server
server_process = subprocess.Popen(['python', 'server.py'])

try:
    # Start a job
    response = requests.post("http://localhost:8000/start_job")
    job_id = response.json().get("job_id")
    print(f"Job started with ID: {job_id}")

    # Check status with client library 
    client = HeygenClient("http://localhost:8000")
    result = client.check_status(job_id)
    print(f"Result for job {job_id}: {result}")

finally:
    # Stop the server
    server_process.terminate()
    server_process.wait()
