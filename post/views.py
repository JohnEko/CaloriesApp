from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, logout, authenticate
from django.core.mail import send_mail
from django.conf import settings
from .forms import Emailsender
from .forms import ContactForm
from.forms import AuthenthecationForm
from.forms import RegisterForm
from .models import Sendemail




# Create your views here.
def index(request):
    user = Sendemail.objects.all()

    context = {'user' : user}

    return render(request, 'main.html', context)


def registeration(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user  = form.save('username', 'password')
            login(request, user)
            return redirect("index")

    form = RegisterForm()
    context ={'form' : form}
    return render(request, 'registration/register.html', context)

def login_page(request):
    if request.method == 'POST':
        form = AuthenthecationForm(request.POST or None)
        username = request.POST('username')
        password = request.POST('password')
        login_user = authenticate(request, username=username, password=password)

        if login_user is not None:
            login(request, login_user)
            return redirect('index')
    
    form = AuthenthecationForm()
    context ={'form' : form}
    return render(request, "registration/login.html", context)   


def mailsend(request):
    form = Emailsender()
    if request.method == 'POST':
        form = Emailsender(request.POST or None)
        subject = request.POST['subject']
        body = request.POST['body']
        from_email = request.POST['email']
        emailTo    = [settings.EMAIL_HOST_USER, 'uremail']
        send_mail(subject, body, from_email, emailTo, fail_silently=True)
        
        return render(request, "home.html")
    else:
        context = {'form' : form
        }
        return render(request, "home.html", context)

def contact(request):
    
    if request.method == 'POST':
        form = ContactForm(request.POST or None)
        body= request.POST['body']
        emailTo = settings.EMAIL_HOST_USER, 
        send_mail('Contact Person', body, emailTo, ['efezino10@gmail.com'], fail_silently=True)
        return redirect('index')
    form = ContactForm()
    context = {'form' : form}
    return render(request, 'contact.html', context)


def text_to_html(request):

    context = {'text' : text}
    return render(request, 'convert.html', context)