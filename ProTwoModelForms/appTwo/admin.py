from django.contrib import admin

# Register your models here.

from appTwo.models import User
admin.site.register(User)
