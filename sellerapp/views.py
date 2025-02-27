

# Create your views here.
# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
from .models import Property
from .forms import PropertyForm

"""@login_required
def seller_dashboard(request):
    if request.user.user_type != 'seller':
        return HttpResponseForbidden()
    products = request.user.products.all()
    return render(request, 'sellerapp/seller_dashboard.html', {'products': products})

"""
def home(request):
    properties = Property.objects.all()
    return render (request, 'sellerapp/home.html',{'properties': properties}) 

# FUNCTION DEFENITION FOR PAGE1.HTML
def about(request):
     return render(request, 'sellerapp/about.html')

#  # FUNCTION DEFENITION FOR PAGE2.HTML
def contact(request):
     return render(request, 'sellerapp/contact.html')
def testimonial(request):
    return render(request, 'sellerapp/testimonial.html')

def property(request):
    properties=Property.objects.all() #calling the product from modelclass product
    return render(request,"sellerapp/property.html",{'properties':properties})




@login_required
def seller_dashboard(request):
    if request.user.user_type != 'seller':
        return HttpResponseForbidden("You are not authorized to view this page")
    
    properties = request.user.properties.all()
    return render(request, 'sellerapp/seller_dashboard.html', {'properties': properties})


@login_required

def add_property(request):
    if request.user.user_type != 'seller':
        return HttpResponseForbidden()
    if request.method == 'POST':
        form = PropertyForm(request.POST,request.FILES)#request.FILES used for image handling. 
        if form.is_valid():
            property = form.save(commit=False)
            property.seller = request.user
            property.save()
            return redirect('seller_dashboard')
    else:
        form = PropertyForm()
    return render(request, 'sellerapp/add_property.html', {'form': form})

@login_required
def edit_property(request, pk):
    property = get_object_or_404(Property, pk=pk, seller=request.user)
    if request.method == 'POST':
        form = PropertyForm(request.POST, request.FILES, instance=property)
        if form.is_valid():
            form.save()
            return redirect('seller_dashboard')
    else:
        form = PropertyForm(instance=property)
    return render(request, 'sellerapp/edit_property.html', {'form': form})

@login_required
def delete_property(request, pk):
    property = get_object_or_404(Property, pk=pk, seller=request.user)
    if request.method == 'POST':
        property.delete()
        return redirect('seller_dashboard')
    return render(request, 'sellerapp/delete_property.html', {'property': property})
