from django.contrib.auth.models import User
from django.db import models
from TestApp.models import Course

# Create your models here.

class Student(models.Model):
    student = models.ForeignKey(User,on_delete=models.CASCADE)
    student_identification = models.CharField(max_length=10)
    student_pic = models.ImageField(upload_to='static/images/studentimages')
    student_course = models.ForeignKey(Course,on_delete=models.CASCADE)
    def __str__(self):
        return str(self.student)
