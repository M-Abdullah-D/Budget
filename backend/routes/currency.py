import requests
from fastapi import APIRouter

router = APIRouter()

CURRENCY_API_URL = "https://api.exchangerate-api.com/v4/latest/USD"

@router.get("/{currency}")
def get_currency_rate(currency: str):
    response = requests.get(CURRENCY_API_URL)
    data = response.json()
    rate = data["rates"].get(currency.upper())

    if rate:
        return {"currency": currency.upper(), "rate": rate}
    return {"error": "Currency not found"}
