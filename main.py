from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class QueryRequest(BaseModel):
    question: str

@app.get("/")
def health_check():
    return {"status": "RAG server running"}

@app.post("/query")
def query(request: QueryRequest):
    return {"answer": f"Question was: {request.question}"}
