# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hw', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sub_email',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('name', models.CharField(verbose_name='称呼', max_length=50)),
                ('email', models.EmailField(verbose_name='邮箱', max_length=35)),
                ('kind', models.SmallIntegerField(verbose_name='时间段')),
            ],
        ),
    ]
