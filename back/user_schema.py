from typing import Optional
from pydantic import BaseModel, Field


class User(BaseModel):
    first_name: str
    last_name: str
    patronymic: str
    age: int
    phone_number: str
    email: str
    company: str
    profession: str


class UserPATCH(BaseModel):
    first_name: Optional[str] = Field(None)
    last_name: Optional[str] = Field(None)
    patronymic: Optional[str] = Field(None)
    age: Optional[int] = Field(None)
    phone_number: Optional[str] = Field(None)
    email: Optional[str] = Field(None)
    company: Optional[str] = Field(None)
    profession: Optional[str] = Field(None)