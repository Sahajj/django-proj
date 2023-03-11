from django.shortcuts import render

# Create your views here.
def index(request):
    render(request, 'index.html')

def login(request):
    render(request, 'login.html')

def logout(request):
    render(request, 'index.html')

#  pass of user Sahaj@2702