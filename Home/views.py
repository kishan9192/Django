from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    context = {
        "variable" : "this is sent"
    }
    return render(request, 'index.html', context)
    #return HttpResponse("This is Homepage")

def about(request):
    return HttpResponse("This is About Page")

def services(request):
    return HttpResponse("This is a service Page")
    
def contact(request):
    return HttpResponse("This is a contact Page")