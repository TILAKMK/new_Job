from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.core.paginator import Paginator

from .models import Job, Applicant
from .forms import JobForm


# ------------------------------------------------------------
# PUBLIC – JOB LIST
# ------------------------------------------------------------
class JobListView(View):
    def get(self, request):
        jobs = Job.objects.filter(status='approved').order_by('-id')
        paginator = Paginator(jobs, 10)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)

        return render(request, 'jobs/job_list.html', {'page_obj': page_obj})


# ------------------------------------------------------------
# PUBLIC – JOB DETAIL
# ------------------------------------------------------------
class JobDetailView(View):
    def get(self, request, job_id):
        job = get_object_or_404(Job, id=job_id)
        return render(request, 'jobs/job_detail.html', {'job': job})


# ------------------------------------------------------------
# COMPANY – CREATE JOB
# ------------------------------------------------------------
@method_decorator(login_required, name='dispatch')
class JobCreateView(View):
    def get(self, request):
        form = JobForm()
        return render(request, 'companies/job_create.html', {'form': form})

    def post(self, request):
        form = JobForm(request.POST)
        if form.is_valid():
            job = form.save(commit=False)
            job.company = request.user.company
            job.save()
            return redirect('jobs:job_list')

        return render(request, 'companies/job_create.html', {'form': form})


# ------------------------------------------------------------
# JOB SEEKER – APPLY FOR JOB
# ------------------------------------------------------------
@method_decorator(login_required, name='dispatch')
class JobApplyView(View):
    def post(self, request, job_id):
        job = get_object_or_404(Job, id=job_id)

        # Avoid duplicate applications
        already = Applicant.objects.filter(job=job, job_seeker=request.user).exists()
        if not already:
            Applicant.objects.create(job=job, job_seeker=request.user)

        return redirect('jobs:job_detail', job_id=job.id)


# ------------------------------------------------------------
# COMPANY – VIEW APPLICANTS
# ------------------------------------------------------------
@login_required
def view_applicants(request, job_id):
    job = get_object_or_404(Job, id=job_id, company=request.user.company)
    applicants = Applicant.objects.filter(job=job).select_related('job_seeker')

    return render(request, "jobs/applicants_list.html", {
        "job": job,
        "applicants": applicants
    })


# ------------------------------------------------------------
# COMPANY – UPDATE APPLICANT STATUS
# ------------------------------------------------------------
@login_required
def update_applicant_status(request, applicant_id, action):
    applicant = get_object_or_404(Applicant, id=applicant_id)

    if applicant.job.company != request.user.company:
        return redirect("jobs:job_list")  # block unauthorized access

    if action == "shortlist":
        applicant.status = "shortlisted"
    elif action == "reject":
        applicant.status = "rejected"
    elif action == "accept":
        applicant.status = "accepted"

    applicant.save()
    return redirect("jobs:view_applicants", job_id=applicant.job.id)
