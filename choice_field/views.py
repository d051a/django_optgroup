from django.shortcuts import render
from choice_field.forms import StuffModelForm
from choice_field.models import Stuff
from django.views.generic import CreateView
from django.urls import reverse_lazy
# Create your views here.

'''def home(request):
	form = StuffModelForm
	template = 'home.html'

	return render(request, template, {'form': form})'''


class HomeView(CreateView):
	model = Stuff
	form_class = StuffModelForm
	template_name = 'home.html'
	success_url = reverse_lazy('choice_field:home')