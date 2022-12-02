from django.shortcuts import render, redirect
from django.views.generic import TemplateView, CreateView, UpdateView, DetailView, ListView, DeleteView
from django.urls import reverse, reverse_lazy
from django.utils.translation import gettext_lazy as _
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from client.forms import UserForm, UserInfoForm


@login_required
def userSettings(request):
    template_name = 'client/settings.html'
    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=request.user)
        info_form = UserInfoForm(request.POST, instance=request.user.profile)
        if user_form.is_valid() and info_form.is_valid():
            user_form.save()
            info_form.save()
            messages.success(request, _(
                "Your information has been successfully updated"))
            # TODO: add notofication on update user info
            # sender = request.user
            # recipient = User.objects.filter(is_superuser=True)
            # message = _('New cusomer account is waiting for confirmation')
            # notify.send(sender=sender, recipient=recipient, verb='Message',
            # description='New cusomer account is waiting for confirmation', level='light')
            return redirect('dashboard')
    else:
        user_form = UserForm()
        info_form = UserInfoForm()
    if request.method == 'GET':
        user_form = UserForm(instance=request.user)
        info_form = UserInfoForm(instance=request.user.profile)
    context = {
        'user_form': user_form,
        'info_form': info_form
    }
    return render(request, template_name, context)


class UserProfile(TemplateView):
    template_name = 'client/profile.html'


class CustomerListView(LoginRequiredMixin, SuccessMessageMixin, ListView):
    template_name = 'client/admin/list.html'
    model = User


class CustomerDelete(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    model = User
    success_message = _('Customer has been successfully deleted')