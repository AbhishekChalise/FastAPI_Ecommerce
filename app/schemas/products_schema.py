from pydantic import BaseModel, Field, EmailStr, ConfigDict
from decimal import Decimal
from datetime import datetime

class ProductCreate(BaseModel):
    store_id: int # This will come from store model
    product_name: str  = Field(..., min_length = 2, max_length = 6)
    product_price: Decimal =  Field(..., ge=0)
    description: str = Field(..., min_length = 2, max_length = 10)
    category: str = Field(...)
    model_config = ConfigDict(extra="forbid")

class ProductResponse(BaseModel):
    id: int
    store_id: int
    product_name: str
    product_price: str
    description: str
    category: str  # will come from category model
    created_at: datetime


