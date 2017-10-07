# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-10-07 07:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ProjectApproval', '0007_auto_20171004_1551'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='activity_range',
            field=models.IntegerField(choices=[(0, 'Within Workshop'), (1, 'Whole School')], default=0, verbose_name='Project Participant'),
        ),
        migrations.AlterField(
            model_name='project',
            name='status',
            field=models.IntegerField(choices=[(0, 'Project Submitted'), (1, 'Project Cancelled'), (2, 'Project Approved'), (3, 'Project Editting'), (4, 'Project Terminated'), (5, 'Project End Submitted'), (6, 'Project End Editting'), (7, 'Project Finished'), (8, 'Project Completed'), (9, 'Additional Info Required')], default=0, verbose_name='Project Status'),
        ),
    ]