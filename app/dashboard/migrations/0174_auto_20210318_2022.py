# Generated by Django 2.2.4 on 2021-03-18 20:22

import django.contrib.postgres.fields.jsonb
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0173_earning_success'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='ens_verification_address',
            field=models.CharField(blank=True, default='', max_length=255),
        ),
        migrations.AddField(
            model_name='profile',
            name='identity_data_facebook',
            field=django.contrib.postgres.fields.jsonb.JSONField(blank=True, default=dict, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='is_duniter_verified',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='profile',
            name='is_ens_verified',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='profile',
            name='is_facebook_verified',
            field=models.BooleanField(default=False),
        ),
    ]
