from django.contrib import admin
from .models import Company

class CompanyAdmin(admin.ModelAdmin):
    list_display = ('company_name', 'owner', 'location', 'created_at')
    search_fields = ('company_name', 'location')
    readonly_fields = ('created_at', 'updated_at')

admin.site.register(Company, CompanyAdmin)