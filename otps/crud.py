from mongodb import db_instance
from otps import schema
from datetime import datetime

db = db_instance()


def find_otp_block(recipient_id: str):
    collection = db.otp_block_list
    result = collection.count_documents({"recipient_id": recipient_id}) > 0
    return result


def save_otp(request: schema.CreateOTP, session_id: str, otp_code: str):
    collection = db["otp_table"]
    return collection.insert_one(
        {"recipient_id": request.recipient_id, "session_id": session_id, otp_code: otp_code, "status": "sent",
         "created_on": datetime.now(), "updated_on": datetime.now(), "otp_failed_count": 0})
