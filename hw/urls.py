from django.conf.urls import url

from . import views

urlpatterns = [
	# 作业
    # url(r'^(?P<myMajor_id>\d+)/$', 'hw.views.hw_all_now', name='now_hws'),
    # url(r'^pass/(?P<myMajor_id>\d+)/$', 'hw.views.hw_all_pass', name='pass_hws'),
    url(r'^detail/(?P<pk>\d+)/$', 'hw.views.hw_detail', name='hw_detail'),
    url(r'^(?P<myMajor_id>\d+)/week/(?P<week>\d+)$', 'hw.views.hw_week', name='week_hws'),
    url(r'^(?P<myMajor_id>\d+)/latest$', 'hw.views.hw_newest', name='newest_hws'),
    url(r'^(?P<myMajor_id>\d+)/achieve$', 'hw.views.hw_achieve', name='achieve_hws'),

    # 课程
    url(r'^course/(?P<myMajor_id>\d+)/$', 'hw.views.course_all', name='course_all'),
    url(r'^course/detail/(?P<pk>\d+)/$', 'hw.views.course_detail', name='course_detail'),

    # 专业
    url(r'^major/(?P<mySchool_id>\d+)/$', 'hw.views.major_all', name='major_all'),
    url(r'^major/detail/(?P<pk>\d+)/$', 'hw.views.major_detail', name='major_detail'),

    # 学院
    url(r'^school/(?P<myCollege_id>\d+)/$', 'hw.views.school_all', name='school_all'),
    url(r'^school/detail/(?P<pk>\d+)/$', 'hw.views.school_detail', name='school_detail'),

    # 大学
    url(r'^colleges/$', 'hw.views.college_all', name='college_all'),
    url(r'^college/detail/(?P<pk>\d+)/$', 'hw.views.college_detail', name='college_detail'),

    url(r'^add_hw_zan/$', 'hw.views.add_hw_zan', name='add_hw_zan'),
    url(r'^add_ok_num/$', 'hw.views.add_ok_num', name='add_ok_num'),
    #url(r'^iFinished/$', 'hw.views.addOKNum', name='addOKNum'),

    # 网站其它的东西
    url(r'^giveSuggestion/$', 'hw.views.giveSuggestion', name='giveSuggestion'),
    url(r'^aboutMe/$', 'hw.views.aboutMe', name='aboutMe'),
    url(r'^test/$', 'hw.views.myTest', name='myTest'),
    url(r'^sub_email/$', 'hw.views.sub_email', name='sub_email'),
    url(r'^check_sub_email/$', 'hw.views.check_sub_email', name='check_sub_email'),
]
