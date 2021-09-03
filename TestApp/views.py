from django.shortcuts import render

# Create your views here.
from rest_framework.generics import CreateAPIView,ListAPIView
from .serializers import *
from TestApp.models import *

class CourseListView(ListAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer


class CourseCreateView(CreateAPIView):
    serializer_class = CourseSerializer

class CodingQuestionsCreateView(CreateAPIView):
    serializer_class = CodingQuestionsSerializer

class MultipleChoiceQuestionsCreateView(CreateAPIView):
    serializer_class = MultipleChoiceQuestionsSerializer
