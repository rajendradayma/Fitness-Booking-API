from fastapi import FastAPI, HTTPException, Query
from pydantic import BaseModel, EmailStr
from datetime import datetime
from typing import List, Optional
import pytz
from app.models import classes, bookings
from app.schemas import BookingRequest, BookingResponse, ClassInfo
from app.utils import convert_to_timezone, find_class_by_id
app = FastAPI(title="Fitness Booking API")

@app.get("/classes", response_model=List[ClassInfo])
def get_classes(tz: Optional[str] = Query("Asia/Kolkata")):
    return [convert_to_timezone(cls, tz) for cls in classes]

@app.post("/book", response_model=BookingResponse)
def book_class(payload: BookingRequest):
    fitness_class = find_class_by_id(payload.class_id)
    if not fitness_class:
        raise HTTPException(status_code=404, detail="Class not found")
    if fitness_class["available_slots"] <= 0:
        raise HTTPException(status_code=400, detail="No available slots")
    booking = {
        "class_id": payload.class_id,
        "client_name": payload.client_name,
        "client_email": payload.client_email,
        "booking_time": datetime.now().isoformat()
    }
    bookings.append(booking)
    fitness_class["available_slots"] -= 1
    return booking

@app.get("/bookings", response_model=List[BookingResponse])
def get_bookings(email: EmailStr):
    return [b for b in bookings if b["client_email"] == email]
@app.get("/")
def read_root():
    return {"message": "Welcome to the Fitness Booking API. Visit /docs for Swagger UI."}


