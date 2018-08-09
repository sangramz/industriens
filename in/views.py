from django.shortcuts import render, redirect
from .models import company_info
from .forms import virkomshedinfo

# Create your views here.
def index(request):
    return render(request, 'in/index.html')

def login(request):
    return render(request, 'in/login.html')

def kunde(request):
    if request.method == 'POST':
        company_info_form = virkomshedinfo(request.POST)

        if company_info_form.is_valid():
            new_company = company_info(name = request.POST['firm_name'],
                                        address = request.POST['address'])
            return redirect('kunde')

    else:
        company_info_form = virkomshedinfo()



    Company_info = company_info.objects.order_by('id')
    context = { 'Company_info' : Company_info, 'company_info_form' : company_info_form }
    return render(request, 'in/kunde.html', context)
