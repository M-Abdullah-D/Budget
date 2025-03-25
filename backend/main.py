from fastapi import FastAPI
from routes import budget, currency

app = FastAPI(title="Personal Budget App API")

# Include routes
app.include_router(budget.router, prefix="/budget", tags=["Budget"])
app.include_router(currency.router, prefix="/currency", tags=["Currency"])

@app.get("/")
def home():
    return {"message": "Welcome to the Personal Budget API"}