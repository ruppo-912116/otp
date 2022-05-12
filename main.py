from fastapi import FastAPI, HTTPException, status
from otps import schema, crud
from utils import otputils, smtputils
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
    otp_code = otputils.get_otp()
    session_id = str(uuid.uuid1())
    crud.save_otp(request, session_id, otp_code)

    # after generation, send to the receiver
    smtputils.send_otp(otp_code)

    return otp_code


@app.post('/otp/verify')
async def send_verification(
        request: schema.VerifyOTP
):
    # check the validity of OTP
    is_verified = otputils.verify_otp(request.otp_code)

    # if OTP is verified, we save the user to a collection
    return is_verified
