#### Director + Celery + Redis https://github.com/glenn-mohre-lab49/director_demo

Director is a framework for magaging tasks and building workflows using Celery.

The demo implementation includes a requirements.txt file. This is required to run the application.
The DB must also be init'd and upgraded.
Instructions:
- `pip install -r requirements.txt`
- `director db init`
- `director db upgrade`

The configured workflows are defined in the workflows.yml file. The workflows reference the tasks defined in `/tasks/`
These files must be in the path defined by the configuration variable [dags_folder](https://airflow.apache.org/docs/apache-airflow/stable/configurations-ref.html#dags-folder).
To define periodic running of a task, you add [entries](https://docs.celeryq.dev/en/stable/userguide/periodic-tasks.html#entries) to the beat schedule list

---

Director includes a few key [commands](https://ovh.github.io/celery-director/#commands)

`director webserver`
- This will start the webserver for monitoring and executing jobs.

---
`director celery worker`
- This will start the Celery worker daemon, which will listen to the Redis broker for messages.
---
`director celery beat`
- This will start the Celery beat daemon, which will execute the defined periodic tasks.
  
#### MVP Requirements

##### Schedule a job and be notified when it completes
You can run [Workflows](https://ovh.github.io/celery-director/guides/run-workflows/) a variety of ways.
Running one via the API, and defining the [ETA](https://docs.celeryq.dev/en/latest/userguide/calling.html#eta-and-countdown) is how to schedule tasks with Celery.

---
###### Have my job be handled by an agent from a pool
The demo implementation uses a Celery as the [Executor](https://airflow.apache.org/docs/apache-airflow/stable/executor/index.html) of the task.
Configuration of Celery includes [configuration](https://docs.celeryq.dev/en/3.1/configuration.html#celeryd-concurrency) for managing the number of concurrent workers.

---
##### Have a UI to monitor active jobs
The `director webserver` command runs a webserver FOR workflow monitoring and execution.

This command also runs [Celery Flower](https://flower.readthedocs.io/en/latest/) which is used for monitoring the Celery Workers
Airflow includes a webserver running a [UI](https://airflow.apache.org/docs/apache-airflow/stable/ui.html)

---
##### Define a job via API so new job types don't require deployments.
This hasn't been solved yet. The key will be to deploy new `workflow.yml` and restart the monitoring
application, so it will find the newly defined workflows.

---
##### Benefits of Director
- Provides an API for execution any defined workflow
- Workflows are defined by static YML files
- Includes a webserver for monitoring tasks

##### Challenges of Director
- Not the best solution for cron jobs created by an API call, since it can only be loaded on configuration.connect
- Could be used to sync from some Alloy endpoint at a regular interval to pick up items marked as jobs.

---
### Technology Solutions Glossary


#### Director - https://github.com/ovh/celery-director
A framework for managing tasks and building workflows with Celery

---
##### Celery - https://docs.celeryq.dev/
Celery is a distributed task queue. Scheduling and orchestration are best handled using a DB backed Scheduler or a framework.

---
##### Celery Beat 
Celery Beat is the built-in scheduler.

---
##### Celery Flower
Flower is a tool for monitoring Celery clusters, and is leveraged by Director for task level monitoring.

---
##### Celery Worker - https://docs.celeryq.dev/en/stable/userguide/workers.html
The Worker handles Tasks from the Celery application, as received from the Broker

---
##### Redis as Celery Broker - https://docs.celeryq.dev/en/stable/getting-started/backends-and-brokers/index.html#redis
Key-value store, frequently used as the Broker for Celery messages.
