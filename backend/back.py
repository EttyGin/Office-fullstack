from fastapi import FastAPI, HTTPException
import uvicorn
from constants import CREATE_URI, DATABASE_NAME, COLLECTION_NAME, CONNECTION_STRING
from database.mongo import Mongo_connection
from database.model import Member
import json
app = FastAPI()


@app.post(CREATE_URI)
def create_member(member: Member):
    m = Mongo_connection(CONNECTION_STRING, DATABASE_NAME, COLLECTION_NAME)
    result = m.create(member)
    


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1")
