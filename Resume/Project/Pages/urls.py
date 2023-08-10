import urllib
from django.urls import path, include
from django.contrib import admin
from .views import Home, Main, Projects, Certifications, AZ900, OCLIFund, OCLISol, Internships, Skills, Contact_view

urlpatterns = [
    path('', Home, name='Home'),
    path('Main/', Main, name='Main'),
    path('Projects/', Projects, name='Projects'),
    path('Certifications/', Certifications, name='Certifications'),
    path('Certifications/AZ900', AZ900, name='az900'),
    path('Certifications/OCLIFund', OCLIFund, name='oclifund'),
    path('Certifications/OCLISol', OCLISol, name='oclisol'),
    path('Internships/', Internships, name='Internships'),
    path('Skills/', Skills, name='Skills'),
    path('Contact/', Contact_view, name='ReachMe'),
]
