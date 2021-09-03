from rest_framework import serializers
from TestApp.models import Course,CodingQuestions,MultipleChoiceQuestions

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'

class CodingQuestionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = CodingQuestions
        fields = '__all__'

class MultipleChoiceQuestionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = MultipleChoiceQuestions
        fields = '__all__'
