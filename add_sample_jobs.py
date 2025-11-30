#!/usr/bin/env python
"""
Script to add sample jobs and companies to the database
Run with: python manage.py shell < add_sample_jobs.py
"""

from users.models import CustomUser
from companies.models import Company
from jobs.models import Job

# Create sample users for companies if they don't exist
users_data = [
    {'username': 'tech_corp', 'email': 'careers@techcorp.com', 'role': 'company'},
    {'username': 'design_co', 'email': 'hr@designco.com', 'role': 'company'},
    {'username': 'data_solutions', 'email': 'jobs@datasolutions.com', 'role': 'company'},
]

company_users = []
for user_data in users_data:
    user, created = CustomUser.objects.get_or_create(
        username=user_data['username'],
        defaults={
            'email': user_data['email'],
            'role': user_data['role'],
        }
    )
    if created:
        user.set_password('temppassword123')
        user.save()
    company_users.append(user)

print(f"Created/Found {len(company_users)} company users")

# Create companies
companies_data = [
    {'owner': company_users[0], 'company_name': 'TechCorp Solutions', 'description': 'Leading technology solutions provider', 'location': 'San Francisco, CA'},
    {'owner': company_users[1], 'company_name': 'Design Innovations Co', 'description': 'Creative design and digital marketing agency', 'location': 'New York, NY'},
    {'owner': company_users[2], 'company_name': 'Data Solutions Inc', 'description': 'Big data and analytics consulting firm', 'location': 'Austin, TX'},
]

companies = []
for company_data in companies_data:
    company, created = Company.objects.get_or_create(
        owner=company_data['owner'],
        defaults={
            'company_name': company_data['company_name'],
            'description': company_data['description'],
            'location': company_data['location'],
        }
    )
    if created:
        print(f"Created company: {company.company_name}")
    companies.append(company)

# Create sample jobs
jobs_data = [
    {
        'company': companies[0],
        'title': 'Senior Python Developer',
        'description': 'We are looking for an experienced Python developer to join our backend team. You will work on scalable web applications and microservices. Requirements: 5+ years of experience, strong knowledge of Django, and experience with REST APIs.',
        'category': 'Software Development',
        'location': 'San Francisco, CA',
        'job_type': 'full_time',
        'salary_min': 120000,
        'salary_max': 180000,
        'status': 'approved'
    },
    {
        'company': companies[0],
        'title': 'DevOps Engineer',
        'description': 'Join our infrastructure team to manage and optimize our cloud infrastructure. Experience with Docker, Kubernetes, and AWS is required. We offer competitive salary and excellent benefits.',
        'category': 'DevOps',
        'location': 'San Francisco, CA',
        'job_type': 'full_time',
        'salary_min': 110000,
        'salary_max': 160000,
        'status': 'approved'
    },
    {
        'company': companies[0],
        'title': 'Frontend Developer',
        'description': 'Build beautiful and responsive web interfaces using React. We are seeking a talented developer with 3+ years of experience in modern JavaScript frameworks.',
        'category': 'Software Development',
        'location': 'Remote',
        'job_type': 'full_time',
        'salary_min': 90000,
        'salary_max': 140000,
        'status': 'approved'
    },
    {
        'company': companies[1],
        'title': 'UI/UX Designer',
        'description': 'Create stunning user experiences for digital products. We are looking for designers with a strong portfolio and experience in Figma and Adobe XD.',
        'category': 'Design',
        'location': 'New York, NY',
        'job_type': 'full_time',
        'salary_min': 80000,
        'salary_max': 130000,
        'status': 'approved'
    },
    {
        'company': companies[1],
        'title': 'Graphic Designer',
        'description': 'Design marketing materials, branding, and digital content. Proficiency in Adobe Creative Suite is essential. Join a creative team with 2+ years of experience.',
        'category': 'Design',
        'location': 'New York, NY',
        'job_type': 'part_time',
        'salary_min': 50000,
        'salary_max': 80000,
        'status': 'approved'
    },
    {
        'company': companies[2],
        'title': 'Data Scientist',
        'description': 'Analyze large datasets and develop machine learning models. We are seeking someone with strong Python and SQL skills, and experience with TensorFlow or PyTorch.',
        'category': 'Data Science',
        'location': 'Austin, TX',
        'job_type': 'full_time',
        'salary_min': 130000,
        'salary_max': 200000,
        'status': 'approved'
    },
    {
        'company': companies[2],
        'title': 'Data Analyst',
        'description': 'Create dashboards and reports from complex datasets. You will work with stakeholders to understand data needs and provide actionable insights.',
        'category': 'Data Science',
        'location': 'Austin, TX',
        'job_type': 'full_time',
        'salary_min': 85000,
        'salary_max': 130000,
        'status': 'approved'
    },
    {
        'company': companies[0],
        'title': 'Software QA Engineer',
        'description': 'Test and ensure quality of our software products. Experience with automated testing frameworks and knowledge of Python is preferred.',
        'category': 'QA/Testing',
        'location': 'San Francisco, CA',
        'job_type': 'full_time',
        'salary_min': 85000,
        'salary_max': 125000,
        'status': 'approved'
    },
    {
        'company': companies[1],
        'title': 'Content Marketing Specialist',
        'description': 'Create engaging content for our blog and social media. SEO knowledge and 2+ years of content writing experience required.',
        'category': 'Marketing',
        'location': 'Remote',
        'job_type': 'full_time',
        'salary_min': 60000,
        'salary_max': 100000,
        'status': 'approved'
    },
    {
        'company': companies[2],
        'title': 'Business Analyst Intern',
        'description': 'Summer internship program for recent graduates. Learn data analysis and business intelligence in a fast-paced environment. Great opportunity for entry-level professionals.',
        'category': 'Business',
        'location': 'Austin, TX',
        'job_type': 'internship',
        'salary_min': 20000,
        'salary_max': 30000,
        'status': 'approved'
    }
]

for job_data in jobs_data:
    job, created = Job.objects.get_or_create(
        company=job_data['company'],
        title=job_data['title'],
        defaults={
            'description': job_data['description'],
            'category': job_data['category'],
            'location': job_data['location'],
            'job_type': job_data['job_type'],
            'salary_min': job_data['salary_min'],
            'salary_max': job_data['salary_max'],
            'status': job_data['status'],
        }
    )
    if created:
        print(f"Created job: {job.title}")

total_jobs = Job.objects.count()
print(f"\nTotal jobs in database: {total_jobs}")
print("Sample jobs have been added successfully!")
