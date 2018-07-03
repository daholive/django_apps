

$(document).ready(function(){
    $("#novaAgenda").click(function(event){
        $("#myModalCad").modal({backdrop: true});
        event.preventDefault();
	});
});


$(document).ready(function(){
	$("#salvarCad").click(function(event){

		data_agenda 		= $("#modal_data_cad").val();
	    hora_inicio_agenda  = $("#modal_hora_inicio_cad").val();
	    hora_fim_agenda 	= $("#modal_hora_fim_cad").val();
	    paciente_agenda 	= $("#modal_paciente_cad").val();
	    procedimento_agenda = $("#modal_procedimento_cad").val();
    	token               = $("#token").val();

    	$.ajax({
	    	method: "POST",
	    	url: "insAgenda/",
	    	data: {
	    		csrfmiddlewaretoken:token,
	    		dt_agenda:data_agenda,
	    		hh_inicio:hora_inicio_agenda,
	    		hh_fim:hora_fim_agenda,
	    		paciente:paciente_agenda,
	    		proced:procedimento_agenda
	    	}
	    }).done(function() {
		    window.location='/'
		}).fail(function() {
		    console.log('error')
		})
	});
});


$(document).ready(function(){
    $(".fa-edit").click(function(event){
        $("#myModal").modal({backdrop: true});
        event.preventDefault();

        tr = ((event.target.parentNode).parentNode)
		td = event.target.parentNode.className

		data_agenda			= tr.querySelector("#data").textContent;
	    hora_inicio_agenda	= tr.querySelector("#hora_inicio").textContent;
	    hora_fim_agenda		= tr.querySelector("#hora_fim").textContent;
	    paciente_agenda		= tr.querySelector("#paciente").textContent;
	    procedimento_agenda = tr.querySelector("#procedimento").textContent;
	    id 					= event.target.id;

	    $("#modal_data").val(data_agenda);
	    $("#modal_hora_inicio").val(hora_inicio_agenda);
	    $("#modal_hora_fim").val(hora_fim_agenda);
	    $("#modal_paciente").val(paciente_agenda);
	    $("#modal_procedimento").val(procedimento_agenda);
	    $("#codigo").val(id);
	    
    });
});


$(document).ready(function(){
	$("#salvar").click(function(event){

		data_agenda 		= $("#modal_data").val();
	    hora_inicio_agenda  = $("#modal_hora_inicio").val();
	    hora_fim_agenda 	= $("#modal_hora_fim").val();
	    paciente_agenda 	= $("#modal_paciente").val();
	    procedimento_agenda = $("#modal_procedimento").val();
    	codigo              = $("#codigo").val();
    	token               = $("#token").val();

	    $.ajax({
	    	method: "POST",
	    	url: "editAgenda/",
	    	data: {
	    		csrfmiddlewaretoken:token,
	    		id_agenda:codigo,
	    		dt_agenda:data_agenda,
	    		hh_inicio:hora_inicio_agenda,
	    		hh_fim:hora_fim_agenda,
	    		paciente:paciente_agenda,
	    		proced:procedimento_agenda
	    	}
	    }).done(function() {
		    window.location='/'
		}).fail(function() {
		    console.log('error')
		})
	});
});


$(document).ready(function(){
	$(".fa-trash").click(function(event){

		tr = ((event.target.parentNode).parentNode)
		td = event.target.parentNode.className

    	codigo = event.target.id;
    	token  = $("#token").val();

		if(confirm("Deseja deletar este agendamento?")){

		   $.ajax({
		    	method: "POST",
		    	url: "delAgenda/",
		    	data: {
		    		csrfmiddlewaretoken:token,
		    		id_agenda:codigo
		    	}
		    }).done(function() {
			    window.location='/'
			}).fail(function() {
			    console.log('error')
			})
		}
	});
});
