from fastapi import FastAPI, HTTPException
import httpx
from datetime import datetime, timezone

app = FastAPI()


@app.get("/me")
async def get_profile():
    cat_fact_url = "https://catfact.ninja/fact"

    try:
        async with httpx.AsyncClient(timeout=5.0) as client:
            response = await client.get(cat_fact_url)
            response.raise_for_status()
            fact_data = response.json()
            cat_fact = fact_data.get("fact", "Cats are amazing creatures!")
    except Exception as e:
        cat_fact = "Could not fetch cat fact at the moment."

    # Build response
    return {
        "status": "success",
        "user": {
            "email": "abayomidavid334@gmail.com",
            "name": "Abayomi David Olamide",
            "stack": "Python/FastAPI"
        },
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "fact": cat_fact
    }
