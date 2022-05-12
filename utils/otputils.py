import pyotp

totp = pyotp.TOTP('base32secret3232', interval=30)


def get_otp():
    return totp.now()


def verify_otp(received_otp):
    print("received otp: " + received_otp)
    print("verification: " + str(totp.verify(received_otp)))
    return totp.verify(received_otp)
