from django import forms

class ResumeBuilderForm(forms.Form):
    name = forms.CharField(max_length=100, required=True)
    email = forms.EmailField(required=True)
    phone = forms.CharField(max_length=15, required=True)
    address = forms.CharField(widget=forms.Textarea, required=True)
    skills = forms.CharField(widget=forms.Textarea, required=True)
    experience = forms.CharField(widget=forms.Textarea, required=True)
    education = forms.CharField(widget=forms.Textarea, required=True)