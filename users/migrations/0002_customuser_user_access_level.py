# Generated by Django 3.1.7 on 2021-03-09 16:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='user_access_level',
            field=models.CharField(choices=[('ADMIN', 'Admin'), ('TEACHER', 'Teacher'), ('STUDENT', 'Student')], default='STUDENT', max_length=40),
        ),
    ]
