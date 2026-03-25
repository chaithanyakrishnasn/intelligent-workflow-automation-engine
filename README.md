# Intelligent Workflow Automation Engine

An end-to-end workflow automation platform that enables users to define triggers and actions for automated task execution with scheduling, retries, and monitoring capabilities.

---

## Features

- FastAPI-based backend with REST APIs  
- PostgreSQL database with SQLAlchemy ORM  
- Workflow creation and management (CRUD)  
- Timer-based automation using APScheduler  
- Webhook-based event-driven execution  
- Modular action engine using Factory pattern  
- Execution logging and monitoring APIs  
- Retry mechanism for failure handling  
- Workflow enable/disable lifecycle control  

---

## Current Demo Capabilities

- Create and manage workflows  
- Attach timer or webhook triggers  
- Execute workflows manually or automatically  
- Log execution results with status tracking  
- Retry failed executions automatically  
- Monitor system metrics via dashboard APIs  
- Enable/disable workflows dynamically  
- Trigger workflows via external HTTP requests  

---

## Project Architecture

```
app/
├── api/        # FastAPI endpoints (workflow, trigger, action, logs, dashboard)
├── services/   # Business logic (workflow_service, execution_service)
├── actions/    # Action engine (base, log_action, factory)
├── models/     # Database models (Workflow, Trigger, Action, ExecutionLog)
├── schemas/    # Pydantic schemas
├── core/       # Database, scheduler, enums
└── main.py     # Application entry point
```

---

## Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/intelligent-workflow-automation-engine.git
cd intelligent-workflow-automation-engine
```

---

### 2. Setup Environment

Ensure you have:

- Python 3 installed  
- Virtual environment activated  

Install dependencies:

```bash
pip install -r requirements.txt
```

---

### 3. Configure Environment Variables

Create a `.env` file:

```
DATABASE_URL=postgresql://postgres:password@localhost:5432/automation_engine
```

---

### 4. Run the Backend

```bash
python -m uvicorn app.main:app --reload
```

Access API docs:

```
http://127.0.0.1:8000/docs
```

---

## Core Features Breakdown

- Workflow module manages automation definitions  
- Trigger system supports timer and webhook execution  
- Scheduler runs background jobs using APScheduler  
- Execution engine processes workflows dynamically  
- Action factory enables pluggable action handlers  
- Retry system ensures fault tolerance  
- Execution logs track system activity  
- Dashboard API provides monitoring metrics  

---

## API Endpoints

### Workflow APIs

- `POST /workflows`
- `GET /workflows`
- `PUT /workflows/{id}`
- `DELETE /workflows/{id}`
- `PATCH /workflows/{id}/enable`
- `PATCH /workflows/{id}/disable`

### Trigger APIs

- `POST /triggers/{workflow_id}`

### Action APIs

- `POST /actions/{workflow_id}`

### Execution APIs

- `POST /execute/{workflow_id}`

### Webhook APIs

- `POST /trigger/webhook/{workflow_id}`

### Logs & Monitoring APIs

- `GET /logs`
- `GET /logs/{workflow_id}`
- `GET /logs/latest`
- `GET /dashboard/stats`

---

## Example Workflow

### 1. Create Workflow

```json
POST /workflows
{
  "name": "Test Workflow",
  "description": "Sample automation"
}
```

---

### 2. Attach Action

```json
POST /actions/{workflow_id}
{
  "type": "log",
  "config": "{}"
}
```

---

### 3. Attach Timer Trigger

```json
POST /triggers/{workflow_id}
{
  "type": "timer",
  "config": "10"
}
```

---

### 4. Automatic Execution

- Workflow runs every 10 seconds  
- Logs stored in database  

---

### 5. Trigger via Webhook

```
POST /trigger/webhook/{workflow_id}
```

---

## Example Output

```json
{
  "status": "SUCCESS",
  "message": "Action executed successfully",
  "workflow_id": 1
}
```

---

## Full Demo Flow

The system can run manually or automatically:

1. Create workflow  
2. Attach trigger and action  
3. Scheduler registers job  
4. Workflow executes automatically  
5. Action is processed  
6. Logs are stored  
7. Failures trigger retries  
8. Metrics available via dashboard  

---

## Real vs System Components

### Real Implementations

- REST API backend with FastAPI  
- PostgreSQL database integration  
- Scheduler-based automation  
- Webhook event handling  
- Retry and failure management  
- Execution logging and monitoring  

### System Design Components

- Factory pattern for action engine  
- Service-layer architecture  
- Event-driven and scheduled execution  
- Modular and extensible backend design  

---

## Best Demo Mode

For best demonstration:

- Create a workflow  
- Attach timer trigger (10 seconds)  
- Attach log action  
- Observe automatic execution logs  
- Trigger via webhook  
- View dashboard stats  

---

## Technologies Used

- Python  
- FastAPI  
- PostgreSQL  
- SQLAlchemy  
- APScheduler  
- Pydantic  
- Git & GitHub  

---

## Future Enhancements

- Email and webhook actions  
- User authentication (JWT)  
- Frontend dashboard  
- Distributed task queue (Celery/Redis)  
- Docker deployment  
- Cloud hosting  
- Advanced analytics and alerting  

---

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss proposed updates.

---

## Support

If you found this project useful, consider giving it a star on GitHub.
