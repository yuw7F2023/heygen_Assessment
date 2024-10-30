import requests
import time

class HeygenClient:
    def __init__(self, server_url):
        self.server_url = server_url

    def start_job(self):
        response = requests.post(f"{self.server_url}/start_job")
        return response

    def check_status(self, job_id, max_retries=20, initial_delay=1, max_delay=16):
        retries = 0
        delay = initial_delay

        while retries < max_retries:
            response = requests.get(f"{self.server_url}/status/{job_id}")
            if response.status_code == 200:
                result = response.json().get("result")
                print(f"Status of job {job_id}: {result}")
                if result in ["completed", "error"]:
                    return result  
            else:
                print(f"Failed to get status for job {job_id}, retrying...")

            retries += 1
            time.sleep(delay)
            delay = min(delay * 2, max_delay) 
        return "timeout"

# Example usage
if __name__ == '__main__':
    client = HeygenClient("http://localhost:8000")
    response = client.start_job()
    job_id = response.json().get("job_id")
    print(f"Job started with ID: {job_id}")
    client.check_status(job_id)
