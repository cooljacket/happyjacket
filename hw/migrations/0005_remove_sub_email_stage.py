# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hw', '0004_sub_email_major_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sub_email',
            name='stage',
        ),
    ]
