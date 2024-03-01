from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from sqlalchemy import create_engine
from sqlalchemy.exc import OperationalError
import os

DATABASE_URL = f"postgresql://{os.environ['DB_USER']}:{os.environ['DB_PASSWORD']}@db:5432/{os.environ['DB_NAME']}" 

app = FastAPI()
engine = create_engine(DATABASE_URI)

def create_database():
    # Split the connection string into components
    db_parts = DATABASE_URI.split("/")
    db_parts[3] = 'postgres'  # Connect to the default 'postgres' database
    temp_uri = "/".join(db_parts)

    temp_engine = create_engine(temp_uri)

    with temp_engine.connect() as conn:
        conn.execute("COMMIT")  # Required for some databases
        try:
            conn.execute(f"CREATE DATABASE {db_parts[3]}")
        except OperationalError:
            # Database might already exist, that's OK
            pass

create_database()  # Try creating the database
Base.metadata.create_all(engine)


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)