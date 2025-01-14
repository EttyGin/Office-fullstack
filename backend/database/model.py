from datetime import date
from typing import Self
from pydantic import BaseModel, field_validator, model_validator

class Member(BaseModel):
    id_num: str
    first_name: str
    last_name: str
    address: str
    birth_date: date
    phone: str
    illness_start_date: date
    illness_end_date: date

    @field_validator('id_num')
    def validate_id(val: str) -> str:
        if len(val) != 9 or not val.isnumeric(): 
            raise ValueError("Invalid ID")
        return val
    
    @field_validator('phone')
    def validate_phone(val: str) -> str:
        if not val.startswith("05") or len(val) != 10 or not val.isnumeric(): 
            raise ValueError("Invalid phone number")
        return val
    
    @field_validator('first_name', 'last_name')
    @classmethod
    def validate_names(cls, val: str) -> str:
        if not val.replace(" ", "").isalpha():
            raise ValueError("Ivalid name. Must be alphabetic")
        return val
        
    @field_validator('birth_date')
    def validate_birth_date(v):
        if v > date.today():
            raise ValueError("Invalid Birth date. Can not be in the past")
        return v
        
    @model_validator(mode="after")
    def validate_illness_range(self) -> Self:
        start_date = self.illness_start_date
        end_date = self.illness_end_date

        if start_date >= end_date:
            raise ValueError("Invalid illness range")
        return self
    def convert(self) -> dict:
        return {
            "id_num": self.id_num,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "address": self.address,
            "birth_date": self.birth_date.isoformat(),
            "phone": self.phone,
            "illness_start_date": self.illness_start_date.isoformat(),
            "illness_end_date": self.illness_end_date.isoformat()
        }
try:  
    member = Member(
        id_num="325746147",
        first_name="John",
        last_name="Doe",
        address="Rabbi",
        phone="0533134012",
        birth_date=date(1980, 1, 1),
        illness_start_date=date(2023, 1, 1),
        illness_end_date=date(2025, 12, 31)  # יגרום לשגיאה
    )

    print(member.convert())
except ValueError as e:
    print(e.errors()[0]["msg"])
