# Generated by Django 2.2.4 on 2021-03-17 02:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0172_auto_20210216_0820'),
    ]

    operations = [
        migrations.AddField(
            model_name='earning',
            name='success',
            field=models.BooleanField(default=False, help_text='Was txn successful?'),
        ),
    ]
