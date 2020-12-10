from django.shortcuts import render, HttpResponse, redirect

# Create your views here.
def index(request):
    # return HttpResponse("This is Home-Page!")
    context = {"variable": "this is sent"}
    return render(request, "index.html", context)


def aboutus(request):
    return render(request, "aboutus.html")
    # return HttpResponse("This is About-us Page!")


def services(request):
    return render(request, "services.html")
    # return HttpResponse("This is Services Page!")


def contacts(request):
    # return render(request, "index.html")
    return HttpResponse("This is Contacts Page!")


def user(request):
    return render(request, "user.html")
