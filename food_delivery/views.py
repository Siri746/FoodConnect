from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from food_delivery.forms import SignUpForm  # Absolute import
from food_delivery.models import Profile, FoodRequest, SellerItem

def landing_page(request):
    if request.method == 'POST':
        role = request.POST.get('role')
        request.session['role'] = role
        return redirect('signup')
    return render(request, 'food_delivery/landing.html')

def signup(request):
    role = request.session.get('role')
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            profile = Profile(
                user=user,
                role=role,
                name=form.cleaned_data['name'],
                mobile=form.cleaned_data['mobile'],
                email=form.cleaned_data['email'],
                address=form.cleaned_data['address'],
                date_of_birth=form.cleaned_data['date_of_birth'],
                expected_salary=form.cleaned_data['expected_salary']
            )
            profile.save()
            login(request, user)
            return redirect('dashboard')
    else:
        form = SignUpForm()
    return render(request, 'food_delivery/signup.html', {'form': form, 'role': role})

@login_required
def dashboard(request):
    profile = Profile.objects.get(user=request.user)
    if profile.role == 'customer':
        if request.method == 'POST':
            description = request.POST.get('description')
            contact_number = request.POST.get('contact_number')
            FoodRequest.objects.create(customer=profile, description=description, contact_number=contact_number)
        return render(request, 'food_delivery/dashboard.html', {'profile': profile, 'requests': FoodRequest.objects.filter(customer=profile)})
    elif profile.role == 'delivery_boy':
        requests = FoodRequest.objects.filter(status='pending')
        if request.method == 'POST':
            request_id = request.POST.get('request_id')
            food_request = FoodRequest.objects.get(id=request_id)
            food_request.delivery_boy = profile
            food_request.status = 'accepted'
            food_request.save()
        return render(request, 'food_delivery/dashboard.html', {'profile': profile, 'requests': requests})
    elif profile.role == 'seller':
        if request.method == 'POST':
            item_name = request.POST.get('item_name')
            description = request.POST.get('description')
            image = request.FILES.get('image')
            SellerItem.objects.create(seller=profile, item_name=item_name, description=description, image=image)
        return render(request, 'food_delivery/dashboard.html', {'profile': profile, 'items': SellerItem.objects.filter(seller=profile)})
