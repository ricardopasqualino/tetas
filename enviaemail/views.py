from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.core.mail import send_mail

def envia_email(request):
    send_mail(
            'Assunto', # Assunto do email
            'Sua compra chegou na portaria', # Mensagem do email
            'EMAIL_HOST_USER', # from do email
            ['ricardo.pasqualino@gmail.com'], #  email do para
            fail_silently=False,
        )
    return redirect('Home')