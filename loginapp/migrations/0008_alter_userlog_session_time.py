# Generated by Django 4.0.1 on 2022-06-19 15:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loginapp', '0007_alter_userlog_session_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userlog',
            name='session_time',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
    ]
