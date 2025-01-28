from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Clientes
from .forms import ClienteForm

class ClienteListView(ListView):
    model = Clientes
    template_name = 'Cliente_list.html'
    context_object_name = 'Clientes'

class ClienteCreateView(CreateView):
    model = Clientes
    form_class = ClienteForm
    template_name = 'Cliente_form.html'
    success_url = reverse_lazy('Cliente_list')

class ClienteUpdateView(UpdateView):
    model = Clientes
    form_class = ClienteForm
    template_name = 'Cliente_form.html'
    success_url = reverse_lazy('Cliente_list')

class ClienteDeleteView(DeleteView):
    model = Clientes
    template_name = 'Cliente_confirm_delete.html'
    success_url = reverse_lazy('Cliente_list')