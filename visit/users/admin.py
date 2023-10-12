from django.contrib import admin
from django.contrib.auth.models import Group

from .models import User


class UserAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'phone')
    search_fields = ('name',)


admin.site.register(User, UserAdmin)
admin.site.unregister(Group)
