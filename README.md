# Portfolio Website

A Django-based portfolio website deployed on Vercel.

## Features

- Responsive design
- Project showcase
- Contact form
- Resume upload and download
- Admin panel for content management

## Local Development

1. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/Mac
   venv\Scripts\activate     # Windows
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Create `.env` file with these variables:
   ```
   SECRET_KEY=your-secret-key
   DEBUG=True
   ```

4. Run migrations:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. Create superuser:
   ```bash
   python manage.py createsuperuser
   ```

6. Run development server:
   ```bash
   python manage.py runserver
   ```

## Deployment

The project is configured for deployment on Vercel:

1. Install Vercel CLI:
   ```bash
   npm install -g vercel
   ```

2. Deploy:
   ```bash
   vercel
   ```

3. For production deployment:
   ```bash
   vercel --prod
   ```

## Environment Variables

Set these in Vercel dashboard:

- `DEBUG`: Set to 'False'
- `SECRET_KEY`: Your Django secret key
- `ALLOWED_HOSTS`: Your Vercel domain

## Tech Stack

- Django
- Bootstrap
- SQLite
- Whitenoise for static files
- Crispy Forms
