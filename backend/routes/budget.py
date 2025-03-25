from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import SessionLocal
import crud, schemas

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=schemas.BudgetResponse)
def add_budget(budget: schemas.BudgetCreate, db: Session = Depends(get_db)):
    return crud.create_budget(db, budget)

@router.get("/", response_model=list[schemas.BudgetResponse])
def get_all_budgets(db: Session = Depends(get_db)):
    return crud.get_budgets(db)
