var $form = '';
var base_modal_html = '';

$(function() {
  init();
});

function init(){
    $form = $('#user_form');
    base_modal_html = $('#user_modal').html();
}

function clear_errors() {
    $form.find('li.error').remove()
}

function clear_form() {
    console.log('clear form');
    clear_errors();
    $('input', $form).val('')
}

function show_errors(errors) {
    for (var error_name in errors) {
        for (var error in errors[error_name]){
            $('[name=' + error_name + ']', $form).closest('td').prepend('<li class="error">'+ errors[error_name][error].message + '</li>');
        }
        $('[name=' + error_name + ']', $form).parent().addClass('error');
    }

}

function update_page(new_html) {
    // console.log('new_html -->', new_html);
    $('#users_list').html(new_html)
}

function getFormData(form) {
    var unindexed_array = form.serializeArray();
    var indexed_array = {};

    $.map(unindexed_array, function (n, i) {
        indexed_array[n['name']] = n['value'];
    });

    return indexed_array;
}

function send_data() {
    var id = $('#user_id').html();
    // console.log('user_id = ', id);
    var prefix =  (id != undefined) ? id : '';
    var user_data = getFormData($form);
    // console.log('user_data = ', user_data);
    $.ajax({
        url: 'create/user/' + prefix,
        type: 'POST',
        data: user_data,
        dataType: 'json',
        success: function (response) {
            console.log("response = ", response);
            if (response.errors) {
                var errors = JSON.parse(response.errors);
                //console.log("errors = ", errors);
                clear_errors();
                show_errors(errors);
            } else {
                clear_form();
                // $('#myModal').modal('hide');
                update_page(response.html);
                console.log("Object create");
                clear_form()
            }
        },
        error: function (xhr, status, error) {
            console.log('error =', error)
        }
    });
}

function fill_form(id){
    $.ajax({
        url: 'get_user_form/' + id,
        type: 'GET',
        dataType: 'json',
        success: function (response) {
            if (response.errors) {
                console.log("errors = ", errors);
            } else {
                $('#user_form').html(response.html);
            }
        },
        error: function (xhr, status, error) {
            console.log('error =', error)
        }
    });
}

// DEMO-function TEMPLATE
function demo_send_data(id){
    $.ajax({
        url: '<адрес ajax-запроса>',
        type: 'GET/POST',
        dataType: 'json',
        // Функция, которая будет выполнена при успешном ответе
        success: function (response) {
            console.log("response = ", response);
        },
        // Функция, которая будет выполнена, при ошибке на сервере
        error: function (xhr, status, error) {
            console.log('error =', error)
        }
    });
}

// function recover_base_form(){
//     $('#user_modal').html(base_modal_html);
//     $form = $('#user_form');
// }