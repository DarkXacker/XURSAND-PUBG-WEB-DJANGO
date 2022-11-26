from django.shortcuts import redirect
from django.contrib.auth import login, authenticate
from django.views.generic import CreateView
from .forms import CustomUserCreationForm
from .models import *

class SignUpView(CreateView):
	form_class = CustomUserCreationForm
	template_name = 'registration/signup.html'
	
	def form_valid(self, form):
		form.save()
		username = form.cleaned_data.get('username')
		password = form.cleaned_data.get('password1')
		user = authenticate(username=username, password=password)
		login(self.request, user)
		return redirect('main')