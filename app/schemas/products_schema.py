from pydantic import BaseModel, Field, EmailStr, ConfigDict
from app.schemas.category_response import CategoryResponse
from decimal import Decimal
from uuid import UUID
from datetime import datetime


class ProductCreate(BaseModel):
    store_id: int # This will come from store model
    product_name: str  = Field(..., min_length = 2, max_length = 6)
    product_price: Decimal =  Field(..., ge=0)
    description: str = Field(..., min_length = 2, max_length = 10)
    category_id: UUID = Field(...)
    model_config = ConfigDict(extra="forbid")


class ProductResponse(BaseModel):
    id: int = Field(...)
    store_id: int = Field(...)
    product_name: str = Field(...)
    product_price: str = Field(...)
    description: str = Field(...)
    category: CategoryResponse = Field(...)
    created_at: datetime = Field(...)