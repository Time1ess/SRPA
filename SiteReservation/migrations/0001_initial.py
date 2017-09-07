# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-09-07 11:59
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('const', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uid', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('status', models.IntegerField(choices=[(0, '预约已提交'), (1, '预约已取消'), (2, '预约已批准'), (3, '预约修改中'), (4, '预约已终止'), (5, '预约已确认'), (6, '预约已完成')], default=0, verbose_name='状态')),
                ('title', models.CharField(max_length=100, verbose_name='活动内容')),
                ('activity_time_from', models.DateTimeField(verbose_name='活动开始时间')),
                ('activity_time_to', models.DateTimeField(verbose_name='活动结束时间')),
                ('reserve_from', models.DateTimeField(verbose_name='预约开始时间')),
                ('reserve_to', models.DateTimeField(verbose_name='预约结束时间')),
                ('comment', models.TextField(verbose_name='备注')),
                ('site', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='const.Site', verbose_name='场地')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='预约人')),
                ('workshop', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='const.Workshop', verbose_name='工坊')),
            ],
            options={
                'verbose_name': '活动场地预约',
                'verbose_name_plural': '活动场地预约',
            },
        ),
    ]
