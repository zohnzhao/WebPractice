# Generated by Django 2.1.5 on 2019-01-06 08:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Schooldetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('logo', models.CharField(blank=True, max_length=255, null=True)),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
                ('tag1', models.CharField(blank=True, max_length=255, null=True)),
                ('tag2', models.CharField(blank=True, max_length=255, null=True)),
                ('tag3', models.CharField(blank=True, max_length=255, null=True)),
                ('tag4', models.CharField(blank=True, max_length=255, null=True)),
                ('level', models.CharField(blank=True, max_length=255, null=True)),
                ('area', models.CharField(blank=True, max_length=255, null=True)),
                ('type', models.CharField(blank=True, max_length=255, null=True)),
                ('telephone', models.CharField(blank=True, max_length=255, null=True)),
                ('weburl', models.CharField(blank=True, max_length=255, null=True)),
                ('introduce', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'schooldetails',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Schoolscore',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('schoolname', models.CharField(blank=True, max_length=255, null=True)),
                ('province', models.CharField(blank=True, max_length=255, null=True)),
                ('pici', models.CharField(blank=True, max_length=255, null=True)),
                ('ambit', models.CharField(blank=True, max_length=255, null=True)),
                ('year', models.CharField(blank=True, max_length=255, null=True)),
                ('average', models.CharField(blank=True, max_length=255, null=True)),
                ('maxscore', models.CharField(blank=True, max_length=255, null=True)),
                ('minscore', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'db_table': 'schoolscore',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Specialtydetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('schoolname', models.CharField(blank=True, max_length=255, null=True)),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
                ('level', models.CharField(blank=True, max_length=255, null=True)),
                ('introduce', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'specialtydetails',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Specialtyscore',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('schoolname', models.CharField(blank=True, max_length=255, null=True)),
                ('province', models.CharField(blank=True, max_length=255, null=True)),
                ('ambit', models.CharField(blank=True, max_length=255, null=True)),
                ('year', models.CharField(blank=True, max_length=255, null=True)),
                ('specialtyname', models.CharField(blank=True, max_length=255, null=True)),
                ('average', models.CharField(blank=True, max_length=255, null=True)),
                ('maxscore', models.CharField(blank=True, max_length=255, null=True)),
                ('minscore', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'db_table': 'specialtyscore',
                'managed': False,
            },
        ),
    ]