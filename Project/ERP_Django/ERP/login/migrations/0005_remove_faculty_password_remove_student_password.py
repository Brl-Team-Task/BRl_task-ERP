# Generated by Django 4.2.7 on 2023-11-22 20:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0004_alter_faculty_password_alter_student_password'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='faculty',
            name='password',
        ),
        migrations.RemoveField(
            model_name='student',
            name='password',
        ),
    ]
