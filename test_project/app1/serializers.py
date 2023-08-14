from rest_framework import serializers
from app1.models import CustomUser
#from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
	class Meta:
		model = CustomUser
		fields = '__all__'