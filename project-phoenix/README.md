# Project Phoenix

A local-first learning platform for hands-on Agentic AI engineering practice.

## Requirements

- Python 3.13 or later

## Setup

From the repository root, install the small initial dependency set into the existing workspace virtual environment:

```powershell
..\.venv\Scripts\python.exe -m pip install -r project-phoenix\requirements.txt
```

## Run locally

```powershell
..\.venv\Scripts\python.exe -m uvicorn app.main:app --app-dir project-phoenix --reload
```

Open http://127.0.0.1:8000. The health endpoint is available at `/api/health`.

## Test

```powershell
..\.venv\Scripts\python.exe -m pytest project-phoenix\tests
```
