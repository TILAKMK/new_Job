# JobPortal - Modern Django Job Portal

A professional, full-featured job portal web application built with Django 5.2 and Bootstrap 5. Connect job seekers with employers in a beautiful, modern interface.

![Django](https://img.shields.io/badge/Django-5.2.8-092E20?style=flat-square&logo=django)
![Python](https://img.shields.io/badge/Python-3.11+-3776AB?style=flat-square&logo=python)
![Bootstrap](https://img.shields.io/badge/Bootstrap-5.3-7952B3?style=flat-square&logo=bootstrap)
![License](https://img.shields.io/badge/License-MIT-green?style=flat-square)

## Features

### 🎯 Core Features
- **User Management**: Custom user authentication with role-based access (Job Seeker, Employer, Admin)
- **Job Listings**: Browse thousands of job opportunities with advanced filtering
- **Job Applications**: Apply directly to jobs and track application status
- **Company Profiles**: Employer dashboard to create and manage company profiles
- **Job Posting**: Employers can post new job openings with detailed information
- **Resume Builder**: Job seekers can create and manage professional resumes
- **User Profiles**: Customizable user profiles with preference management
- **Modern UI/UX**: Responsive design with Bootstrap 5 and smooth animations

### 💼 Employer Features
- Create and manage company profiles
- Post job listings with detailed descriptions
- View job applications and applicants
- Manage job postings (create, edit, delete)
- Track active job listings

### 👤 Job Seeker Features
- Browse and search job listings
- Apply to multiple jobs
- Track application status
- Build and manage resumes
- Manage user profile and preferences

### 🔐 Security Features
- CSRF protection
- SQL injection prevention
- XSS protection
- Secure password hashing
- Session management
- WhiteNoise for static file serving in production

## Technology Stack

### Backend
- **Django 5.2.8** - Python web framework
- **Django REST Framework** - API development
- **PostgreSQL/SQLite** - Database (PostgreSQL for production)
- **Gunicorn** - WSGI application server
- **python-decouple** - Environment variable management
- **dj-database-url** - Database URL parsing

### Frontend
- **Bootstrap 5.3** - CSS framework
- **Font Awesome 6.4** - Icon library
- **CSS3** - Modern styling with animations
- **JavaScript** - Interactive components

### Additional Libraries
- **Pillow** - Image processing
- **WeasyPrint** - PDF generation for resumes
- **Django Crispy Forms** - Form rendering
- **WhiteNoise** - Static file compression

## Installation & Setup

### Prerequisites
- Python 3.11 or higher
- pip (Python package manager)
- Virtual environment (recommended)

### Local Development Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/jobportal.git
   cd jobportal/job1
   ```

2. **Create and activate virtual environment**
   ```bash
   # Windows
   python -m venv venv
   venv\Scripts\activate
   
   # macOS/Linux
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Create .env file** (copy from .env.example)
   ```bash
   cp .env.example .env
   ```

5. **Run migrations**
   ```bash
   python manage.py migrate
   ```

6. **Create superuser**
   ```bash
   python manage.py createsuperuser
   ```

7. **Run development server**
   ```bash
   python manage.py runserver
   ```

8. **Access the application**
   - Home: http://localhost:8000/
   - Admin: http://localhost:8000/admin/

## Project Structure

```
jobportal/
├── job1/                      # Main Django project
│   ├── manage.py             # Django management script
│   ├── requirements.txt       # Python dependencies
│   ├── db.sqlite3           # SQLite database (development)
│   ├── build.sh             # Render build script
│   ├── render.yaml          # Render deployment config
│   ├── .env.example         # Environment variables template
│   │
│   ├── job1/                # Project settings
│   │   ├── settings.py      # Django configuration
│   │   ├── urls.py          # URL routing
│   │   ├── wsgi.py          # WSGI configuration
│   │
│   ├── templates/           # HTML templates
│   │   ├── base.html        # Base template with navbar/footer
│   │   ├── home.html        # Home page
│   │   ├── jobs/            # Job-related templates
│   │   ├── companies/       # Company-related templates
│   │   ├── users/           # User-related templates
│   │   └── resume_builder/  # Resume builder templates
│   │
│   ├── static/              # Static files
│   │   ├── css/             # Custom CSS
│   │   └── js/              # JavaScript files
│   │
│   ├── media/               # User-uploaded files
│   │
│   └── apps/                # Django apps
│       ├── users/           # User authentication & management
│       ├── jobs/            # Job listings & applications
│       ├── companies/       # Company profiles & management
│       ├── applicants/      # Application tracking
│       └── resume_builder/  # Resume creation & management
│
└── README.md               # This file
```

## Database Schema

### User Roles
- **Admin**: Full system access
- **Job Seeker**: Can browse jobs, apply, create resumes
- **Employer**: Can create company profile, post jobs, view applications

### Key Models
- **CustomUser**: Extended user model with role field
- **Company**: Employer company information
- **Job**: Job listing details
- **Application**: Job application tracking
- **Resume**: Resume information for job seekers
- **Profile**: User profile preferences

## Environment Variables

Create a `.env` file in the project root with:

```env
# Django Settings
DEBUG=False
SECRET_KEY=your-very-secure-secret-key-here
ALLOWED_HOSTS=localhost,127.0.0.1,yourdomain.com

# Database (Optional - leave empty for SQLite)
DATABASE_URL=postgresql://user:password@host:5432/dbname

# Render.com will automatically set these:
# DATABASE_URL (PostgreSQL URL from add-on)
# SECRET_KEY (generated automatically)
```

## Deployment to Render

### Step-by-Step Deployment Guide

1. **Push code to GitHub**
   ```bash
   git add .
   git commit -m "Prepare for Render deployment"
   git push origin main
   ```

2. **Create Render Account**
   - Visit [Render.com](https://render.com)
   - Sign up with your GitHub account

3. **Connect GitHub Repository**
   - Go to Dashboard → New → Web Service
   - Connect your GitHub repository
   - Select the repository containing this project

4. **Configure Web Service**
   - **Name**: jobportal
   - **Runtime**: Python 3.11
   - **Build Command**: `pip install -r requirements.txt && python manage.py collectstatic --noinput && python manage.py migrate`
   - **Start Command**: `gunicorn job1.wsgi:application`
   - **Auto-deploy**: Enable

5. **Set Environment Variables**
   - Go to Environment in service settings
   - Add these variables:
     ```
     DEBUG=False
     ALLOWED_HOSTS=yourdomain.onrender.com
     ```
   - `SECRET_KEY` and `DATABASE_URL` will be auto-generated by Render

6. **Add PostgreSQL Database (Optional but Recommended)**
   - Click "Add PostgreSQL" in the services panel
   - Select plan (free tier available)
   - Database URL will be automatically added to environment

7. **Deploy**
   - Click "Deploy" button
   - Monitor deployment logs
   - Once complete, access your app at provided URL

### Render Deployment Features
- **Auto-deploy on push**: Changes pushed to main branch auto-deploy
- **Free tier available**: Run production apps without cost
- **PostgreSQL included**: Free database with web service
- **SSL certificate**: Automatic HTTPS for all apps
- **Environment variables**: Secure secret management

## Usage

### For Job Seekers
1. Register as "Job Seeker"
2. Browse job listings on the Jobs page
3. Click on jobs to view details
4. Click "Apply" to submit application
5. Track applications in "Applications" section
6. Use Resume Builder to create professional resume

### For Employers
1. Register as "Employer"
2. Create company profile with logo and description
3. Go to "Post Job" to create job listings
4. Add job details (title, description, salary, location, etc.)
5. View posted jobs in company profile
6. See applications in company dashboard

### For Admins
1. Access Django admin at `/admin/`
2. Manage users, jobs, companies
3. Approve/reject job listings
4. Monitor applications

## API Endpoints

### Jobs
- `GET /jobs/` - List all jobs
- `GET /jobs/<id>/` - Job details
- `POST /jobs/<id>/apply/` - Apply to job
- `POST /jobs/post/` - Create new job (employer only)

### Companies
- `GET /companies/<id>/` - Company profile
- `POST /companies/create/` - Create company (employer only)

### Users
- `GET /profile/` - User profile
- `POST /login/` - User login
- `POST /register/` - User registration
- `POST /logout/` - User logout

## Performance Optimizations

- **Static files**: Compressed with WhiteNoise
- **Database queries**: Optimized with select_related/prefetch_related
- **Caching**: Page-level caching enabled
- **Security headers**: CSP, XSS protection enabled
- **CDN**: Bootstrap and Font Awesome served via CDN

## Security Considerations

1. **Never commit `.env` file** - Use `.env.example` as template
2. **Change SECRET_KEY** - Generate strong secret key for production
3. **Use HTTPS** - Always use HTTPS in production
4. **Database security** - Use strong passwords for PostgreSQL
5. **Regular updates** - Keep Django and dependencies updated

## Troubleshooting

### Common Issues

**Issue**: Static files not loading in production
- **Solution**: Run `python manage.py collectstatic --noinput`

**Issue**: Database migrations fail
- **Solution**: Check DATABASE_URL environment variable, ensure migrations exist

**Issue**: 502 Bad Gateway on Render
- **Solution**: Check build logs, verify Gunicorn start command

**Issue**: CSRF token missing
- **Solution**: Ensure session middleware is enabled, check CSRF_TRUSTED_ORIGINS

## Development Tips

### Create Test Data
```bash
python manage.py shell
from jobs.models import Job, Company
from users.models import CustomUser

# Add sample data in shell
```

### Run Tests
```bash
python manage.py test
```

### Access Django Shell
```bash
python manage.py shell
```

### Database Backup
```bash
# SQLite
cp db.sqlite3 db.sqlite3.backup

# PostgreSQL
pg_dump databasename > backup.sql
```

## Contributing

1. Fork the repository
2. Create feature branch: `git checkout -b feature/YourFeature`
3. Commit changes: `git commit -m 'Add YourFeature'`
4. Push to branch: `git push origin feature/YourFeature`
5. Open a Pull Request

## Future Enhancements

- [ ] Email notifications for applications
- [ ] Advanced job search filters
- [ ] Job recommendations based on profile
- [ ] Two-factor authentication
- [ ] Social media login integration
- [ ] Video interview capabilities
- [ ] Salary comparison tools
- [ ] Mobile app (React Native)
- [ ] Real-time notifications with WebSockets
- [ ] Analytics dashboard for employers

## License

This project is licensed under the MIT License - see LICENSE file for details.

## Support

For issues, questions, or suggestions:
- Open an issue on GitHub
- Contact: support@jobportal.com
- Documentation: [Full docs](https://github.com/yourusername/jobportal/wiki)

## Acknowledgments

- Django community for excellent framework
- Bootstrap team for responsive UI framework
- Font Awesome for icon library
- All contributors and users

---

**Built with ❤️ by the JobPortal Team**

Last Updated: November 2025
