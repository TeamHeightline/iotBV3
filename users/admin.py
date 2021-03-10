from django.contrib import admin

from .models import CustomUser
from usertests.admin import MyModelAdmin
# Register your models here.


admin.site.register(CustomUser, MyModelAdmin)