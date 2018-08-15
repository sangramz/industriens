from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .models import CompanyInfo
from .forms import CompanyInfoForm

# index here
def index(request):
    return render(request, 'in/index.html')

def login(request):
    return render(request, 'in/login.html')

#               -------- Registeration ---------

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()

    return render(request, 'in/registration.html', { 'form' : form })

#               -------- Registeration ---------

#               -------- KUNDE PAGE FUNCTIONALITY ---------

def kunde(request):
    if request.method == 'POST':
        form = CompanyInfoForm(request.POST)
        if form.is_valid():
            new_company = CompanyInfo(name=request.POST['name'], address=request.POST['address'],
                            postnr=request.POST['postnr'], by=request.POST['by'], tlf=request.POST['tlf'],
                            email=request.POST['email'], bank=request.POST['bank'], regnr=request.POST['regnr'], kontonr=request.POST['kontonr'])
            new_company.save()
            return redirect('kunde')

    else:
        form = CompanyInfoForm()

    info = CompanyInfo.objects.all()
    return render(request, 'in/kunde.html', { 'info' : info, 'form' : form })

#               -------- KUNDE PAGE FUNCTIONALITY ---------


#               -------- kontakt ---------

def kontakt(request):
    return render(request, 'in/kontakt.html')

#               -------- kontakt ---------


#               -------- betal ---------

def betal(request):
        return render(request, 'in/betal.html')

#               -------- betal ---------


#               -------- afdrag ---------

def afdrag(request):
        return render(request, 'in/afdrag.html')

#               -------- afdrag ---------
