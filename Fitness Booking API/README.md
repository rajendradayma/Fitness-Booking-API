# Fitness Booking API

A simple RESTful API built with FastAPI to manage fitness class bookings at a fictional fitness studio. Users can view available classes, book a spot, and retrieve their bookings.

---

## Features

- View upcoming fitness classes with timezone support
- Book classes with slot availability validation
- Retrieve bookings by client email
- Input validation and error handling
- In-memory data storage (no external DB needed)
- Includes unit tests

---

## Tech Stack

- Python 3.8+
- FastAPI
- Pydantic
- Uvicorn
- Pytest
- pytz (for timezone conversions)

---

## Setup Instructions

1. Clone the repository:

```bash
git clone https://github.com/your-username/fitness-booking-api.git
cd fitness-booking-api

2. Create and activate a virtual environment:
python -m venv .venv
# Windows
.\.venv\Scripts\activate

3. Install dependencies:
pip install -r requirements.txt

4. Run the API server:
uvicorn app.main:app --reload

The server will start at http://127.0.0.1:8000

How to Test the API
Using Swagger UI (Recommended)
Open your browser and navigate to:

http://127.0.0.1:8000/docs

This interactive documentation allows you to:

View the list of classes (GET /classes)

Book a class (POST /book) by filling the JSON form

Get all bookings for an email (GET /bookings)
```
Running Tests
Run unit tests with:

pytest app/test_main.py



