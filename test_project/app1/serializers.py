from rest_framework import serializers
#from app1.models import User
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
	class Meta:
		model = User
		fields = '__all__'