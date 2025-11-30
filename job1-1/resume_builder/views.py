from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import ResumeForm
from .models import Resume
from django.contrib.auth.decorators import login_required
from django.template.loader import render_to_string
from weasyprint import HTML
import tempfile
import os

@login_required
def resume_builder(request):
    if request.method == 'POST':
        form = ResumeForm(request.POST)
        if form.is_valid():
            resume = form.save(commit=False)
            resume.user = request.user
            resume.save()
            return redirect('resume_preview', resume_id=resume.id)
    else:
        form = ResumeForm()
    return render(request, 'resume_builder/resume_form.html', {'form': form})

@login_required
def resume_preview(request, resume_id):
    resume = Resume.objects.get(id=resume_id, user=request.user)
    return render(request, 'resume_builder/resume_preview.html', {'resume': resume})

@login_required
def export_resume(request, resume_id):
    resume = Resume.objects.get(id=resume_id, user=request.user)
    html_string = render_to_string('resume_builder/resume_preview.html', {'resume': resume})
    html = HTML(string=html_string)
    
    with tempfile.NamedTemporaryFile(delete=True) as tmp_file:
        html.write_pdf(target=tmp_file.name)
        with open(tmp_file.name, 'rb') as pdf_file:
            response = HttpResponse(pdf_file.read(), content_type='application/pdf')
            response['Content-Disposition'] = f'attachment; filename="resume_{resume_id}.pdf"'
            return response