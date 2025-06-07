from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')

def login(request):
    return render(request, 'user/login.html')

def register(request):
    return render(request, 'user/register.html')

def post_property_view(request):
    return render(request, 'pages/post_property.html')