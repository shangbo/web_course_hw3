jQuery(document).ready(function($) {
    $('#submit').click(function(event) {
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
    });
    var provinceList = {
        无:['无'],
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


