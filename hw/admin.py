from django.contrib import admin
from .models import College, School, Course, Homework, Teacher, Major, ZAN, Suggestion, IP, ZanOnce, Sub_email

lst = [College, School, Course, Homework, Teacher, Major, ZAN, Suggestion, IP, ZanOnce, Sub_email]
for model in lst:
	admin.site.register(model)

