# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hw', '0005_remove_sub_email_stage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sub_email',
            name='hour',
            field=models.PositiveIntegerField(verbose_name='时间'),
        ),
    ]
