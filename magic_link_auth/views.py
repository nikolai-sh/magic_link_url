from django.shortcuts import render

def home(request):
    return render(request, 'magic_link_auth/home.html')
