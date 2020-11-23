$( document ).ready(function() {

    // Codificação referente a listagem de Barcos
    $("#link_listar_barcos").click(function(){
    
        $.ajax({
            url:'http://localhost:5000/listar_barcos',
            method:'GET',
            dataType:'json', // os dados são recebidos no formato json
            success:listar_barcos, // chama a função listar para processar o resultado
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

  });