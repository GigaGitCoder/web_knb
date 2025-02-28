# Generated by Django 5.1.6 on 2025-02-28 12:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('knb', '0002_customuser'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='last_login',
            field=models.DateTimeField(blank=True, null=True, verbose_name='last login'),
        ),
        migrations.AlterField(
            model_name='user',
            name='login',
            field=models.CharField(max_length=30, unique=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='password',
            field=models.CharField(max_length=128, verbose_name='password'),
        ),
        migrations.DeleteModel(
            name='CustomUser',
        ),
    ]
