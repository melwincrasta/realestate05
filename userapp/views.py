
# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import BuyerRegisterForm, SellerRegisterForm,LoginForm
from sellerapp.models import Property
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login as auth_login, authenticate
from django.contrib import messages


def buyer_register(request):
    if request.method == 'POST':
        form = BuyerRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful as a Buyer!")
            return redirect('buyer_dashboard')
    else:
        form = BuyerRegisterForm()

    return render(request, 'userapp/register.html', {'form': form})

# View for Seller Registration
def seller_register(request):
    if request.method == 'POST':
        form = SellerRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful as a Seller!")
            return redirect('seller_dashboard')
    else:
        form = SellerRegisterForm()

    return render(request, 'userapp/register.html', {'form': form})


@login_required
def buyer_dashboard(request):
    if request.user.user_type == 'seller':
        return redirect('seller_dashboard')
    elif request.user.user_type == 'buyer':
        properties = Property.objects.all()
        return render(request, 'userapp/buyer_dashboard.html', {'properties': properties})
    return render(request, 'userapp/buyer_dashboard.html')


from django.shortcuts import render, get_object_or_404
# Product Detail View
@login_required
def property_detail(request, property_id):
    # Get the product by ID or return a 404 error if not found
    property = get_object_or_404(Property, id=property_id)
    
    # Render the product details page with the product information
    return render(request, 'userapp/property_detail.html', {'property': property})


def home(request):
    return render(request, 'userapp/home.html')


def user_login(request):
    form = LoginForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(request, username=username, password=password)
            if user is not None:
                # Log the user in
                auth_login(request, user)

                # Check if the user is a seller or buyer
                if user.user_type == 'seller':
                    return redirect("seller_dashboard")  # Redirect to seller's dashboard
                elif user.user_type == 'buyer':
                    return redirect("buyer_dashboard")  # Redirect to buyer's dashboard
                else:
                    return redirect("home")  # Default redirect if user_type is neither

            else:
                messages.error(request, "Invalid username or password")
    
    return render(request, "userapp/login.html", {"form": form})



from django.shortcuts import redirect
from django.contrib.auth import logout

def user_logout(request):
    # Log out the user
    logout(request)
    # Redirect to the home page or login page after logging out
    return redirect('home')  # Or 'login' if you want to redirect to the login page

