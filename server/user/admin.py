from django.contrib import admin
from .models import UserProfile
# Register your models here.


class UserProfileAdmin(admin.ModelAdmin):
    fields = ('id', 'user', 'phone', 'address')


admin.site.register(UserProfile, UserProfileAdmin)
