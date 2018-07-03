# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-06-25 11:48
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('lernen', '0002_auto_20180616_1919'),
    ]

    operations = [
        migrations.CreateModel(
            name='ArtikelImages',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imgname', models.CharField(max_length=30)),
                ('order', models.PositiveIntegerField()),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lernen.Artikel')),
            ],
            options={
                'ordering': ['order'],
            },
        ),
    ]