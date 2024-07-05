from fastapi import FastAPI
from fastapi.responses import FileResponse
import sqlite3

app = FastAPI()
conn = sqlite3.connect("db/my.db")
cursor = conn.cursor()

@app.get("/")
async def read_index():
    return FileResponse('index.html')

@app.get("/api/books")
async def books():
  cursor.execute("SELECT * FROM BOOK")
  books = []
  for row in cursor.fetchall(): 
    books.append(row[0])
  return books