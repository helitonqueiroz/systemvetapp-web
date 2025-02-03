from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Clientes
from .forms import ClienteForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

class ClienteListView(LoginRequiredMixin, ListView):
    model = Clientes
    template_name = 'Cliente_list.html'
    context_object_name = 'Clientes'

class ClienteCreateView(LoginRequiredMixin, CreateView):
    model = Clientes
    form_class = ClienteForm
    template_name = 'Cliente_form.html'
    success_url = reverse_lazy('Cliente_list')

class ClienteUpdateView(LoginRequiredMixin, UpdateView):
    model = Clientes
    form_class = ClienteForm
    template_name = 'Cliente_form.html'
    success_url = reverse_lazy('Cliente_list')

class ClienteDeleteView(LoginRequiredMixin, DeleteView):
    model = Clientes
    template_name = 'Cliente_confirm_delete.html'
    success_url = reverse_lazy('Cliente_list')