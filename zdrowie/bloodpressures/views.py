from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.forms import BaseForm, DateTimeInput
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.urls import reverse
from .forms import BloodpressureForm
from .models import BloodPressure
from django.db.models import QuerySet
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy


class BloodpressureDeleteView(SuccessMessageMixin, LoginRequiredMixin, DeleteView):
    model = BloodPressure
    # success_message = "Usunięto pomiar!"
    success_url = reverse_lazy('bloodpressures:list')


bloodpressure_delete_view = BloodpressureDeleteView.as_view()


class BloodpressureUpdateView(SuccessMessageMixin, LoginRequiredMixin, UpdateView):
    model = BloodPressure
    fields = ['systolic', 'diastolic', 'pulse', 'record_datetime', 'notes']
    success_message = "Zaktualizowano pomiar!"
    template_name = 'bloodpressures/bloodpressure_update_form.html'


bloodpressure_update_view = BloodpressureUpdateView.as_view()


class BloodpressureCreateView(SuccessMessageMixin, CreateView, LoginRequiredMixin):
    model = BloodPressure
    fields = ['systolic', 'diastolic', 'pulse', 'record_datetime', 'notes']
    success_url = reverse_lazy("bloodpressures:list")
    success_message = "Dodano wpis!"

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.fields['record_datetime'].widget = DateTimeInput(
            attrs={'type': 'datetime-local', 'class': 'form_control'}
        )
        return form

    def form_valid(self, form: BaseForm) -> HttpResponse:
        bloodpressure = form.save(commit=False)
        bloodpressure.user = self.request.user
        bloodpressure.save()
        return super().form_valid(form)


bloodpressure_create_view = BloodpressureCreateView.as_view()


class BloodpressureListView(LoginRequiredMixin, ListView):
    model = BloodPressure

    def get_queryset(self) -> QuerySet:
        queryset = self.model.objects.filter(user=self.request.user)
        return queryset


bloodpressure_list_view = BloodpressureListView.as_view()


class BloodpressureDetailView(LoginRequiredMixin, DetailView):
    model = BloodPressure

    def get_queryset(self) -> QuerySet:
        queryset = self.model.objects.filter(user=self.request.user)
        return queryset


bloodpressure_detail_view = BloodpressureDetailView.as_view()

# @login_required
# def bloodpressures_list(request):
#     bloodpressures = BloodPressure.objects.filter(user=request.user)
#     form = BloodpressureForm()
#     if request.method == "POST":
#         form = BloodpressureForm(request.POST)
#         if form.is_valid():
#             instance = form.save(commit = False)
#             instance.user = request.user
#             instance.save()
#             messages.add_message(request, messages.INFO, 'działa?')
#             return HttpResponseRedirect(reverse('bloodpressures:list'))
#     return render(request, "bloodpressures/bloodpressure_list.html", {'bloodpressures':bloodpressures, "form":form})
#
# @login_required
# def bloodpressures_details(request, bp_id):
#     bloodpressure = BloodPressure.objects.get(user=request.user, pk=bp_id)
#     form = BloodpressureForm(instance=bloodpressure)
#     if request.method == "POST":
#         form = BloodpressureForm(request.POST, instance=bloodpressure)
#         if form.is_valid():
#             form.save()
#     return render(request, "bloodpressures/bloodpressure_detail.html", {'bloodpressure':bloodpressure, 'form':form})
