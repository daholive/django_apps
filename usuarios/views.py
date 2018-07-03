from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.models import User
from django.views.generic.base import View
#from perfis.models import Perfil
from usuarios.forms import RegistrarUsuarioForm
from django.http import HttpResponse


# Create your views here.
class RegistrarUsuarioView(View):

	template_name = 'registrar.html'

	def get(self, request):
		return render(request, self.template_name)

	def post(self, request):
		form = RegistrarUsuarioForm(request.POST)

		if form.is_valid():

			dados_form = form.data

			usuario = User.objects.create_user(dados_form['nome'], dados_form['email'], dados_form['senha'])
			
			return redirect('index')

		return render(request, self.template_name, {'form' : form})