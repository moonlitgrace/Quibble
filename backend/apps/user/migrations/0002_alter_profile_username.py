# Generated by Django 5.1.4 on 2024-12-11 15:44

from django.db import migrations, models

import apps.user.validators


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='username',
            field=models.CharField(
                max_length=25,
                unique=True,
                validators=[apps.user.validators.UsernameValidator()],
                verbose_name='username',
            ),
        ),
    ]
