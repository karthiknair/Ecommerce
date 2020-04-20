from django.shortcuts import render, HttpResponse,redirect
from products.models import Product
from django.views.generic import ListView
from django.contrib.auth.forms import AuthenticationForm

class Home(ListView):
    model = Product
    context_object_name="all_products"
    template_name = 'products/home.html'


def login_view(request):
    
    if request.method=='POST':
        form=AuthenticationForm(data=request.POST)
        if form.is_valid:
            return redirect('mainapp:home')

    else:
        form=AuthenticationForm
    return render(request, 'products/login.html', {'form':form})