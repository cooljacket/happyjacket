# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import DjangoUeditor.models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='College',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='学校名称')),
                ('icon', models.ImageField(upload_to='hw/%Y/%m/%d', verbose_name='校徽')),
                ('introduction', DjangoUeditor.models.UEditorField(max_length=800, blank=True, verbose_name='大学介绍')),
            ],
            options={
                'verbose_name_plural': '大学',
            },
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='课程')),
                ('howToSubmit', DjangoUeditor.models.UEditorField(max_length=800, verbose_name='提交方式')),
                ('homepage', models.URLField(max_length=80, blank=True, verbose_name='课程主页')),
                ('grading', DjangoUeditor.models.UEditorField(max_length=800, default='暂时还不清楚', verbose_name='给分方法')),
            ],
            options={
                'verbose_name_plural': '课程',
            },
        ),
        migrations.CreateModel(
            name='Homework',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='作业名称')),
                ('deadline', models.DateTimeField(verbose_name='DDL')),
                ('week', models.SmallIntegerField(verbose_name='第几周')),
                ('description', DjangoUeditor.models.UEditorField(max_length=800, verbose_name='作业内容')),
                ('OK_num', models.SmallIntegerField(editable=False, default=0, verbose_name='完成人数')),
                ('memo', DjangoUeditor.models.UEditorField(max_length=800, blank=True, verbose_name='备注')),
                ('topIt', models.BooleanField(default=False, verbose_name='置顶')),
                ('myCourse', models.ForeignKey(to='hw.Course', verbose_name='所属课程')),
            ],
            options={
                'verbose_name_plural': '作业',
            },
        ),
        migrations.CreateModel(
            name='IP',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('ip', models.GenericIPAddressField()),
            ],
            options={
                'verbose_name_plural': 'IP',
            },
        ),
        migrations.CreateModel(
            name='Major',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='专业')),
                ('year', models.DecimalField(max_digits=4, decimal_places=0, verbose_name='年级')),
            ],
            options={
                'verbose_name_plural': '专业',
            },
        ),
        migrations.CreateModel(
            name='School',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='学院')),
                ('icon', models.ImageField(upload_to='hw/%Y/%m/%d', verbose_name='院徽')),
                ('intro', DjangoUeditor.models.UEditorField(max_length=800, blank=True, verbose_name='学院介绍')),
                ('myCollege', models.ForeignKey(to='hw.College', verbose_name='所属大学')),
            ],
            options={
                'verbose_name_plural': '学院',
            },
        ),
        migrations.CreateModel(
            name='Suggestion',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('name', models.CharField(max_length=50, editable=False, verbose_name='姓名')),
                ('email', models.EmailField(max_length=254, editable=False, verbose_name='邮箱')),
                ('suggestion', models.CharField(max_length=800, editable=False, verbose_name='反馈意见')),
            ],
            options={
                'verbose_name_plural': '反馈意见',
            },
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='姓名')),
                ('phoneNumber', models.CharField(max_length=11, blank=True, verbose_name='手机号码')),
                ('email', models.EmailField(max_length=35, blank=True, verbose_name='邮箱')),
                ('mySchool', models.ForeignKey(to='hw.School', verbose_name='所属学院')),
            ],
            options={
                'verbose_name_plural': '教师',
            },
        ),
        migrations.CreateModel(
            name='ZAN',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('num', models.PositiveIntegerField(default=0, verbose_name='赞')),
                ('name', models.CharField(max_length=50, verbose_name='为什么赞')),
            ],
            options={
                'verbose_name_plural': '赞',
            },
        ),
        migrations.CreateModel(
            name='ZanOnce',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('num', models.PositiveIntegerField(default=0, verbose_name='赞')),
                ('name', models.CharField(max_length=50, verbose_name='为什么赞')),
                ('IPs', models.ManyToManyField(editable=False, to='hw.IP', verbose_name='ip列表')),
            ],
            options={
                'verbose_name_plural': '只赞一次',
            },
        ),
        migrations.AddField(
            model_name='major',
            name='mySchool',
            field=models.ForeignKey(to='hw.School', verbose_name='所属学院'),
        ),
        migrations.AddField(
            model_name='course',
            name='mentor',
            field=models.ManyToManyField(max_length=50, to='hw.Teacher', verbose_name='老师'),
        ),
        migrations.AddField(
            model_name='course',
            name='myMajor',
            field=models.ForeignKey(to='hw.Major', verbose_name='所属专业'),
        ),
    ]
