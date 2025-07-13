from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from database import get_connection, create_table

app = FastAPI()
create_table()

class City(BaseModel):
    city: str

@app.get("/")
def root():
    return {"message": "Location Service is running"}

@app.post("/locations")
def add_city(city: City):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO locations (city) VALUES (?)", (city.city,))
    conn.commit()
    conn.close()
    return {"message": f"City '{city.city}' added successfully."}

@app.get("/locations")
def get_all_cities():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM locations")
    rows = cursor.fetchall()
    conn.close()
    return [dict(row) for row in rows]
