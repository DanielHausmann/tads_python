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
    // Codificação referente a inserção de Colaboradores
    $("#btn_incluir_colaborador").click(function(){
        //Verifica se algum valor esta vazio
        if($("#id_colaboradores").val()==""|| $("#nome_colaboradores").val()=="" || $("#email_colaboradores").val()==""
        ||$("#telefone_colaboradores").val()==""|| $("#salario_colaboradores").val()==""){
            alert("Favor preencher todos os dados!")
        }else{
            //obtem os dados do formulário
            id_colaboradores = $("#id_colaboradores").val();
            nome_colaboradores = $("#nome_colaboradores").val();
            email_colaboradores = $("#email_colaboradores").val();
            telefone_colaboradores = $("#telefone_colaboradores").val();
            salario_colaboradores = $("#salario_colaboradores").val();
            
            // prepara os dados para o envio em json
            dados = JSON.stringify({id : id_colaboradores, nome : nome_colaboradores, email : email_colaboradores,
                telefone : telefone_colaboradores, salario : salario_colaboradores});

            //manda para o back-end
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
                //mensagem de sucesso
                alert("Colaborador Incluido");
                //limpa todos os valores dos campos do formulário
                $("#id_colaboradores").val("");
                $("#nome_colaboradores").val("");
                $("#email_colaboradores").val("");
                $("#telefone_colaboradores").val("");
                $("#salario_colaboradores").val("");
                }else{
                    //mensagem caso ocorra algum erro de comunicação
                    alert("Erro na Comunicação");
                }
            }
            function erroIncluirColaborador(resposta){
                //mensagem caso ocorra algum erro na requisição back-end
                alert("Erro na chamada Backend");

                
            }
        }
       });
});