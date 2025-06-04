from datetime import datetime
import pytz
from app.models import classes

def convert_to_timezone(class_data, tz):
    ist = pytz.timezone("Asia/Kolkata")
    target_tz = pytz.timezone(tz)
    dt = ist.localize(datetime.fromisoformat(class_data["datetime"]))
    converted_dt = dt.astimezone(target_tz)
    return {
        **class_data,
        "datetime": converted_dt.isoformat()
    }

def find_class_by_id(class_id):
    return next((c for c in classes if c["id"] == class_id), None)
