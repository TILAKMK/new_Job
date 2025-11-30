from django import forms

class ResumeBuilderForm(forms.Form):
    # Personal Information
    full_name = forms.CharField(max_length=200, widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))
    phone = forms.CharField(max_length=15, widget=forms.TextInput(attrs={'class': 'form-control'}))
    location = forms.CharField(max_length=200, widget=forms.TextInput(attrs={'class': 'form-control'}))
    
    # Professional Summary
    summary = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 4}), required=False)
    
    # Experience
    experience = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 4, 'placeholder': 'Job Title - Company (Year)\nDescription'}), required=False)
    
    # Education
    education = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 4, 'placeholder': 'Degree - University (Year)'}), required=False)
    
    # Skills
    skills = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Comma-separated skills'}), required=False)
    
    # Certifications
    certifications = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 3}), required=False)