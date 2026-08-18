from pydantic import BaseModel, Field, EmailStr, ConfigDict
from datetime import datetime
from typing import Optional


class UserCreate(BaseModel):
    first_name: str = Field(min_length = 2, max_length = 20, description="Users first name")
    middle_name: Optional[str] = Field(default = None, min_length = 2, max_length = 20, description="Users middle name")
    last_name:  str = Field(min_length = 2, max_length = 20, description="Users last name")
    username:   str = Field(min_length = 2, max_length = 20, description="Username")
    email:      EmailStr
    password:   str = Field(min_length=8)
    is_seller: bool = Field(description="If user is seller true else false")
    model_config = ConfigDict(extra = 'forbid')



class UserResponse(BaseModel):
    id: int
    username: str
    email:    EmailStr
    first_name: str
    last_name: str


    


