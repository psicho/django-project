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