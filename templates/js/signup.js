jQuery(document).ready(function($) {
        $("#signup_form").validate({
            rules: {
                username: {
                    required: true,
                    minlength: 5,
                    maxlength: 10
                },
                password: {
                    required: true,
                    minlength: 6,
                    maxlength: 32
                },
                password_again: {
                    required: true,
                    minlength: 6,
                    maxlength: 32,
                    equalTo: "#password"
                },
                introduce: {
                    maxlength: 200
                },
                code: {
                    required: true
                }
            },
            messages: {
                password: {
                    required: "连密码都不输入,要你何用!",
                    minlength: jQuery.format("密码不能小于{0}个字符"),
                    maxlength: jQuery.format("密码不能大于{0}个字符")
                },
                password_again: {
                    required: "不确认下密码嘛..",
                    minlength: jQuery.format("确认密码不能小于{0}个字符"),
                    maxlength: jQuery.format("确认密码不能大于{0}个字符"),
                    equalTo: "不一样呀!"
                },
                username: {
                    required: "你没名字嘛..",
                    minlength: jQuery.format("用户名不能小于{0}个字符"),
                    maxlength: jQuery.format("用户名不能大于{0}个字符")

                },
                code: {
                    required: "验证码呢.",
                }
            }
        });
    $('#submit_1').click(function(event) {
        var password = $('#password').val();
        var password_again = $('#password_again').val();
        var password_md5 = $.md5(password);
        if(password !== '')
        {
            var password_md5 = $.md5(password);
            $('#password').val(password_md5);
        }
        if(password_again !== '')
        {
            var password_again_md5 = $.md5(password_again);
            $('#password_again').val(password_again_md5);
        }
        var username = $('#username').val();
        if(username !== '')
        {
            $.ajax({
                url: 'check_username/',
                type: 'POST',
                data: {'username': username}
            })
            .done(function(data) {
                console.log(data);
                if(data === '1')
                {
                    $('#username').empty();
                    $('#username').after("用户名已经注册.");
                    error = 1;
                }
                else if (data==='0')
                {
                    $('#username').empty();
                    $('#username').after("用户名没有注册.");
                }
                else
                {
                    $('#username').empty();
                    $('#username').after("出错了");
                }
                var code = $('#code_content').val();
                $.ajax({
                    url: 'decode/',
                    type: 'GET',
                    data: {'code': code}
                })
                .done(function(data) {
                    console.log("success"+data);
                    if(data === '1')
                    {
                        $('#code_result').empty();
                        $('#code_result').append("验证码正确");
                        $('#signup_form').submit()
                    }
                    else if(data === '0')
                    {
                        $('#code_result').empty();
                        $('#code_result').append("验证码错误");
                    }
                    else
                    {
                        $('#code_result').empty();
                        $('#code_result').append("验证码错误");
                    }
                })
                .fail(function() {
                    console.log("error");
                })
                .always(function() {
                    console.log("complete");
                });
            })
            .fail(function() {
                console.log("error");
            })
            .always(function() {
                console.log("complete");
            });        
        }
        
    });
    var provinceList = {
        北京:['东城区','西城区','崇文区','宣武区','朝阳区','丰台区','石景山区','海淀区','门头沟区','房山区','通州区','顺义区','昌平区','大兴区','怀柔区','平谷区','密云县','延庆县'],
        上海:['黄浦区','卢湾区','徐汇区','长宁区','静安区','普陀区','闸北区','虹口区','杨浦区','闵行区','宝山区','金山区','松江区','青浦区','南汇区','奉贤区','崇明县']  
    };
    for(var i in provinceList)
    {
        var string = $('<option></option>'); 
        string.attr('value',i);
        string.text(i);
        $('#province').append(string);
    }
    var province = $('#province').val()
    $('#city').empty();
    for(var j=0;j<provinceList[province].length;j++)
    {
        var string_options = $('<option></option>'); 
        string_options.attr('value', provinceList[province][j]);
        string_options.text(provinceList[province][j]);
        $('#city').append(string_options);
    }
    $('#province').change(function(event) {
        var province = $('#province').val()
        $('#city').empty();
        for(var j=0;j<provinceList[province].length;j++)
        {
            var string_options = $('<option></option>'); 
            string_options.attr('value', provinceList[province][j]);
            string_options.text(provinceList[province][j]);
            $('#city').append(string_options);
        }
    });    
});


