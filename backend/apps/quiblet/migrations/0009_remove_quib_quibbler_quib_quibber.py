# Generated by Django 5.1.3 on 2024-12-04 06:39

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiblet', '0008_alter_quib_slug'),
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='quib',
            name='quibbler',
        ),
        migrations.AddField(
            model_name='quib',
            name='quibber',
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name='quibs',
                to='user.profile',
                verbose_name='quibber',
            ),
        ),
    ]