$(document).ready(function () {

    // Codificação referente a listagem de Barcos
    $("#link_listar_barcos").click(function () {

        $.ajax({
            url: 'http://localhost:5000/listar_barcos',
            method: 'GET',
            dataType: 'json', // os dados são recebidos no formato json
            success: listar_barcos, // chama a função listar_barcos para processar o resultado
            error: function () {
                alert("erro ao ler dados, verifique o backend");
            }
        });

        function listar_barcos(barcos) {
            linhas = ""
            for (var i in barcos) {
                lin =
                    "<tr>" +
                    "<th>" + barcos[i].id + "</th>" +
                    "<td>" + barcos[i].tipo + "</td>" +
                    "<td>" + barcos[i].cor + "</td>" +
                    "<td>" + barcos[i].ano + "</td>" +
                    '<td><a href=# id="excluir_' + barcos[i].id + '"' + 'class="excluir_barco"><img src="images/excluir.png" ' +
                    'alt="Excluir Barco" title=Excluir Barco></a>' + '</td>' +
                    "</tr>"
                linhas = linhas + lin;
            }
            $("#corpoTabelaBarcos").html(linhas);

            $("#conteudoInicialBarco").addClass("invisible");
            $("#tabelaBarcos").addClass("invisible");

            $("#tabelaBarcos").removeClass("invisible");

        }


    });

    // Codificação referente a inserção de Barcos
    $("#btn_incluir_barco").click(function () {
        //Verifica se algum valor esta vazio
        if ($("#ano_barco").val() == "") {
            alert("Favor preencher todos os dados!")
        } else {
            //obtem os dados do formulário
            tipo_barco = $("#tipo_barco").val();
            cor_barco = $("#cor_barco").val();
            ano_barco = $("#ano_barco").val();

            // prepara os dados para o envio em json
            dados = JSON.stringify({ tipo: tipo_barco, cor: cor_barco, ano: ano_barco });
            //manda para o back-end
            $.ajax({
                url: 'http://localhost:5000/incluir_barco',
                type: 'POST',
                contentType: 'application/json',
                dataType: 'json',
                data: dados,
                success: incluirBarco,
                error: erroIncluirBarco
            })
            function incluirBarco(resposta) {
                if (resposta.resultado == "ok") {
                    //mensagem de sucesso
                    alert("Barco Incluido");
                    //limpa os valor de ANO do barco
                    $("#ano_barco").val("");
                } else {
                    //mensagem caso ocorra algum erro de comunicação
                    alert("Erro na Comunicação");
                }
            }
            function erroIncluirBarco(resposta) {
                //mensagem caso ocorra algum erro na requisição back-end
                alert("Erro na chamada Backend");
            }
        }

    });

    // codigo referente a exclusão de Barcos
    $(document).on("click", ".excluir_barco", function () {
        
        var componente_clicado = $(this).attr('id');
        
        var nome_icone = "excluir_";
        var id_barco = componente_clicado.substring(nome_icone.length);
        
        $.ajax({
            url: 'http://localhost:5000/excluir_barco/' + id_barco,
            type: 'DELETE', // método da requisição
            dataType: 'json', // os dados são recebidos no formato json
            success: barcoExcluido, 
            error: erroAoExcluir
        });
        function barcoExcluido(retorno) {

            if (retorno.resultado == "ok") {
                alert("Barco removido com sucesso!");
                if (! $("#tabelaBarcos").hasClass('invisible')) {
                    document.getElementById("link_listar_barcos").click();
                }
            } else {
                // informar mensagem de erro
                alert("erro ao excluir dados" + retorno.resultado);
            }
        }
        function erroAoExcluir(retorno) {
            // informar mensagem de erro
            alert("erro ao excluir dados, verifique o backend: ");
        }
    });

});