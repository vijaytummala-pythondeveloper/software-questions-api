from rest_framework.generics import CreateAPIView,ListAPIView
from Student.serializers import *
from Student.models import *

# Create your views here.
class StudentCreateView(CreateAPIView):
    serializer_class = StudentSerializer
