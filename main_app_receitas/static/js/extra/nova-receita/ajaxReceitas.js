$(document).ready(
    function listarReceitas() {
        $.ajax({
            type: 'GET',
            url: 'http://jsonstub.com/receita/lista',
            contentType: 'application/json',
            beforeSend: function (request) {
                request.setRequestHeader('JsonStub-User-Key', 'a4ed75a2-3733-4107-aacb-68a12165b258');
                request.setRequestHeader('JsonStub-Project-Key', '322cfc5d-3c67-40a3-bb76-d4d40e59d94a');
            }
        }).done(function (data) {
            $.each(data, function (indexInArray, valueOfElement) {
                var row = $("<tr />");
                var buttonEdit = '<td><button type="button" class="btn btn-md" data-toggle="modal" data-target="#editReceita"><i class="fa fa-edit"></i></button></td>';
                var buttonDelete = '<td><button type="button" id="buttonDelelar" class="btn btn-danger btn-md" data-toggle="modal" data-target="#deletarIngrediente"><i class="fa fa-trash-o"></i></button></td>';
                var buttonView = '<td><button type="button" class="btn btn-default btn-md" data-toggle="modal" data-target="#visualizar"><i class="fa fa-eye" aria-hidden="true"></i></span> Visualizar Receita </button></td>';
                
                $("#tableReceitas").append(row); //this will append tr element to table... keep its reference for a while since we will add cels into it
                row.append($("<td>" + valueOfElement.nome_receita + "</td>"));
                row.append($("<td>" + valueOfElement.classificacao + "</td>"));
                row.append($("<td>" + valueOfElement.categoria + "</td>"));
                row.append(buttonEdit);
                row.append(buttonDelete);
                row.append(buttonView);
            });
        });
    });

    $(deletarIngrediente).click(function (e) { 
        e.preventDefault();

        
    });