To start the server, run the following command:

```
python server.py
```

========================================

To start the client, run the following command:

```
python client.py
```
In the main function of client.py, the client initialize a job by calling the start_job method. It will then send a request to the server to start a job.
After the job is successfully started, the server returns a job_id. The client then calls the check_status method with the job_id to check the status of the job.

========================================

To start the test, run the following commands:

```
python server.py
python test.py
```
