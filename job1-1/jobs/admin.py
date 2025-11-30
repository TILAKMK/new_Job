from django.contrib import admin
from .models import Job

@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    list_display = ('title', 'company', 'location', 'type', 'salary', 'status')
    list_filter = ('status', 'type', 'location')
    search_fields = ('title', 'description', 'company__company_name')
    ordering = ('-status', 'title')