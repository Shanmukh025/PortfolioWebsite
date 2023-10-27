from django.shortcuts import render, HttpResponse
from .models import Contact
from django.http import FileResponse
from django.conf import settings


# Create your views here.

def Home(request):
    return render(request, 'Home.html')


def Main(request):
    return render(request, 'Main.html')


def Projects(request):
    return render(request, 'Projects.html')


def Certifications(request):
    return render(request, 'Certifications.html')


def az900(request):
    return render(request, 'az900.html')


def az204(request):
    return render(request, 'az204.html')


def Redhat(request):
    return render(request, 'redhat.html')


def OCLIFund(request):
    return render(request, 'oclifund.html')


def OCLISol(request):
    return render(request, 'oclisol.html')


def Internships(request):
    return render(request, 'Internships.html')


def Aicte(request):
    return render(request, 'Aicte.html')


def Skills(request):
    return render(request, 'Skills.html')


def ContactMe(request):
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


def download_pdf(request):
    return render(request, 'temp.html')
    '''
    pdf_path = os.path.join(settings.BASE_DIR, 'static/pdfs/ShanmukhResume.pdf')
    pdf_file = open(pdf_path, 'rb')
    pdf_content = pdf_file.read()
    pdf_file.close()

    response = HttpResponse(pdf_content, content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="ShanmukhResume.pdf"'
    return response
    '''


def Social(request):
    return render(request, 'Profile.html')
