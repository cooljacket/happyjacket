# -*- coding: utf-8 -*-
from django.db import models
from DjangoUeditor.models import UEditorField
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User  


name_len = 50
icon_len = 30
longText = 800
ImageUrl = 'hw/%Y/%m/%d'

# Create your models here.
class College(models.Model):
	"""College"""
	# name = models.CharField(primary_key=True, verbose_name='学校名称', max_length=name_len)
	name = models.CharField(verbose_name='学校名称', max_length=name_len)
	icon = models.ImageField(verbose_name='校徽', upload_to=ImageUrl)
	introduction = UEditorField(verbose_name='大学介绍', max_length=longText, blank=True, height=300, width='100%', toolbars='besttome')

	def __str__(self):
		return str(self.name)

	class Meta:
		verbose_name_plural = '大学'


class School(models.Model):
	"""School"""
	myCollege = models.ForeignKey(College, verbose_name='所属大学')
	name = models.CharField(verbose_name='学院', max_length=name_len)
	icon = models.ImageField(verbose_name='院徽', upload_to=ImageUrl)
	intro = UEditorField(verbose_name='学院介绍', max_length=longText, blank=True, height=300, width='100%', toolbars='besttome')

	def __str__(self):
		return str(self.name)

	class Meta:
		verbose_name_plural = '学院'


class Major(models.Model):
	"""Major"""
	mySchool = models.ForeignKey(School, verbose_name='所属学院')
	name = models.CharField(verbose_name='专业', max_length=name_len)
	year = models.DecimalField(verbose_name='年级', max_digits=4, decimal_places=0)

	def __str__(self):
		return str(self.name) + '(' + str(self.year) + ')'

	class Meta:
		verbose_name_plural = '专业'


class Teacher(models.Model):
	"""Teacher"""
	mySchool = models.ForeignKey(School, verbose_name='所属学院')
	name = models.CharField(verbose_name='姓名', max_length=name_len)
	phoneNumber = models.CharField(verbose_name='手机号码', max_length=11, blank=True)
	email = models.EmailField(verbose_name='邮箱', max_length=35, blank=True)

	def __str__(self):
		return str(self.name)

	class Meta:
		verbose_name_plural = '教师'


# class Student(models.Model):
# 	"""Student"""
# 	mySchool = models.ForeignKey(Major, verbose_name='所属学院')
# 	user = models.OneToOneField(User, unique=True, verbose_name='我的id')
# 	name = models.CharField(verbose_name='真实姓名', max_length=name_len)
# 	email = models.EmailField(verbose_name='邮箱', max_length=35, blank=True)


class Course(models.Model):
	"""Course"""
	myMajor = models.ForeignKey(Major, verbose_name='所属专业')
	mentor = models.ManyToManyField(Teacher, verbose_name='老师', max_length=name_len)
	name = models.CharField(verbose_name='课程', max_length=name_len)
	howToSubmit = UEditorField(verbose_name='提交方式', max_length=longText, height=300, width='100%', toolbars='besttome')
	homepage = models.URLField(verbose_name='课程主页', max_length=80, blank=True)
	grading = UEditorField(verbose_name='给分方法', max_length=longText, height=300, width='100%', toolbars='besttome', default='暂时还不清楚')

	def __str__(self):
		return str(self.name)

	class Meta:
		verbose_name_plural = '课程'


class Homework(models.Model):
	"""Homework"""
	myCourse = models.ForeignKey(Course, verbose_name='所属课程')
	name = models.CharField(verbose_name='作业名称', max_length=name_len)
	deadline = models.DateTimeField('DDL')
	week = models.SmallIntegerField(verbose_name='第几周')
	description = UEditorField(verbose_name='作业内容', max_length=longText, height=300, width='100%', toolbars='besttome')
	OK_num = models.SmallIntegerField(verbose_name='完成人数', default=0, editable=False)
	memo = UEditorField(verbose_name='备注', max_length=longText, height=300, width='100%', toolbars='besttome', blank=True)
	topIt = models.BooleanField(verbose_name='置顶', default=False)

	def __str__(self):
		return str(self.name) + '(' + str(self.myCourse.name) + ')'

	class Meta:
		verbose_name_plural = '作业'


class Suggestion(models.Model):
	"""Suggestion for this app"""
	name = models.CharField(verbose_name='姓名', max_length=name_len, editable=False)
	email = models.EmailField(verbose_name='邮箱', editable=False)
	suggestion = models.CharField(verbose_name='反馈意见', max_length=longText, editable=False)

	def __str__(self):
		return str(self.name+self.email+self.suggestion)

	class Meta:
		verbose_name_plural = '反馈意见'


class ZAN(models.Model):
	"""Collecting zan from the website viewers"""
	num = models.PositiveIntegerField('赞', default=0)
	name = models.CharField(verbose_name='为什么赞', max_length=name_len)
	
	def get_zan_num(name):
		return ZAN.objects.get(name=name).num

	def __str__(self):
		return str(self.name)

	class Meta:
		verbose_name_plural = '赞'


# 要规定它不能被编辑，或者对于后台是隐藏的
class IP(models.Model):
	"""Recording the zan IP"""
	ip = models.GenericIPAddressField()

	class Meta:
		verbose_name_plural = 'IP'


class ZanOnce(models.Model):
	"""Allow zan only at most once"""
	num = models.PositiveIntegerField(verbose_name='赞', default=0)
	name = models.CharField(verbose_name='为什么赞', max_length=name_len)
	IPs = models.ManyToManyField(IP, verbose_name='ip列表', editable=False)
	
	def get_zan_num(name, ip):
		return ZAN.objects.get(name=name).num

	def __str__(self):
		return str(self.name)

	class Meta:
		verbose_name_plural = '只赞一次'

