# Generated by Django 2.2.2 on 2019-06-16 23:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customuser',
            old_name='bio',
            new_name='categories',
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='birth_date',
        ),
    ]
