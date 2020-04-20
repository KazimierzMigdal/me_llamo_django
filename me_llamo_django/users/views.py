from .forms import ProfileUpdateForm, UserRegisterForm, UserUpdateForm
from django import forms
from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import PasswordResetView, PasswordResetConfirmView
from django.shortcuts import render, redirect


class MyPasswordResetView(PasswordResetView):
    def get_form(self, form_class=None):
        if form_class is None:
            form_class = self.get_form_class()
        form = super(MyPasswordResetView, self).get_form(form_class)
        form.fields['email'].widget = forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Email'})
        form.fields['email'].lable = ''
        return form

class MyPasswordResetConfirmView(PasswordResetConfirmView):
    def get_form(self, form_class=None):
        if form_class is None:
            form_class = self.get_form_class()
        form = super(MyPasswordResetConfirmView, self).get_form(form_class)
        form.fields['new_password1'].widget = forms.PasswordInput()
        form.fields['new_password1'].label = False
        form.fields['new_password1'].help_text = None
        form.fields['new_password2'].widget = forms.PasswordInput()
        form.fields['new_password2'].label = False
        form.fields['new_password2'].help_text = None
        return form

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Konto dla {username} zostało założone! Witamy w Me llamo Django!')
            login(request, user)
            return redirect('home')
    else:
        form = UserRegisterForm()
    return render(request,'users/register.html', {'form': form})


@login_required
def profile_edit(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST,
                                instance=request.user)
        p_form = ProfileUpdateForm(request.POST,
                                    request.FILES,
                                    instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Twój profil został zaktualizowany')
            return redirect('home')
        else:
            print(u_form.errors)
            print(p_form.errors)
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)
    context = {
        'u_form': u_form,
        'p_form': p_form,
    }
    return render(request, 'users/profile_edit.html', context)
