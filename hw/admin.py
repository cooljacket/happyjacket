from django.contrib import admin
from .models import College, School, Course, Homework, Teacher, Major, ZAN, Suggestion, IP, ZanOnce

lst = [College, School, Course, Homework, Teacher, Major, ZAN, Suggestion, IP, ZanOnce]
for model in lst:
	admin.site.register(model)

