from django import forms
from .models import Company

class CompanyForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = ['company_name', 'description', 'location', 'logo']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 4}),
        }