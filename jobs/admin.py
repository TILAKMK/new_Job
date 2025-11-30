from django.contrib import admin
from .models import Job

class JobAdmin(admin.ModelAdmin):
    list_display = ('title', 'company', 'location', 'status', 'created_at')
    list_filter = ('status', 'job_type', 'created_at')
    search_fields = ('title', 'description', 'company__company_name')
    readonly_fields = ('created_at', 'updated_at')

admin.site.register(Job, JobAdmin)