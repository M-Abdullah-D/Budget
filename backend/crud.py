from sqlalchemy.orm import Session
from models import Budget
from schemas import BudgetCreate

def create_budget(db: Session, budget: BudgetCreate):
    new_budget = Budget(category=budget.category, amount=budget.amount, currency=budget.currency)
    db.add(new_budget)
    db.commit()
    db.refresh(new_budget)
    return new_budget

def get_budgets(db: Session):
    return db.query(Budget).all()
