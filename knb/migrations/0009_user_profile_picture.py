# Generated by Django 5.1.6 on 2025-03-01 00:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('knb', '0008_user_games_total'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='profile_picture',
            field=models.ImageField(blank=True, default='default_avatar.png', null=True, upload_to='profile_pics/'),
        ),
    ]
