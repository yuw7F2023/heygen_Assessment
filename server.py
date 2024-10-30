from flask import Flask, jsonify
import random
import time
import threading

app = Flask(__name__)
status_map = {} 
delay_seconds = 10  # Configurable delay for simulation

@app.route('/status/<job_id>', methods=['GET'])
def get_status(job_id):
    # Simulate different job statuses
    if job_id not in status_map:
        return jsonify({"error": "Job not found"}), 404
    return jsonify({"result": status_map[job_id]}), 200

def simulate_job(job_id, delay):
    """Simulates a long-running job by updating status_map after delay."""
    status_map[job_id] = "pending"
    time.sleep(delay)  
    status_map[job_id] = "completed" if random.random() > 0.1 else "error"  # 10% chance of error

@app.route('/start_job', methods=['POST'])
def start_job():
    job_id = str(random.randint(1, 9999))
    threading.Thread(target=simulate_job, args=(job_id, delay_seconds)).start()
    return jsonify({"job_id": job_id}), 202

if __name__ == '__main__':
    app.run(debug=True, port=8000)
