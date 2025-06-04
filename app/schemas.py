from pydantic import BaseModel, EmailStr
from typing import Optional

class BookingRequest(BaseModel):
    class_id: int
    client_name: str
    client_email: EmailStr

class BookingResponse(BookingRequest):
    booking_time: str

class ClassInfo(BaseModel):
    id: int
    name: str
    datetime: str
    instructor: str
    available_slots: int
