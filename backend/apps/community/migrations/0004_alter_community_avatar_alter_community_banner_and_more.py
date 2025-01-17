# Generated by Django 5.1.4 on 2025-01-17 11:45

import dynamic_filenames
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('community', '0003_remove_community_rangers_community_moderators_and_more'),
        ('user', '0002_alter_profile_avatar_alter_profile_created_at_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='community',
            name='avatar',
            field=models.ImageField(
                blank=True,
                null=True,
                upload_to=dynamic_filenames.FilePattern(
                    filename_pattern='avatar/{uuid:s}{ext}'
                ),
                verbose_name='Avatar',
            ),
        ),
        migrations.AlterField(
            model_name='community',
            name='banner',
            field=models.ImageField(
                blank=True,
                null=True,
                upload_to=dynamic_filenames.FilePattern(
                    filename_pattern='community_banner/{uuid:s}{ext}'
                ),
                verbose_name='Banner',
            ),
        ),
        migrations.AlterField(
            model_name='community',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Create at'),
        ),
        migrations.AlterField(
            model_name='community',
            name='description',
            field=models.TextField(verbose_name='Description'),
        ),
        migrations.AlterField(
            model_name='community',
            name='is_public',
            field=models.BooleanField(default=True, verbose_name='Is public'),
        ),
        migrations.AlterField(
            model_name='community',
            name='members',
            field=models.ManyToManyField(
                blank=True,
                related_name='joined_communities',
                to='user.profile',
                verbose_name='Members',
            ),
        ),
        migrations.AlterField(
            model_name='community',
            name='moderators',
            field=models.ManyToManyField(
                blank=True,
                related_name='moderated_communities',
                to='user.profile',
                verbose_name='Moderators',
            ),
        ),
        migrations.AlterField(
            model_name='community',
            name='name',
            field=models.CharField(
                error_messages={'unique': 'Community with this name already exists.'},
                max_length=25,
                unique=True,
                verbose_name='Name',
            ),
        ),
        migrations.AlterField(
            model_name='community',
            name='title',
            field=models.CharField(
                blank=True, max_length=50, null=True, verbose_name='Title'
            ),
        ),
    ]
