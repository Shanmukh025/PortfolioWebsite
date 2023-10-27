import urllib
from django.urls import path, include
from django.contrib import admin
from .views import Home, Main, Projects, Certifications, az900, az204, Redhat, OCLISol, Internships, Aicte, Skills, ContactMe, download_pdf, Social

urlpatterns = [
    path('', Home, name='Home'),
    path('Main/', Main, name='Main'),
    path('Projects/', Projects, name='Projects'),
    path('Certifications/', Certifications, name='Certifications'),
    path('Certifications/az900', az900, name='az900'),
    path('Certifications/az204', az204, name='az204'),
    path('Certifications/Redhat', Redhat, name='redhat'),
    path('Certifications/OCLISol', OCLISol, name='oclisol'),
    path('Internships/', Internships, name='Internships'),
    path('aicte/', Aicte, name='aicte'),
    path('Skills/', Skills, name='Skills'),
    path('ContactMe/', ContactMe, name='ContactMe'),
    path('Social/', Social, name='Social'),
    path('download-pdf/', download_pdf, name='download_pdf'),
]
