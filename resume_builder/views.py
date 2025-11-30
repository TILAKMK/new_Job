from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .forms import ResumeBuilderForm
from users.models import Profile
from django.shortcuts import redirect

@login_required
def resume_builder_view(request):
    if request.method == 'POST':
        form = ResumeBuilderForm(request.POST)
        if form.is_valid():
            resume_data = form.cleaned_data
            # if user uploaded a resume file, save it to their profile
            resume_file = request.FILES.get('resume')
            if resume_file:
                profile, _ = Profile.objects.get_or_create(user=request.user)
                profile.resume = resume_file
                profile.save()

            return render(request, 'resume_builder/resume_preview.html', {'resume_data': resume_data})
    else:
        form = ResumeBuilderForm()
    
    return render(request, 'resume_builder/resume_form.html', {'form': form})

@login_required
def resume_preview_view(request):
    # This view expects POST data from the resume builder form
    if request.method == 'POST':
        form = ResumeBuilderForm(request.POST)
        if form.is_valid():
            resume_data = form.cleaned_data
            return render(request, 'resume_builder/resume_preview.html', {'resume_data': resume_data})

    # If accessed directly, redirect to builder
    return redirect('resume_builder:resume_builder')