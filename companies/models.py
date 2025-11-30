from django.db import models
from users.models import CustomUser

class Company(models.Model):
    owner = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name='company')
    company_name = models.CharField(max_length=200)
    description = models.TextField()
    location = models.CharField(max_length=200)
    website = models.URLField(blank=True, null=True)
    logo = models.ImageField(upload_to='company_logos/', blank=True, null=True)
    established_year = models.IntegerField(blank=True, null=True)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        db_table = 'companies_company'
        verbose_name_plural = 'Companies'
    
    def __str__(self):
        return self.company_name