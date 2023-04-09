from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from accounts.api.serializers import UserSerializer
from django.contrib.auth import get_user_model
from .helper import otp_manager
from rest_framework.authtoken.models import Token
from rest_framework.permissions import AllowAny

# Create your views here.

User = get_user_model()

class RegisterAV(APIView):
    permission_classes  = [AllowAny,]
    def post(self,request,*args,**kwargs):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            
            otp_manager(serializer.data.get('phone_number'))
            
            return Response({
                "msg":"OTP Sent Succesfully...",
                "user":serializer.data
            })
        else:
            return Response(serializer.errors)

class ValidateOTPAV(APIView):
    permission_classes  = [AllowAny,]
    
    def post(self,request,*args, **kwargs):
        try:
            phone_number = request.data.get('phone_number')
            otp = request.data.get('otp')
            print(phone_number,otp)
            
            if phone_number and otp:
                user = User.objects.get(phone_number__iexact=phone_number)
                if user.otp == otp:
                    user.is_phone_verified = True
                    user.save()
                    
                    return Response({
                        "success":"Phone number verified",
                        "user": user.phone_number,
                        "token":self.send_auth_token(user=user)
                    })
        except User.DoesNotExist:
            return Response({
                "error":"User with this Phone number does not exists..."
            })
            
    def send_auth_token(self,user):
        token = Token.objects.get_or_create(user=user)
        return token[0].key