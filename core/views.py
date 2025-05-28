from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from .models import Project, Resume, Profile
from .forms import ContactForm, ResumeForm

def home(request):
    try:
        profile = Profile.objects.first()
    except:
        # If database table doesn't exist or any other error
        profile = None
    
    try:
        projects = Project.objects.all()[:3]  # Get latest 3 projects
    except:
        projects = []
    
    context = {
        'profile': profile,
        'projects': projects,
    }
    return render(request, 'core/home.html', context)

def projects(request):
    try:
        projects = Project.objects.all()
    except:
        projects = []
    context = {
        'projects': projects,
        'title': 'Projects'
    }
    return render(request, 'core/projects.html', context)

def resume(request):
    latest_resume = Resume.objects.first()
    if request.method == 'POST':
        form = ResumeForm(request.POST, request.FILES)
        if form.is_valid():
            if latest_resume:
                latest_resume.delete()  # Delete old resume
            form.save()
            messages.success(request, 'Resume uploaded successfully!')
            return redirect('resume')
    else:
        form = ResumeForm()
    
    context = {
        'resume': latest_resume,
        'form': form,
        'title': 'Resume'
    }
    return render(request, 'core/resume.html', context)

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Save the contact form data first
            contact = form.save()
            
            # Prepare email content
            subject = f'New Contact Message from {contact.name}'
            message = f"""
            Name: {contact.name}
            Email: {contact.email}
            Message: {contact.message}
            
            Sent at: {contact.created_at}
            """
            from_email = settings.EMAIL_HOST_USER
            recipient_list = [settings.EMAIL_HOST_USER]
            
            if settings.DEBUG:
                # In development, just log to console
                print(f"\nNew Contact Form Submission:")
                print(f"Subject: {subject}")
                print(f"Message: {message}")
                print(f"From: {from_email}")
                print(f"To: {recipient_list}\n")
                messages.success(request, 'Message saved successfully! (Email sending is disabled in development mode)')
            else:
                # In production, attempt to send email
                try:
                    send_mail(subject, message, from_email, recipient_list)
                    messages.success(request, 'Your message has been sent successfully!')
                except Exception as e:
                    messages.warning(request, 'Your message was saved but there was an error sending the email notification.')
                    print(f"Email error: {str(e)}")
            
            return redirect('contact')
    else:
        form = ContactForm()
    
    try:
        profile = Profile.objects.first()
    except:
        profile = None
    context = {
        'form': form,
        'profile': profile,
        'title': 'Contact'
    }
    return render(request, 'core/contact.html', context)

def download_resume(request):
    resume = get_object_or_404(Resume.objects.first())
    response = redirect(resume.file.url)
    return response
