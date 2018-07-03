from django.shortcuts import get_object_or_404,render, redirect
from django.utils.dateparse import parse_datetime
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.template import defaultfilters
from django.views.generic.base import View
from agenda.forms import EditAgendaForm
from agenda.models import Agenda

# Create your views here.
@login_required
def index(request):
	all_data = Agenda.objects.all()
	stu = { "agendamentos" : all_data }

	#return HttpResponse(html)
	return render(request, 'index.html', stu )

def logout(request):
	return HttpResponse('Fez logout')


def insAgenda(request):

	ins_date 		 = request.POST['dt_agenda']
	ins_hora_inicio  = request.POST['hh_inicio']
	ins_hora_fim 	 = request.POST['hh_fim']
	ins_paciente 	 = request.POST['paciente']
	ins_procedimento = request.POST['proced']

	agenda = Agenda(agd_date=ins_paciente, agd_hora_inicio=ins_hora_inicio,agd_hora_fim=ins_hora_fim,agd_paciente=ins_paciente,agd_procedimento=ins_procedimento)
	agenda.save()

	return HttpResponseRedirect('/')

def editAgenda(request):

	agenda 					= Agenda.objects.get(id=request.POST['id_agenda'])
	agenda.agd_date 		= request.POST['dt_agenda']
	agenda.agd_hora_inicio 	= request.POST['hh_inicio']
	agenda.agd_hora_fim 	= request.POST['hh_fim']
	agenda.agd_paciente 	= request.POST['paciente']
	agenda.agd_procedimento = request.POST['proced']
	agenda.save()

	return HttpResponseRedirect('/')

def delAgenda(request):

	agenda = Agenda.objects.get(id=request.POST['id_agenda']).delete()
	print("delete")

	return redirect('index')