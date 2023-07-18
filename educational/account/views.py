from django.contrib import messages
from django.contrib.auth import authenticate, logout, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView, PasswordChangeView
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView

from .forms import CustomUserCreationForm, LoginUserForm, UpdateUserForm
from .models import CustomUser


class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('entrance')
    template_name = 'registration/registration.html'

    def registration(request):
        form = None
        if request.method == 'POST':
            form = CustomUserCreationForm(request.POST)
            email = request.POST.get('email')
            if CustomUser.objects.filter(email=email).exists():
                messages.error(request, 'Данная почта уже используется!')
            else:
                if form.is_valid():
                    ins = form.save()
                    username = form.cleaned_data['username']
                    password = form.cleaned_data['password1']

                    user = authenticate(username=username, password=password, email=email)
                    ins.email = email
                    ins.save()
                    form.save_m2m()
                    messages.success(request, 'Регистрация прошла успешно')
                    return redirect('entrance')

        else:
            form = CustomUserCreationForm()

        context = {'form': form}
        return render(request, 'registration/registration.html', context)


class LoginUser(LoginView):
    form_class = LoginUserForm
    template_name = 'entrance/entrance.html'


def account(request):
    return render(request, 'profile/profile.html')


@login_required
def profile(request):
    if request.method == 'POST':
        user_form = UpdateUserForm(request.POST, instance=request.user)

        if user_form.is_valid():
            user_form.save()
            messages.success(request, 'Изменения в профиле сохранены.')
            return redirect('profile')
        if not (user_form.is_valid()):
            messages.error(request, 'Введенные данные некорректны!')
    else:
        user_form = UpdateUserForm(instance=request.user)

    return render(request, 'profile/profile-changed.html', {'user_form': user_form})
