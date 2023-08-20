from django.shortcuts import render, HttpResponse
from .models import Contact


# Create your views here.

def Home(request):
    return render(request, 'Home.html')


def Main(request):
    return render(request, 'Main.html')


def Projects(request):
    return render(request, 'Projects.html')


def Certifications(request):
    return render(request, 'Certifications.html')


def AZ900(request):
    return render(request, 'AZ900.html')


def OCLIFund(request):
    return render(request, 'oclifund.html')


def OCLISol(request):
    return render(request, 'oclisol.html')


def Internships(request):
    return render(request, 'Internships.html')


def Skills(request):
    return render(request, 'Skills.html')


def Contact_view(request):
    if request.method == "POST":
        contact = Contact()
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        contact.name = name
        contact.email = email
        contact.message = message
        contact.save()
        return render(request, 'Thankyou.html')
    return render(request, 'Contact.html')
