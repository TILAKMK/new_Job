from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from .models import Job
from .forms import JobForm
from django.core.paginator import Paginator

class JobListView(View):
    def get(self, request):
        jobs = Job.objects.filter(status='approved').order_by('-id')
        paginator = Paginator(jobs, 10)  # Show 10 jobs per page
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        return render(request, 'jobs/job_list.html', {'page_obj': page_obj})

class JobDetailView(View):
    def get(self, request, job_id):
        job = get_object_or_404(Job, id=job_id)
        return render(request, 'jobs/job_detail.html', {'job': job})

@method_decorator(login_required, name='dispatch')
class JobCreateView(View):
    def get(self, request):
        form = JobForm()
        return render(request, 'companies/job_create.html', {'form': form})

    def post(self, request):
        form = JobForm(request.POST)
        if form.is_valid():
            job = form.save(commit=False)
            job.company = request.user.company  # Assuming the user has a related Company
            job.save()
            return redirect('jobs:job_list')
        return render(request, 'companies/job_create.html', {'form': form})

@method_decorator(login_required, name='dispatch')
class JobApplyView(View):
    def post(self, request, job_id):
        job = get_object_or_404(Job, id=job_id)
        # Logic to handle job application (e.g., create an Applicant instance)
        return redirect('jobs:job_detail', job_id=job.id)