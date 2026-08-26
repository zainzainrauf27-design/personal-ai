# Backend Structure

The backend is responsible for connecting the user interface with the Personal AI's core services.

## Current Files

### main.py

The initial FastAPI application.

Responsibilities:

- Start the backend application
- Provide the root endpoint
- Provide the health-check endpoint

### requirements.txt

Contains the Python dependencies required by the backend.

## Planned Structure

The backend will eventually be organized into separate modules.

```text
backend/
│
├── main.py
├── requirements.txt
│
├── api/
├── auth/
├── services/
├── models/
├── database/
├── middleware/
├── security/
└── utils/
