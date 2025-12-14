# Deployment Documentation

## Project
Social Media API (Django REST Framework)

## Production Configuration
- DEBUG set to False
- ALLOWED_HOSTS configured
- Security headers enabled
- Static files collected using collectstatic
- Gunicorn used as WSGI server

## Hosting Platform
The application is prepared for deployment on platforms such as:
- Heroku
- Render
- AWS Elastic Beanstalk

## Static Files
Static files are managed using Django's collectstatic command and served from the staticfiles directory.

## Environment Variables
- SECRET_KEY is stored as an environment variable in production
- DEBUG is disabled in production

## Deployment Steps
1. Push code to GitHub repository
2. Configure environment variables on hosting provider
3. Run database migrations
4. Collect static files
5. Start application using Gunicorn

## Monitoring & Maintenance
- Logs monitored via hosting provider dashboard
- Regular dependency updates planned
