from fastapi import FastAPI, HTTPException, status
from otps import schema, crud
from utils import otputils
import uuid

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}


@app.post('/otp/send')
async def send_otp(
        request: schema.CreateOTP
):
    # check block OTP
    otp_block = crud.find_otp_block(request.recipient_id)
    if otp_block:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Sorry this phone number is blocked in 5 "
                                                                          "minutes")
    # generate and save to table
    otp_code = otputils.random(6)
    session_id = str(uuid.uuid1())
    print(crud.save_otp(request, session_id, otp_code))
    return 'OTP sent'


@app.post('/otp/verify')
async def send_verification():
    return 'verified OTP'
