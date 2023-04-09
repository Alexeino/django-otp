import random
from django.contrib.auth import get_user_model

User = get_user_model()

def otp_generator():
    otp = random.randint(111111,999999)
    return otp

def otp_manager(phone_number):
    try:
        user = User.objects.get(phone_number=phone_number)
        otp = otp_generator()
        user.otp = otp
        user.save()
        
        # TODO: Send OTP to Mobile using any 3rd party provider like Msg91, twilio etc.
        return otp
    
    except User.DoesNotExist:
        return None