from rest_framework import serializers
from django.contrib.auth import get_user_model


User=get_user_model()

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id','phone_number','username','password']
        extra_kwargs = {
            'id':{'read_only':True},
            'phone_number':{'required':True},
            'username':{'required':True},
            'password':{'required':True},
        }
        
    def create(self, validated_data):
        return User.objects.create(**validated_data)
    
