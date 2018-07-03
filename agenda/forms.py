from django import forms
from django.db import models
#from django.contrib.auth.models import User

class EditAgendaForm(forms.Form):

	id = 11111111
	date = models.DateField(null=False)
	hora_inicio = models.TimeField(null=False)
	hora_fim = models.TimeField(null=False)
	paciente = models.CharField(max_length=255, null=False)
	procedimento = models.CharField(max_length=255, null=False)


	