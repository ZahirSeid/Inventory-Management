from django.shortcuts import render, redirect
from django.contrib.auth.models import Group
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout
from .forms import CreateUserForm, UserUpdateForm, ProfileUpdateForm

def register(request):
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()

            # Get or create the 'Customers' group
            group, created = Group.objects.get_or_create(name='Customers')
            user.groups.add(group)

            # Log the user in after successful registration
            login(request, user)
            return redirect('user-profile')
    else:
        form = CreateUserForm()

    context = {
        'form': form
    }
    return render(request, 'user/register.html', context)

def profile(request):
    context = {}
    return render(request, 'user/profile.html', context)

def profile_update(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            return redirect('user-profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form,
    }
    return render(request, 'user/profile_update.html', context)

def custom_logout(request):
    logout(request)
    return redirect('/')
