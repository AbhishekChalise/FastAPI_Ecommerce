from pydantic import BaseModel
from uuid import UUID
from datetime import datetime

class CategoryCreate(BaseModel):
    category_name: str

class CategoryResponse(BaseModel):
    id: UUID
    category_name: str 