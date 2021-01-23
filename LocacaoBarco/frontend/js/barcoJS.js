$( document ).ready(function() {


    
    // Codificação referente a listagem de Barcos
    $("#link_listar_barcos").click(function(){
    
        $.ajax({
            url:'http://localhost:5000/listar_barcos',
            method:'GET',
            dataType:'json', // os dados são recebidos no formato json
            success:listar_barcos, // chama a função listar_barcos para processar o resultado
            error: function() {
                alert("erro ao ler dados, verifique o backend");
            }
        });

        function listar_barcos(barcos){
           linhas = ""
           for(var i in barcos){
               lin = 
                "<tr>" +
                "<th>"+barcos[i].id+"</th>"+
                "<td>"+barcos[i].tipo+"</td>"+
                "<td>"+barcos[i].cor+"</td>"+
                "<td>"+barcos[i].ano+"</td>"
                "</tr>"
                linhas = linhas + lin;
           }
           $("#corpoTabelaBarcos").html(linhas);

           $("#conteudoInicialBarco").addClass("invisible");
           $("#tabelaBarcos").addClass("invisible");

           $("#tabelaBarcos").removeClass("invisible");
           
        }

        
    });

    $("#btn_incluir_barco").click(function(){
        if($("#id_barco").val()==""|| $("#ano_barco").val()==""){
            alert("Favor preencher todos os dados!")
        }else{
            id_barco = $("#id_barco").val();
            tipo_barco = $("#tipo_barco").val();
            cor_barco = $("#cor_barco").val();
            ano_barco = $("#ano_barco").val();

            dados = JSON.stringify({id : id_barco, tipo : tipo_barco, cor : cor_barco, ano : ano_barco});

            $.ajax({
                url: 'http://localhost:5000/incluir_barco',
                type : 'POST',
                contentType : 'application/json',
                dataType: 'json',
                data: dados,
                success: incluirBarco,
                error: erroIncluirBarco
            })
            function incluirBarco(resposta) {
                if (resposta.resultado =="ok"){
                
                alert("Barco Incluido");
                $("#id_barco").val("");
                $("#ano_barco").val("");
                }else{
                    alert("Erro no BackEnd");
                }
            }
            function erroIncluirBarco(resposta){
                alert("Erro na chamada Backend");
            }
        }
       });

  });