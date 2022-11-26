
from django.utils.translation import gettext_lazy as _
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse
from django.views import View
from django.views.generic import (
    DetailView,
    RedirectView,
    UpdateView,
    ListView,
    CreateView,
)







User = get_user_model()


class UserCreateView(SuccessMessageMixin, CreateView):
    model = User
    fields = ['first_name', 'last_name', 'bio']
    # template_name_suffix = '_form'

user_create_view = UserCreateView.as_view()




class UserListView(ListView):
    model = User
    template_name = 'users/user_list.html'

    def get(self, request):
        user_list = self.model.objects.all()
        return render(request, self.template_name, {'user_list' : user_list})

user_list_view = UserListView.as_view()

class UserCounterView(View):
    model = User
    template_name = 'users/counter.html'

    def get(self, request):
        users_counter = self.model.objects.count()
        return render(request, self.template_name, {'users_counter': users_counter})

user_counter_view = UserCounterView.as_view()


class UserDetailView(SuccessMessageMixin, LoginRequiredMixin, DetailView):
    model = User
    # These Next Two Lines Tell the View to Index
    #   Lookups by Username
    slug_field = "username"
    slug_url_kwarg = "username"



user_detail_view = UserDetailView.as_view()


class UserUpdateView(SuccessMessageMixin, LoginRequiredMixin, UpdateView):
    fields = [
        "name",
        "bio",
    ]
    success_url = '/success/'
    success_message = _("Update successfully")

    # We already imported user in the View code above,
    #   remember?
    model = User






    # Send the User Back to Their Own Page after a
    #   successful Update
    def get_success_url(self):
        return reverse(
            "users:detail",
            kwargs={'username': self.request.user.username},
        )

    def get_object(self):
        # Only Get the User Record for the
        #   User Making the Request
        return User.objects.get(
            username=self.request.user.username
        )


user_update_view = UserUpdateView.as_view()


class UserRedirectView(LoginRequiredMixin, RedirectView):
    permanent = False

    def get_redirect_url(self):
        return reverse(
            "users:detail",
            kwargs={"username": self.request.user.username},
        )


user_redirect_view = UserRedirectView.as_view()
