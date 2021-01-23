$( document ).ready(function() {
  
    //Codificação referente a listagem de Colaboradores
    $("#link_listar_colaboradores").click(function(){
        
        $.ajax({
            url:'http://localhost:5000/listar_colaboradores',
            method:'GET',
            dataType:'json', // os dados são recebidos no formato json
            success:listar_colaboradores, // chama a função listar_colaboradores para processar o resultado
            error: function() {
                alert("erro ao ler dados, verifique o backend");
            }
        });

        function listar_colaboradores(colaboradores){
        linhas = ""
        for(var i in colaboradores){
            lin = 
                "<tr>" +
                "<th>"+colaboradores[i].id+"</th>"+
                "<td>"+colaboradores[i].nome+"</td>"+
                "<td>"+colaboradores[i].email+"</td>"+
                "<td>"+colaboradores[i].telefone+"</td>"+
                "<td>"+colaboradores[i].salario+"</td>"
                "</tr>"
                linhas = linhas + lin;
        }
        $("#corpoTabelaColaboradores").html(linhas);

        $("#conteudoInicialColaboradores").addClass("invisible");
        $("#tabelaColaboradores").addClass("invisible");

        $("#tabelaColaboradores").removeClass("invisible");
        
        }
        
    });

    $("#btn_incluir_colaborador").click(function(){
        if($("#id_colaboradores").val()==""|| $("#nome_colaboradores").val()=="" || $("#email_colaboradores").val()==""
        ||$("#telefone_colaboradores").val()==""|| $("#salario_colaboradores").val()==""){
            alert("Favor preencher todos os dados!")
        }else{
            
        
            id_colaboradores = $("#id_colaboradores").val();
            nome_colaboradores = $("#nome_colaboradores").val();
            email_colaboradores = $("#email_colaboradores").val();
            telefone_colaboradores = $("#telefone_colaboradores").val();
            salario_colaboradores = $("#salario_colaboradores").val();

            dados = JSON.stringify({id : id_colaboradores, nome : nome_colaboradores, email : email_colaboradores,
                telefone : telefone_colaboradores, salario : salario_colaboradores});

            $.ajax({
                url: 'http://localhost:5000/incluir_colaborador',
                type : 'POST',
                contentType : 'application/json',
                dataType: 'json',
                data: dados,
                success: incluirColaborador,
                error: erroIncluirColaborador
            })
            function incluirColaborador(resposta) {
                if (resposta.resultado =="ok"){
                
                alert("Colaborador Incluido");
                $("#id_colaboradores").val("");
                $("#nome_colaboradores").val("");
                $("#email_colaboradores").val("");
                $("#telefone_colaboradores").val("");
                $("#salario_colaboradores").val("");
                }else{
                    alert("Erro na chamada BackEnd");
                }
            }
            function erroIncluirColaborador(resposta){
                alert("Erro na chamada Backend");

                
            }
        }
       });
});