from django.db import models

# Create your models here.
#class Paciente(models.Model):

#	nome = models.CharField(max_length=255, null=False)
#	idade = models.DecimalField(max_digits=5, null=False, decimal_places=3)
#	telefone = models.CharField(max_length=255, null=False)
#	email = models.EmailField()

class Agenda(models.Model):

	agd_date = models.CharField(max_length=255, null=False)
	agd_hora_inicio = models.CharField(max_length=255, null=False)
	agd_hora_fim = models.CharField(max_length=255, null=False)
	agd_paciente = models.CharField(max_length=255, null=False)
	agd_procedimento = models.CharField(max_length=255, null=False)

	def get_date(self):
		return self.agd_date


