# JWT Authentication API

Minimal FastAPI service for secure JWT token generation and validation. T

## Features

- Token generation with expiration
- Secure token validation
- Environment-based configuration
- Automated test coverage

## Installation

1. Clone the repository:
   `git clone https://github.com/BigyaDhungana/Minimal-JWT-Auth.git`
   `cd Minimal-JWT-Auth`

2. Set up environment:
   `cp .env.example .env`
   (Edit .env with your secret values)

3. Create virtual environment:
   `python -m venv .venv`

4. Activate environment:

- Linux/Mac: `source .venv/bin/activate`
- Windows: `.venv\Scripts\activate`

5. Install dependencies:
   `pip install -r requirements.txt`

## Running the Application

Start development server:
`uvicorn app.main:app --reload`

## Docker

1. To build and run
   `docker compose build --no-cache && docker compose up -d`

2. To stop
   `docker compose down`

the app is running in http://0.0.0.0:8000/ and docs is available in http://0.0.0.0:8000/docs

API Endpoints:

```
POST /token/{username}  # Generate token
GET /check/            # Validate token
```
