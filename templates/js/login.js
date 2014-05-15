jQuery(document).ready(function($) {
    $('#submit_1').click(function(event) {
        _md5();
        check_code();
    });
});


function _md5 () {
    var password = $('#password').val();
    var password_md5 = $.md5(password);
    if(password !== '')
    {
        var password_md5 = $.md5(password);
        $('#password').val(password_md5);
        // alert(password_md5);
    }
}

function check_code(){
    var code = $('#code_content').val()
    $.ajax({
        url: '/login/decode/',
        type: 'GET',
        data: {'code':  code}
    })
    .done(function(data) {
        if(data === '1')
        {
            $('#code_result').empty();
            $('#code_result').append("验证码正确");
            $('#login_form').submit()
        }
        else if(data === '0')
        {
            $('#code_result').empty();
            $('#code_result').append("验证码错误");
        }
        else
        {
            $('#code_result').empty();
            $('#code_result').append("验证码错误1");
        }
    })
    .fail(function() {
        console.log("error");
    })
    .always(function() {
        console.log("complete");
    });
        
}

