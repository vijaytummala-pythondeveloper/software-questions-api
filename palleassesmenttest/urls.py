"""palleassesmenttest URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from TestApp.views import *
from Student.views import *

urlpatterns = [
    path('course-create/', CourseCreateView.as_view(), name='course_create'),
    path('coding-questions-create/', CodingQuestionsCreateView.as_view(), name='coding-questions-create'),
    path('multiple-choices-questions-create/', MultipleChoiceQuestionsCreateView.as_view(), name='multiple-choices-questions-create'),
    path('course-list/', CourseListView.as_view(), name='course-list'),
    path('student-create/', StudentCreateView.as_view(), name='student_create'),
    path('student-list/', StudentListView.as_view(), name='student-list'),
    path('admin/', admin.site.urls),

]