from django.contrib import admin
from .models import Applicant

class ApplicantAdmin(admin.ModelAdmin):
    list_display = ('job_seeker', 'job', 'status', 'applied_at')
    list_filter = ('status', 'applied_at')
    search_fields = ('job_seeker__username', 'job__title')
    readonly_fields = ('applied_at', 'updated_at')

admin.site.register(Applicant, ApplicantAdmin)