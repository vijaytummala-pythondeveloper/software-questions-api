from rest_framework import serializers
from Student.models import Student
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email')

class StudentSerializer(serializers.ModelSerializer):
    student = UserSerializer(required=True)
    class Meta:
        model = Student
        fields = '__all__'