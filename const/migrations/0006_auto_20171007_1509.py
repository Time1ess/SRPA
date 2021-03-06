# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-10-07 07:09
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0008_alter_user_username_max_length'),
        ('const', '0005_feedback_created'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='feedback',
            options={'verbose_name': 'Audit Feedback', 'verbose_name_plural': 'Audit Feedback'},
        ),
        migrations.AlterModelOptions(
            name='site',
            options={'default_permissions': ('add', 'delete', 'update', 'view'), 'verbose_name': 'Site', 'verbose_name_plural': 'Site'},
        ),
        migrations.AlterModelOptions(
            name='workshop',
            options={'default_permissions': ('add', 'delete', 'update', 'view'), 'verbose_name': 'Workshop', 'verbose_name_plural': 'Workshop'},
        ),
        migrations.AddField(
            model_name='workshop',
            name='group',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='auth.Group', verbose_name='Group'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='feedback',
            name='created',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Audit Time'),
        ),
        migrations.AlterField(
            model_name='feedback',
            name='desc',
            field=models.TextField(verbose_name='Audit Opinion'),
        ),
        migrations.AlterField(
            model_name='feedback',
            name='target_uid',
            field=models.UUIDField(verbose_name='Audited Target'),
        ),
        migrations.AlterField(
            model_name='feedback',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Auditor'),
        ),
        migrations.AlterField(
            model_name='site',
            name='desc',
            field=models.CharField(max_length=50, verbose_name='Site Description'),
        ),
        migrations.AlterField(
            model_name='workshop',
            name='desc',
            field=models.CharField(max_length=50, verbose_name='Workshop Description'),
        ),
        migrations.AlterField(
            model_name='workshop',
            name='instructor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='authentication.TeacherInfo', verbose_name='Instructor'),
        ),
    ]
