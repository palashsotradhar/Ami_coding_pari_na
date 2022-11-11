from django.contrib import admin
from .models import khojmodel,khojm

@admin.register(khojm)
class UserAdmin(admin.ModelAdmin):
    list_display = ('input_values',)
