from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Applicant
from .forms import ApplicantForm

@login_required
def applicants_list(request):
    applicants = Applicant.objects.filter(job__applicants=request.user.profile)
    return render(request, 'applicants/applicants_list.html', {'applicants': applicants})

@login_required
def apply_job(request, job_id):
    if request.method == 'POST':
        form = ApplicantForm(request.POST)
        if form.is_valid():
            applicant = form.save(commit=False)
            applicant.job_id = job_id
            applicant.job_seeker = request.user.profile
            applicant.save()
            return redirect('applicants:applicants_list')
    else:
        form = ApplicantForm()
    return render(request, 'jobs/apply_job.html', {'form': form})

@login_required
def update_application_status(request, applicant_id, status):
    applicant = Applicant.objects.get(id=applicant_id)
    if request.user.profile.company == applicant.job.company:
        applicant.status = status
        applicant.save()
    return redirect('applicants:applicants_list')