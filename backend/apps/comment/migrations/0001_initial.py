# Generated by Django 5.1.4 on 2025-01-17 09:06

import django_ltree.fields
from django.contrib.postgres.operations import CreateExtension
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        CreateExtension('ltree'),
        migrations.CreateModel(
            name='Comment',
            fields=[
                (
                    'id',
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name='ID',
                    ),
                ),
                ('path', django_ltree.fields.PathField(unique=True)),
                (
                    'created_at',
                    models.DateTimeField(auto_now_add=True, verbose_name='create at'),
                ),
                ('content', models.TextField(verbose_name='content')),
                ('deleted', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': 'Comment',
                'verbose_name_plural': 'Comments',
            },
        ),
    ]
