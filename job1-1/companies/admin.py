from django.contrib import admin
from .models import Company

@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ('company_name', 'location', 'description', 'logo')
    search_fields = ('company_name', 'location')
    list_filter = ('location',)