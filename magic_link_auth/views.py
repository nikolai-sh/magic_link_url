from django.shortcuts import redirect, render
from .forms import UserRegisterForm
from django.contrib import messages

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
