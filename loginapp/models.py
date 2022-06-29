from django.db import models

from django.contrib.auth.models import User
# Create your models here.

class UserLog(models.Model):
    username = models.CharField(
        max_length = 20,
        null = True,
        blank = True,
    )
    login_time = models.CharField(
        
        max_length = 10,
        null = True,
        blank = True,
    )
    logout_time = models.CharField(
        
        max_length = 10,
        null = True,
        blank = True,
    )
    updated_on = models.DateTimeField( auto_now_add= True)

    session_time = models.CharField(
        
        max_length = 10,
        null = True,
        blank = True,
    )

