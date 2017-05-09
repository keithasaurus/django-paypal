# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ipn', '0007_auto_20160219_1135'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paypalipn',
            name='transaction_subject',
            field=models.CharField(max_length=1024, blank=True),
        ),
    ]
