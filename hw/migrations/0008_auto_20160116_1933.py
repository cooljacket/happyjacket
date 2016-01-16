# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hw', '0007_auto_20160116_0444'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='sub_email',
            options={'verbose_name_plural': '作业订阅'},
        ),
    ]
