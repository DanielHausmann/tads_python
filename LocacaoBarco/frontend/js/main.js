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

    //Codificação referente a listagem de Colaboradores
    $("#link_listar_colaboradores").click(function(){
    
        $.ajax({
            url:'http://localhost:5000/listar_colaboradores',
            method:'GET',
            dataType:'json',
            success:listar_colaboradores,
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

    // Codificação referente a listagem de Locações
    $("#link_listar_locacao").click(function(){
    
        $.ajax({
            url:'http://localhost:5000/listar_locacoes',
            method:'GET',
            dataType:'json',
            success:listar_locacoes,
            error: function() {
                alert("erro ao ler dados, verifique o backend");
            }
        });

        function listar_locacoes(locacoes){
           linhas = ""
           for(var i in locacoes){
               lin = 
                "<tr>" +
                "<th>"+locacoes[i].id+"</th>"+
                "<td>"+locacoes[i].cliente+"</td>"+
                "<td>"+locacoes[i].data_locacao+"</td>"+
                "<td>"+locacoes[i].data_entrega+"</td>"+
                "<td>"+locacoes[i].id_barco+"</td>"+
                "<td>"+locacoes[i].id_colaborador+"</td>"+
                "</tr>"
                
                linhas = linhas + lin;
           }
           $("#corpoTabelaLocacao").html(linhas);

           $("#conteudoInicialLocacao").addClass("invisible");
           $("#tabelaLocacao").addClass("invisible");

           $("#tabelaLocacao").removeClass("invisible");
           
        }
        
    });    

  });