# Generated by Django 4.0.1 on 2022-06-19 15:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loginapp', '0006_alter_userlog_login_time_alter_userlog_logout_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userlog',
            name='session_time',
            field=models.DurationField(blank=True, null=True),
        ),
    ]