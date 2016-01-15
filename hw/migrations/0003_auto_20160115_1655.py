# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hw', '0002_sub_email'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sub_email',
            name='kind',
        ),
        migrations.AddField(
            model_name='sub_email',
            name='hour',
            field=models.SmallIntegerField(verbose_name='时间', default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='sub_email',
            name='stage',
            field=models.SmallIntegerField(verbose_name='上下午', default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='sub_email',
            name='whichDay',
            field=models.SmallIntegerField(verbose_name='第几天', default=1),
            preserve_default=False,
        ),
    ]
