# Stage 0 - Dynamic Profile Endpoint

This FastAPI project implements the Stage 0 backend task for HNGi13.  
It exposes a `/me` endpoint that returns my profile and a random cat fact.

## 🚀 Features
- Dynamic UTC timestamp (ISO 8601)
- Fetches a new cat fact on every request
- Graceful error handling
- Simple and lightweight setup

## 🧩 Endpoint
**GET** `/me`

### Response Example
```json
{
  "status": "success",
  "user": {
    "email": "abayomidavidolamide@gmail.com",
    "name": "Abayomi David Olamide",
    "stack": "Python/FastAPI"
  },
  "timestamp": "2025-10-19T17:35:24.362Z",
  "fact": "Cats have 32 muscles in each ear."
}
