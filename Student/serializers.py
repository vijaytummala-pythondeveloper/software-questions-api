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

    def create(self, validated_data):
        """
        Overriding the default create method of the Model serializer.
        :param validated_data: data containing all the details of student
        :return: returns a successfully created student record
        """
        user_data = validated_data.pop('student')
        user = UserSerializer.create(UserSerializer(), validated_data=user_data)
        student, created = Student.objects.update_or_create(student=user,
                                                            student_identification=validated_data.pop('student_identification'),
                                                            student_pic=validated_data.pop('student_pic'),
                                                            student_course=validated_data.pop(
                                                                'student_course'),
                                                            )
        return student