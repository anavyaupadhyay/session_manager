from django.contrib import admin
from .models import UserLog

# Register your models here.

# admin.site.register(UserLog)
@admin.register(UserLog)
class UserLogAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'login_time', 'logout_time', 'session_time', 'updated_on')