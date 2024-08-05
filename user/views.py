from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import CreateUserForm, UserUpdateForm, ProfileUpdateForm
from django.contrib.auth import login, logout

def register(request):
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Ensure `login` is imported
            return redirect('user-profile')  # Adjust the URL name as needed
    else:
        form = CreateUserForm()
    
    context = {
        'form': form,
    }
    return render(request, 'user/register.html', context)


@login_required
def profile(request):
    # Ensure the profile information is included in the context
    context = {
        'user': request.user,
        'profile': request.user.profile  # Directly access the profile
    }
    return render(request, 'user/profile.html', context)


@login_required
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
    # Redirect to a default page or any other page
    return redirect('/')