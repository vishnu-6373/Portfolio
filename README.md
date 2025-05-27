# Portfolio Website

A modern, responsive portfolio website built with Django, featuring a projects showcase, resume download, and contact form.

## Features

- Responsive design with Bootstrap 5
- Projects showcase with filtering
- Downloadable resume
- Contact form with email notifications
- Admin panel for content management
- PostgreSQL database
- Modern animations and transitions

## Prerequisites

- Python 3.8+
- PostgreSQL
- pip (Python package manager)

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd portfolio
```

2. Create a virtual environment and activate it:
```bash
python -m venv venv
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate
```

3. Install required packages:
```bash
pip install -r requirements.txt
```

4. Create a PostgreSQL database named 'portfolio_db'.

5. Copy the `.env.example` file to `.env` and update the variables:
```bash
cp .env.example .env
```

Update the following variables in the `.env` file:
- `SECRET_KEY`: Your Django secret key
- `DB_PASSWORD`: Your PostgreSQL password
- `EMAIL_HOST_USER`: Your email address
- `EMAIL_HOST_PASSWORD`: Your email app-specific password

6. Run migrations:
```bash
python manage.py makemigrations
python manage.py migrate
```

7. Create a superuser:
```bash
python manage.py createsuperuser
```

8. Create required directories:
```bash
mkdir -p media/projects media/profile media/resumes
```

## Running the Development Server

```bash
python manage.py runserver
```

The site will be available at http://127.0.0.1:8000/

## Admin Panel

Access the admin panel at http://127.0.0.1:8000/admin to:
- Add/edit projects
- Update profile information
- Manage resume uploads
- View contact form submissions

## Project Structure

```
portfolio/
├── core/                   # Main app directory
│   ├── models.py          # Database models
│   ├── views.py           # View functions
│   ├── forms.py           # Forms
│   ├── urls.py           # URL patterns
│   └── admin.py          # Admin configurations
├── static/                # Static files
│   ├── css/              # CSS files
│   ├── js/               # JavaScript files
│   └── img/              # Images
├── media/                 # User-uploaded content
├── templates/            # HTML templates
│   ├── base.html        # Base template
│   └── core/            # App templates
├── portfolio/           # Project settings
└── manage.py           # Django management script
```

## Customization

1. Profile Information:
   - Log in to the admin panel
   - Add your profile details (name, bio, social links)
   - Upload a profile picture

2. Projects:
   - Add projects through the admin panel
   - Include title, description, technologies used
   - Add project images and links

3. Resume:
   - Upload your resume through the admin interface
   - Only PDF files are supported

4. Styling:
   - Custom styles are in `static/css/style.css`
   - Main color scheme and other variables can be modified here

## Deployment

1. Set `DEBUG=False` in `.env`
2. Update `ALLOWED_HOSTS` in `.env`
3. Configure your web server (e.g., Nginx)
4. Set up a production database
5. Configure static and media files serving
6. Use a production WSGI server (e.g., Gunicorn)

## Technology Stack

- Django 4.2.1
- PostgreSQL
- Bootstrap 5
- JavaScript (Vanilla)
- HTML5 & CSS3

## License

This project is licensed under the MIT License - see the LICENSE file for details.
