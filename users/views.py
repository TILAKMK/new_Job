from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.views.generic import CreateView, UpdateView, DetailView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import CustomUser, Profile
from .forms import CustomUserCreationForm, CustomUserChangeForm, ProfileForm

class SignUpView(CreateView):
    model = CustomUser
    form_class = CustomUserCreationForm
    template_name = 'users/register.html'
    success_url = reverse_lazy('users:login')

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'users/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('home')

@login_required
def profile_view(request):
    profile, created = Profile.objects.get_or_create(user=request.user)
    if request.method == 'POST':
        # Normalize POST data so 'experience' is an integer when possible
        data = request.POST.copy()
        exp_val = data.get('experience')
        if exp_val is not None:
            try:
                data['experience'] = int(exp_val)
            except (ValueError, TypeError):
                # If cannot convert, remove to let form validation handle it
                data.pop('experience', None)

        form = ProfileForm(data, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            # Also save phone/address to CustomUser if provided in the form
            phone = request.POST.get('phone')
            address = request.POST.get('address')
            if phone is not None:
                request.user.phone = phone
            if address is not None:
                request.user.address = address
            request.user.save()
            return redirect('users:profile')
    else:
        form = ProfileForm(instance=profile)
    return render(request, 'users/profile.html', {'form': form, 'profile': profile})

@login_required
def edit_profile_view(request):
    if request.method == 'POST':
        form = CustomUserChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('users:profile')
    else:
        form = CustomUserChangeForm(instance=request.user)
    return render(request, 'users/edit_profile.html', {'form': form})