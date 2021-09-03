from django.db import models


# Create your models here.
class Course(models.Model):
    course_name = models.CharField(max_length=100, blank=False, null=False, unique=True)

    def __str__(self):
        return self.course_name

class CodingQuestions(models.Model):
    course = models.ForeignKey(Course,on_delete=models.CASCADE)
    question = models.TextField(blank=False,null=False)
    answer = models.TextField(blank=False,null=False)
    def __str__(self):
        return self.question

class MultipleChoiceQuestions(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    question = models.TextField(blank=False, null=False)
    correct_answer = models.CharField(max_length=500,blank=False, null=False)
    answer_1 = models.CharField(max_length=500, blank=False, null=False)
    answer_2 = models.CharField(max_length=500, blank=False, null=False)
    answer_3 = models.CharField(max_length=500, blank=False, null=False)
    answer_4 = models.CharField(max_length=500, blank=False, null=False)
    def __str__(self):
        return self.question

