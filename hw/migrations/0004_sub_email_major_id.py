# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hw', '0003_auto_20160115_1655'),
    ]

    operations = [
        migrations.AddField(
            model_name='sub_email',
            name='major_id',
            field=models.PositiveIntegerField(verbose_name='专业id', default=1),
            preserve_default=False,
        ),
    ]
