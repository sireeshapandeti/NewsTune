# Generated by Django 2.2.2 on 2019-06-17 00:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20190616_2350'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='entertainment',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='customuser',
            name='politics',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='customuser',
            name='sports',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='customuser',
            name='world',
            field=models.BooleanField(default=False),
        ),
    ]
