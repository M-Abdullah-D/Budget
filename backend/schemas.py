from pydantic import BaseModel

class BudgetCreate(BaseModel):
    category: str
    amount: float
    currency: str = "USD"

class BudgetResponse(BudgetCreate):
    id: int
