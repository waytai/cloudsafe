from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'webui/index.html')
def faq(request):
    return render(request,'webui/faq.html')
def about(request):
    return render(request,'webui/about.html')
