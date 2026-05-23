from pydantic import BaseModel
from datetime import date
from typing import Optional

# Common attributes shared when reading or creating data
class ExpenseBase(BaseModel):
    amount: float
    category: str
    description: Optional[str] = None
    date: Optional[date] = None

# Schema used when a user creates a new record (Input)
class ExpenseCreate(ExpenseBase):
    pass

# Schema used when returning data to the user (Output)
class ExpenseResponse(ExpenseBase):
    id: int

    class Config:
        from_attributes = True  # Allows Pydantic to read SQLAlchemy models