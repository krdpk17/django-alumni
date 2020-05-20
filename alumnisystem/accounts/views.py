from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.urls import reverse_lazy
from django.views import generic
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.views.generic.edit import UpdateView
from django.contrib import messages
from .forms import SignUpForm, UserProfileForm, EditUserProfileForm, ProfileChangeForm

class UpdateProfile(UpdateView):
    success_url = reverse_lazy('update')
    template_name = 'account_update.html'
    form_class = ProfileChangeForm
    form_profile = EditUserProfileForm

    def get(self, request):
        form = ProfileChangeForm(instance=request.user)
        user_profile_form = EditUserProfileForm(instance=request.user.userprofile)
        context = {'form': form, 'profile_form': user_profile_form}
        return render(request, self.template_name, context)   

    def post(self, request):
        form = self.form_class(request.POST, instance=request.user)
        profile_form = self.form_profile(request.POST, instance=request.user.userprofile)
        context = {'form': form, 'profile_form': profile_form}
        if form.is_valid() and profile_form.is_valid():
            form.save()
            profile_form.save()
            messages.success(request, 'Form submission successful')
            return redirect('update')
                
        return render(request, self.template_name, context)


class SignUp(generic.CreateView):
    success_url = reverse_lazy('login')
    template_name = 'signup.html'
    form_class = SignUpForm
    form_profile = UserProfileForm

    #Display blank form
    def get(self, request):
        form = self.form_class(None)
        profile_form = self.form_profile()
        context = {'form': form, 'profile_form': profile_form}
        return render(request, self.template_name, context)

    #Process form data
    def post(self, request):
        form = self.form_class(request.POST)
        profile_form = self.form_profile(request.POST)
        context = {'form': form, 'profile_form': profile_form}
        if form.is_valid() and profile_form.is_valid():
            user = form.save(commit=False)

            # Cleaned (normalized) data
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user.set_password(password)
            user.save()

            user_profile = profile_form.save(commit=False)
            user_profile.user = user
            user_profile.save()

            # Returns User objects if credential are correct
            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('update')
                    
        return render(request, self.template_name, context)
