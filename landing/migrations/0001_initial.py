# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-03-12 12:17
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=256)),
            ],
            options={
                'verbose_name': 'Company',
                'verbose_name_plural': 'Companies',
                'ordering': ['-created'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=256)),
            ],
            options={
                'verbose_name': 'Country',
                'verbose_name_plural': 'Countries',
                'ordering': ['-created'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Services',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=256)),
                ('image', models.ImageField(blank=True, null=True, upload_to='images')),
                ('description', models.TextField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'Service',
                'verbose_name_plural': 'Services',
                'ordering': ['-created'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Specialization',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=256)),
            ],
            options={
                'verbose_name': 'Specialization',
                'verbose_name_plural': 'Specializations',
                'ordering': ['-created'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Vacancy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=256)),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='landing.Company')),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='landing.Country')),
                ('specialization', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='landing.Specialization')),
            ],
            options={
                'verbose_name': 'Vacancy',
                'verbose_name_plural': 'Vacancy',
                'ordering': ['-created'],
                'abstract': False,
            },
        ),
    ]
