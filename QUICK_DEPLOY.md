# 🚀 Quick Render Deployment Guide

> Simple 5-minute deployment guide for JobPortal to Render

## Prerequisites
- ✅ GitHub account (code pushed to repo)
- ✅ Render account (free at https://render.com)

## 5 Steps to Deploy

### Step 1: Push to GitHub
```bash
cd job1
git add .
git commit -m "Ready for Render deployment"
git push origin main
```

### Step 2: Go to Render Dashboard
Visit https://render.com/dashboard and sign in

### Step 3: Create Web Service
1. Click **"New +"** → **"Web Service"**
2. Select your **JobPortal repository**
3. **Name**: `jobportal`
4. **Environment**: Python 3
5. **Build Command**: (auto-filled)
   ```
   pip install -r requirements.txt && python manage.py collectstatic --noinput && python manage.py migrate
   ```
6. **Start Command**: (auto-filled)
   ```
   gunicorn job1.wsgi:application
   ```
7. Click **"Create Web Service"**

### Step 4: Set Environment Variables
1. Go to **Environment** tab
2. Add these variables:
   ```
   DEBUG=False
   ALLOWED_HOSTS=<service-name>.onrender.com
   ```
3. Click **"Save"**

### Step 5: Deploy
- Application auto-deploys when service is created
- Monitor **Logs** tab for progress
- ✅ Done when status turns **Green**

## Access Your App
- **Live URL**: `https://<your-service-name>.onrender.com`
- **Admin Panel**: `https://<your-service-name>.onrender.com/admin/`

## Create Admin User
1. Click **"Shell"** in Render dashboard
2. Run:
   ```bash
   python manage.py createsuperuser
   ```

## Add Database (Optional but Recommended)
1. In web service, click **"Add PostgreSQL"**
2. Select **Free** plan
3. Database URL auto-added to environment
4. Service auto-redeploys

## Auto-Deploy on Every Push
From now on, any push to main branch auto-deploys:
```bash
git add .
git commit -m "New feature"
git push origin main
# Your app updates in ~2 minutes automatically!
```

## Troubleshooting

| Problem | Solution |
|---------|----------|
| Build fails | Check build logs, ensure requirements.txt exists |
| Static files missing | Already handled by build script |
| 502 Bad Gateway | Check logs, verify gunicorn command |
| Database not found | Add PostgreSQL from service dashboard |

## Security Checklist
- ✅ DEBUG=False (production)
- ✅ Strong SECRET_KEY (auto-generated)
- ✅ HTTPS enabled (automatic)
- ✅ CSRF protection (built-in)

## Next Steps
1. ✅ Configure custom domain (optional)
2. ✅ Monitor app performance
3. ✅ Set up email notifications
4. ✅ Add team members

## Help
- **Full Guide**: See `DEPLOYMENT.md`
- **Render Docs**: https://render.com/docs
- **Django Docs**: https://docs.djangoproject.com

---
**You're deployed! Celebrate! 🎉**
