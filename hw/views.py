# -*- coding: utf-8 -*-
from django.shortcuts import render, render_to_response
from django.http import HttpResponse
from django.core.urlresolvers import reverse
from django.db.models import Max
from django.db.models import Q
# from django.views.generic.base import TemplateView
import datetime, re

from hw.models import College, School, Major, Course, Homework, ZAN, Suggestion, Sub_email
from hw.utils.bread import getBreadUrls, ObjNum, hw_zan_name
from hw.utils import send_email
from hw.utils.settings import EMAIL_TO_WHON, DOMAIN_NAME

from django.utils.timezone import utc
from django.utils.timezone import localtime

def myTest(request):
	# week = Homework.objects.filter(myCourse_id=1).aggregate(Max('week'))
	# print(week)
	# return HttpResponse(week['week__max'])
	# return HttpResponse(reverse('hw:newest_hws', args=[1]))
	# return HttpResponse(localtime(datetime.datetime.utcnow().replace(tzinfo=utc)))
	return HttpResponse(get_sub_hws(1))

# Create your views here.
def index(request):
	title = 'testing'
	return render(request, 'hw/base.html', locals())


def aboutMe(request):
	'''介绍网站'''
	title = '本站介绍'
	return render(request, 'hw/about.html', locals())


def hw_detail(request, pk):
	'''作业详情'''
	title = '作业详情'
	
	try:
		hw = Homework.objects.get(id=pk)
	except Homework.DoesNotExist:
		return render(request, 'hw/404.html', {'err_msg': '并没有这个作业'})

	breadUrls = getBreadUrls(ObjNum.HW, pk)[0:-1]
	return render(request, 'hw/hw.html', locals())


def getLatestWeek(myMajor_id):
	try:
		major = str(Major.objects.get(id=myMajor_id))
	except Major.DoesNotExist:
		return None

	week = 1
	courses = Course.objects.filter(myMajor_id=myMajor_id)
	for c in courses:
		week = max(week, Homework.objects.filter(myCourse_id=c.id).aggregate(Max('week'))['week__max'])

	return week


def hw_newest(request, myMajor_id):
	week = getLatestWeek(myMajor_id)
	if week is None:
		return render(request, 'hw/404.html', {'err_msg': '并没有这个专业'})
	return hw_week(request, myMajor_id, week)


def hw_week(request, myMajor_id, week):
	try:
		major = str(Major.objects.get(id=myMajor_id))
	except Major.DoesNotExist:
		return render(request, 'hw/404.html', {'err_msg': '并没有这个专业'})

	# py 3.x only
	title = '第{0}周作业'.format(week) 
	now = datetime.datetime.now()
	courses = Course.objects.filter(myMajor_id=myMajor_id)
	breadUrls = getBreadUrls(ObjNum.MAJOR, myMajor_id)
	majorId = myMajor_id

	hws = []
	for c in courses:
		hws = hws + list(Homework.objects.filter(myCourse_id=c.id).filter(week=week).order_by('deadline'))

	for hw in hws:
		hw.myCourse.howToSubmit = hw.myCourse.howToSubmit.replace('\n', '<br>')
		hw.deadline = hw.deadline.strftime("%Y-%m-%d %H:%M %a")
	return render(request, 'hw/week_hw.html', locals())


def hw_achieve(request, myMajor_id):
	newest = getLatestWeek(myMajor_id)
	if newest is None:
		return render(request, 'hw/404.html', {'err_msg': '并没有这个专业'})

	breadUrls = getBreadUrls(ObjNum.MAJOR, myMajor_id)
	major = Major.objects.get(id=myMajor_id)
	majorName = str(major)

	# weeks = {}
	# for w in range(newest, 0, -1):
	# 	weeks[w] = reverse('hw:week_hws', args=(myMajor_id, w))
	class Tmp(object):
		def __init__(self):
			self.id = 0
			self.link = '233'

	weeks = []
	for w in range(newest, 0, -1):
		t = Tmp()
		t.id = w
		t.link = reverse('hw:week_hws', args=(myMajor_id, w))
		weeks.append(t)

	return render(request, 'hw/hw_achieve.html', locals())


# 根据major来展示该专业开设的所有课程
def course_all(request, myMajor_id):
	'''某专业开设的所有课程'''

	try:
		myMajor = str(Major.objects.get(id=myMajor_id))
	except Major.DoesNotExist:
		return render(request, 'hw/404.html', {'err_msg': '并没有这个专业'})

	title = '课程'
	courses = Course.objects.filter(myMajor_id=myMajor_id)
	breadUrls = getBreadUrls(ObjNum.MAJOR, myMajor_id)

	for c in courses:
		c.teachers = ', '.join([str(t.name) for t in c.mentor.all()])
		c.howToSubmit = c.howToSubmit.replace('\n', '<br>')
	return render(request, 'hw/courses.html', locals())


def course_detail(request, pk):
	'''课程详情'''
	title = '课程详情'

	try:
		course = Course.objects.get(id=pk)
	except Course.DoesNotExist:
		return render(request, 'hw/404.html', {'err_msg': '并没有这个课程'})

	breadUrls = getBreadUrls(ObjNum.COURSE, pk)[0:-1]
	
	if course is not None:
		course.teachers = ', '.join([str(t.name) for t in course.mentor.all()])
		course.howToSubmit = course.howToSubmit.replace('\n', '<br>')
		hws = Homework.objects.filter(myCourse_id=course.id).order_by('-deadline').values('name', 'id')
	return render(request, 'hw/course.html', locals())


def major_all(request, mySchool_id):
	'''某学院的所有专业'''
	title = '专业'

	try:
		mySchool = str(School.objects.get(id=mySchool_id))
	except School.DoesNotExist:
		return render(request, 'hw/404.html', {'err_msg': '并没有这个学院'})

	majors = Major.objects.filter(mySchool_id=mySchool_id)
	breadUrls = getBreadUrls(ObjNum.SCHOOL, mySchool_id)
	return render(request, 'hw/majors.html', locals())


def major_detail(request, pk):
	'''专业详情'''
	title = '专业'
	
	try:
		major = Major.objects.get(id=pk)
		majorName = str(major)
	except Major.DoesNotExist:
		return render(request, 'hw/404.html', {'err_msg': '并没有这个专业'})

	courseList = Course.objects.filter(myMajor_id=pk)
	breadUrls = getBreadUrls(ObjNum.MAJOR, pk)[0:-1]

	for c in courseList:
		c.teachers = ', '.join([str(t.name) for t in c.mentor.all()])
		c.howToSubmit = c.howToSubmit.replace('\n', '<br>')
	return render(request, 'hw/major.html', locals())


def school_all(request, myCollege_id):
	'''某大学的所有学院'''
	title = '学院'

	try:
		collegeName = str(College.objects.get(id=myCollege_id))
	except College.DoesNotExist:
		return render(request, 'hw/404.html', {'err_msg': '并没有这个课程'})

	schools = School.objects.filter(myCollege_id=myCollege_id)
	breadUrls = getBreadUrls(ObjNum.COLLEGE, myCollege_id)
	return render(request, 'hw/schools.html', locals())


def school_detail(request, pk):
	'''某大学的所有学院'''
	title = '学院详情'
	
	try:
		school = School.objects.get(id=pk)
	except School.DoesNotExist:
		return render(request, 'hw/404.html', {'err_msg': '并没有这个学院'})

	majors = Major.objects.filter(mySchool_id=school.id)
	breadUrls = getBreadUrls(ObjNum.SCHOOL, pk)[0:-1]
	return render(request, 'hw/school.html', locals())


def college_all(request):
	'''所有大学'''
	title = '大学'
	colleges = College.objects.all()
	return render(request, 'hw/colleges.html', locals())


def college_detail(request, pk):
	'''大学详情'''
	title = '大学详情'
	
	try:
		college = College.objects.get(id=pk)
	except College.DoesNotExist:
		return render(request, 'hw/404.html', {'err_msg': '并没有这个大学'})

	if college:
		schools = School.objects.filter(myCollege_id=college.id) 
	return render(request, 'hw/college.html', locals())


def add_hw_zan(request):
	"""给所有关于hw这个app的页面点赞"""
	hw_zan = ZAN.objects.get(name=hw_zan_name)
	hw_zan.num = hw_zan.num + 1
	hw_zan.save()
	return HttpResponse('(' + str(hw_zan.num) + ')')


def add_ok_num(request):
	"""我完成了，Homework中的OK_num自增1"""
	hid = request.GET.get('hid')
	try:
		hw = Homework.objects.get(id=hid)
	except Homework.DoesNotExist:
		return render(request, 'hw/404.html', {'err_msg': '并没有这个作业'})

	hw.OK_num = hw.OK_num + 1
	hw.save()
	return HttpResponse(str(hw.OK_num))


# 使用POST更安全，因为有django提供的csrf验证
def giveSuggestion(request):
	name = request.POST.get('name', 'nobody')
	email = request.POST.get('email', '233@666.com')
	suggestion = request.POST.get('suggestion', None)

	if suggestion:
		sug = Suggestion(name=name, email=email, suggestion=suggestion)
		sug.save()
		content = '{0}({1})给你提了反馈意见：\n{2}'.format(name, email, suggestion)
		send_email.send_email(EMAIL_TO_WHON, '反馈意见', content)
		return HttpResponse('谢谢你的反馈意见')

	return HttpResponse('反馈意见为空或传输数据出了故障，请稍后再试')


def sub_email(request):
	name = request.POST.get('name', 'nobody')
	email = request.POST.get('email', None)
	whichDay = request.POST.get('whichDay', None)
	hour = request.POST.get('hour', None)
	stage = request.POST.get('stage', None)
	majorId = request.POST.get('major', None)
	if email is '' or majorId is None or whichDay is None or hour is None or stage is None:
		return HttpResponse('订阅失败，请补充好订阅的信息')

	try:
		major = str(Major.objects.get(id=majorId))
	except Major.DoesNotExist:
		return HttpResponse('订阅失败，请补充好订阅的信息')

	hour = int(hour) + 12 * int(stage)
	sub_email = Sub_email(name=name, email=email, major_id=majorId, whichDay=whichDay, hour=hour)
	sub_email.save()

	which_days = ['周日', '周一', '周二', '周三', '周四', '周五', '周六', '天']
	which_stage = ['上午', '下午']
	msg = '订阅成功，您订阅了{major}专业的作业提醒邮件，时间为：每{day}{stage}的{hour}点(温馨提示：可以多次订阅不同时间段)'.format(
		major=major, day=which_days[int(whichDay)], stage=which_stage[int(stage)], hour=hour
	)
	return HttpResponse(msg)


from django.utils.timezone import utc
from django.utils.timezone import localtime


def get_sub_hws(majorId):
	week = getLatestWeek(majorId)
	courses = Course.objects.filter(myMajor_id=majorId)
	msg = '本周（截止到今天）作业简报，详情见：{0}\n'.format(DOMAIN_NAME+reverse('hw:newest_hws', args=[majorId]))

	cnt = 0
	for c in courses:
		hws = list(Homework.objects.filter(myCourse_id=c.id).filter(week=week).order_by('deadline'))
		howToSubmit = re.sub(r'</?\w+[^>]*>', ' ', c.howToSubmit.replace('<br>', '\n'))
		for hw in hws:
			content = re.sub(r'</?\w+[^>]*>', ' ', hw.description.replace('<br>', '\n'))
			msg += '{0}，DDL是：{1}\n内容是：{2}\n提交方式为：{3}\n\n\n'.format(str(hw), hw.deadline.strftime("%Y-%m-%d %H:%M %a"), content, howToSubmit)
	
	print(msg)

	return msg


def do_check_sub_email():
	everyday = 7
	now = localtime(datetime.datetime.utcnow().replace(tzinfo=utc))
	hour = now.hour
	today = now.weekday()
	subs = Sub_email.objects.filter(Q(whichDay=today) | Q(whichDay=everyday)).filter(hour=hour)

	for s in subs:
		try:
			msg = get_sub_hws(s.major_id)
			send_email.send_email([s.email], '作业LA本周作业订阅', msg)
			print('good', msg)
		except Exception:
			print('bad', s.email, msg)

def check_sub_email(request):
	key = request.GET.get('key', None)
	if key == '23345fafaafjadljkffalwofal;/.afan.nq==+)+0=':
		do_check_sub_email()
		return HttpResponse('come on!')

	return HttpResponse('hehehe')
