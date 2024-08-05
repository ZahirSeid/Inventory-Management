from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile



class CreateUserForm(UserCreationForm):
    email = forms.EmailField()
    FullName = forms.CharField(max_length=100)
    phone = forms.CharField(max_length=50)
    address = forms.CharField(max_length=200)

    class Meta:
        model = User
        fields = ['username', 'email', 'FullName', 'phone', 'address', 'password1', 'password2']

    def save(self, commit=True):
        user = super(CreateUserForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
            Profile.objects.create(
                employee=user,
                FullName=self.cleaned_data['FullName'],
                phone=self.cleaned_data['phone'],
                address=self.cleaned_data['address']
            )
        return user


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['FullName', 'phone', 'address', 'image']

class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email']


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['phone', 'address', 'image']
