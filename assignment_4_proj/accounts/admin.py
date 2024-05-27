from django.contrib import admin
from .models import User

from django.contrib import admin

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'user_type')
    ordering = ('user_type',)
    search_fields = ('email', 'user_type')


