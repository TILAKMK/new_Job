from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from .models import Applicant

@login_required
def applicant_dashboard_view(request):
    if request.user.role != 'job_seeker':
        return redirect('home')
    
    applications = Applicant.objects.filter(job_seeker=request.user).select_related('job', 'job__company')
    
    stats = {
        'total_applications': applications.count(),
        'applied': applications.filter(status='applied').count(),
        'shortlisted': applications.filter(status='shortlisted').count(),
        'rejected': applications.filter(status='rejected').count(),
        'accepted': applications.filter(status='accepted').count(),
    }
    
    return render(request, 'applicants/applicant_dashboard.html', {'applications': applications, 'stats': stats})