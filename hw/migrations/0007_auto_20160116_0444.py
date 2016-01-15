# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hw', '0006_auto_20160116_0438'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sub_email',
            name='hour',
            field=models.SmallIntegerField(verbose_name='时间'),
        ),
    ]
