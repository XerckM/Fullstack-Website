from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from dotenv import load_dotenv

load_dotenv()

from db import engine, get_db
from models import Base, Project

app = FastAPI(title="Xerckiem Mercado Portfolio API")

Base.metadata.create_all(bind=engine)

@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/projects")
def list_projects(db: Session = Depends(get_db)):
    return db.query(Project).all()
