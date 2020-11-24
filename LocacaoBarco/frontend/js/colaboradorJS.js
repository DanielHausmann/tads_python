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
});