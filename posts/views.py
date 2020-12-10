from django.shortcuts import render, HttpResponse, redirect
from django.core.files.storage import FileSystemStorage

from .forms import ClothesForm
from .models import Clothes

# Create your views here.
def index(request):
    # return HttpResponse("This is Home-Page!")
    cloth = Clothes.objects.all()
    return render(request, "index.html", {"cloth": cloth})


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


def details(request):
    cloth = Clothes.objects.all()
    return render(request, "details.html", {"cloth": cloth})


def upload(request):
    # context = {}
    form = ClothesForm()
    if request.method == "POST":
        # uploaded_file = request.FILES["document"]
        # fs = FileSystemStorage()
        # name = fs.save(uploaded_file.name, uploaded_file)
        # context["url"] = fs.url(name)
        form = ClothesForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect("/")
    else:
        form = ClothesForm()
    return render(request, "upload.html", {"form": form})
