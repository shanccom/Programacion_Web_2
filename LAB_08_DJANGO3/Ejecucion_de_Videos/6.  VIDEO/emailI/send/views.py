from django.shortcuts import render
from django.core.mail import send_mail

def index(request):

    send_mail('Hola',
    'Mensaje automatico PRUEBA 1', 
    'sergiodanilohancco@gmail.com',
    ['chechower@gmail.com'],
    fail_silently = False)

    return render(request, 'send/index.html')
