from django.contrib import messages
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.urls import reverse
from .forms import GlucoseForm
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Glucose
from django.db.models import QuerySet
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from django.forms import BaseForm, DateTimeInput
from django.http import HttpResponseRedirect, HttpResponse


# Create your views here.

class GlucoseDeleteView(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    model = Glucose
    success_url = reverse_lazy('glucoses:list')
glucose_delete_view = GlucoseDeleteView.as_view()


class GlucoseUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Glucose
    fields = ['value', 'record_datetime', 'notes']
    success_message = "Zaktualizowano pomiar!"
    template_name = 'glucoses/glucose_update_form.html'

glucose_update_view = GlucoseUpdateView.as_view()


class GlucoseCreateView(CreateView, SuccessMessageMixin, LoginRequiredMixin):
    model = Glucose
    fields = ['value', 'record_datetime', 'notes']
    success_url = reverse_lazy("glucoses:list")
    success_message = "Dodano pomiar!"

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.fields['record_datetime'].widget = DateTimeInput(
            attrs = { 'type': 'datetime-local', 'class' : 'form_control'}
        )
        return form

    def form_valid(self, form : BaseForm) -> HttpResponse:
        glucose = form.save(commit=False)
        glucose.user = self.request.user
        glucose.save()
        return super().form_valid(form)

glucose_create_view = GlucoseCreateView.as_view()

class GlucoseListView(LoginRequiredMixin, ListView):
    model = Glucose

    def get_queryset(self) -> QuerySet:
        queryset = self.model.objects.filter(user=self.request.user)
        return queryset

glucose_list_view = GlucoseListView.as_view()

class GlucoseDetailView(LoginRequiredMixin, DetailView):
    model = Glucose

glucose_detail_view = GlucoseDetailView.as_view()


# @login_required
# def glucoses_list(request):
#     glucose = Glucose.objects.filter(user=request.user)
#     form = GlucoseForm()
#     if request.method == "POST":
#         form = GlucoseForm(request.POST)
#         if form.is_valid():
#             instance = form.save(commit = False)
#             instance.user = request.user
#             instance.save()
#             return HttpResponseRedirect(reverse('glucoses:list'))
#             messages.add_message(request, messages.INFO, 'działa ?')
#     return render(request, "glucoses/bloodpressure_list.html", {'glucose':glucose, 'form':form})
#
#
# @login_required
# def glucoses_details(request, bp_id):
#     glucose = Glucose.objects.get(user=request.user, pk=bp_id)
#     form = GlucoseForm(instance=glucose)
#     if request.method == "POST":
#         form = GlucoseForm(request.POST, instance=glucose)
#         if form.is_valid():
#             form.save()
#     return render(request, "glucoses/bloodpressure_detail.html", {'glucose':glucose, 'form':form})

