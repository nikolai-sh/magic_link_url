from .models import User
from django.contrib import messages
from .services import get_magic_link
from django.shortcuts import redirect, render
from .forms import UserRegisterForm, EmailForm
from django.core.mail import send_mail, BadHeaderError

def home(request):
    return render(request, 'magic_link_auth/home.html')


def register(request):
    """ Function to register new user """

    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email')
            messages.success(request, f'Created new user {email}!')
            return redirect('send-magic-link')
    else:
        form = UserRegisterForm()
    return render(request, 'magic_link_auth/register.html', {'form': form})


def send_magic_link(request):
    """
    Function to send magic link url
    """
    subject = 'Login'
    scheme = request.scheme 
    host = request.get_host()

    if request.method == 'GET':
        email_form = EmailForm()
    else:
        email_form = EmailForm(request.POST)
        if email_form.is_valid():
            email = email_form.cleaned_data['email']
            try:
                user = User.objects.get(email__exact=email)
                magic_link = get_magic_link(user, scheme, host)
                send_mail(subject=subject, 
                          message=magic_link, 
                          from_email=None,
                          recipient_list=[email]
                          )
                messages.success(request, 'Success! Check your inbox.')
            except User.DoesNotExist:
                messages.error(request, 'Write correct email or register')
                return redirect('send-magic-link')
            except BadHeaderError:
                messages.error(request, 'Invalid header found.')
                return redirect('send-magic-link')
            return redirect('home')

    return render(request, "magic_link_auth/send_magic_link_form.html", {'form': email_form})
