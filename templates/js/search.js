jQuery(document).ready(function($) {
    $('#submit_1').click(function(event) {
        var username = $('#username').val()
        if(username !== ''){
            $.ajax({
                url: 'submit/',
                type: 'GET',
                data: {'username':username}
            })
            .done(function(data) {
                console.log("success");
                info = $.parseJSON(data);
                $('#result_div').empty();
                for(var i in info)
                {   
                    temp_string1 = '';
                    temp_string2 = '';
                    if(i === 'hobby')
                    {
                        temp_string1 = '爱好:';
                        hobby = info[i].split(' ');
                        for(var j in hobby)
                        {
                            if(j === '1')
                                temp_string2 = temp_string2 + ' 篮球';
                            if(j === '2')
                                temp_string2 = temp_string2 + ' 足球';
                            if(j === '3')
                                temp_string2 = temp_string2 + ' 音乐';
                            if(j === '4')
                                temp_string2 = temp_string2 + ' 电子竞技';
                        }
                    }
                    else if(i === 'native_place')
                    {
                        temp_string1 = '籍贯:';
                        temp_string2 = info[i];
                    }
                    else if(i === 'introduce')
                    {
                        temp_string1 = '介绍:';
                        temp_string2 = info[i];
                    }
                    else if(i === 'gender')
                    {
                        temp_string1 = '性别:'
                        if(info[i] === true)
                        {
                            temp_string2 = '男';
                        }
                        else
                        {
                            temp_string2 = '女';
                        }
                    }
                    else if(i === 'photo_path')
                    {
                        temp_string1 = '头像:';
                        temp_string2 = info[i];
                    }
                    string1 = $('<b></b>');
                    string1.text(temp_string1);
                    $('#result_div').append(string1);
                    if(i !== 'photo_path')
                    {
                        string2 = $('<p></p>');
                        string2.text(temp_string2);
                        $('#result_div').append(string2);    
                    }
                    else
                    {
                        string2 = $('<br><img width="200px" height="100px"/><br>');
                        string2.attr('src','/'+temp_string2);
                        $('#result_div').append(string2);       
                    }
                    
                }
            })
            .fail(function() {
                console.log("error");
            })
            .always(function() {
                console.log("complete");
            });
        }
    });
})