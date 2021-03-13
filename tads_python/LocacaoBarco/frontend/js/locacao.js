$(document).ready(function () {

    //Codificação referente a listagem de Locacao
    $("#link_listar_locacao").click(function () {

        $.ajax({
            url: 'http://localhost:5000/listar_locacoes',
            method: 'GET',
            dataType: 'json', // os dados são recebidos no formato json
            success: listar_locacao, // chama a função listar_locacao para processar o resultado
            error: function () {
                alert("erro ao ler dados, verifique o backend");
            }
        });

        function listar_locacao(locacoes) {
            linhas = ""
            for (var i in locacoes) {
                lin =
                    "<tr>" +
                    "<th>" + locacoes[i].id + "</th>" +
                    "<td>" + locacoes[i].nome + "</td>" +
                    "<td>" + locacoes[i].email + "</td>" +
                    "<td>" + locacoes[i].telefone + "</td>" +
                    "<td>" + locacoes[i].colaborador_id + "</td>" +
                    "<td>" + locacoes[i].barco_id + "</td>" +
                    '<td><a href=# id="excluir_' + locacoes[i].id + '"' + 'class="excluir_locacao"><img src="images/excluir.png" ' +
                    'alt="Excluir Locacao" title=Excluir Locacao></a>' + '</td>' +
                    "</tr>"
                linhas = linhas + lin;
            }
            $("#corpoTabelaLocacao").html(linhas);

            $("#conteudoInicialLocacao").addClass("invisible");
            $("#tabelaLocacao").addClass("invisible");

            $("#tabelaLocacao").removeClass("invisible");

        }

    });
    
    // codigo referente a exclusão de locacao
    $(document).on("click", ".excluir_locacao", function() {
       
        var componente_clicado = $(this).attr('id'); 
       
        var nome_icone = "excluir_";
        var id_locacao = componente_clicado.substring(nome_icone.length);
       
        $.ajax({
            url: 'http://localhost:5000/excluir_locacao/'+id_locacao,
            type: 'DELETE', // método da requisição
            dataType: 'json', // os dados são recebidos no formato json
            success: locacaoExcluida, 
            error: erroAoExcluir
        });
        function locacaoExcluida (retorno) {
            
            if (retorno.resultado == "ok") { 
                alert("Locacao removida com sucesso!");
                if (! $("#tabelaLocacao").hasClass('invisible')) {
                    document.getElementById("link_listar_locacao").click();
                }
            } else {
                // informar mensagem de erro
                alert("erro ao excluir dados" + retorno.resultado);
            }            
        }
        function erroAoExcluir (retorno) {
            // informar mensagem de erro
            alert("erro ao excluir dados, verifique o backend: ");
        }
    });


});