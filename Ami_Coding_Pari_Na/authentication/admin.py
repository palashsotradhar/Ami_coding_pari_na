from django.contrib import admin
from .models import login,regimodel

@admin.register(regimodel)
class UserAdmin(admin.ModelAdmin):
    list_display = ('email',)
