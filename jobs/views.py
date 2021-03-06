from django.shortcuts import render, get_object_or_404
import jobs
from .models import Job
# from django.utils.translation import gettext as _

# Create your views here.
def homepage(request):
    jobs = Job.objects  #grab everything from db out of Job (this will represent a list of jobS)
    return render(request, 'jobs/home.html', {'jobs': jobs})

def detail (request, job_id):   # whenver this is called the job_id gets forwar
    job_detail = get_object_or_404(Job, pk=job_id)
    return render(request, 'jobs/detail.html', {'job': job_detail})

# def about (request):
#     jobs = Job.objects
#     return render(request, 'jobs/aboutme.html', {'jobs':jobs})

def resume (request):
    jobs = Job.objects
    return render(request, 'jobs/resume.html', {'jobs': jobs})

def portfolio (request):
    jobs = Job.objects
    return render(request, 'jobs/portfolio.html', {'portfolio': jobs})

def homepage (request):
    jobs = Job.objects
    return render(request, 'jobs/homepage.html', {'homepage': jobs })

def certifications(request):
    jobs = Job.objects
    return render(request, 'jobs/certifications.html', {'certifications': jobs })

def aboutme(request):
    jobs = Job.objects
    
    # from django.utils import translation
    # user_language = 'fi'
    # translation.activate(user_language)
    # request.session[translation.LANGUAGE_SESSION_KEY] = user_language
    # if translation.LANGUAGE_SESSION_KEY in request.session:
    #     del request.session[translation.LANGUAGE_SESSION_KEY]

    # title = _('Homepage')
    return render(request, 'jobs/aboutme.html', {'aboutme': jobs})#, 'title': title

def contact(request):
    jobs = Job.objects

    return render(request, 'jobs/contact.html', {'contact': jobs })