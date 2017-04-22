$.ajaxSetup({
    beforeSend: function(xhr, settings) {
        function getCookie(name) {
            var cookieValue = null;
            if (document.cookie && document.cookie != '') {
                var cookies = document.cookie.split(';');
                for (var i = 0; i < cookies.length; i++) {
                    var cookie = jQuery.trim(cookies[i]);
                    if (cookie.substring(0, name.length + 1) == (name + '=')) {
                        cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                        break;
                    }
                }
            }
            return cookieValue;
        }
        if (!(/^http:.*/.test(settings.url) || /^https:.*/.test(settings.url))) {
            xhr.setRequestHeader("X-CSRFToken", getCookie('csrftoken'));
        }
    }
});
$(document).ready(function() {
    ajax_add();
    get_list();
    get_flist();
});

function ajax_add() {
    $('#myModal form').submit(function() {
        $.ajax({
            type: "POST",
            data: $('#myModal form').serializeObject(),
            url: "/todos/",
            cache: false,
            success: function(textStatus) {
                get_list();
                $('#myModal').modal('hide');
                $('#myModal form')[0].reset();
            },
            error: function(XMLHttpRequest, textStatus, errorThrown) {
                console.log(XMLHttpRequest.status);
                console.log(XMLHttpRequest.readyState);
                console.log(textStatus);
            }
        });
        return false;
    });
};

function del(tid) {
    $.ajax({
        type: "DELETE",
        url: "/todos/" + tid,
        cache: false,
        success: function(textStatus) {
            get_list();
            get_flist();
        },
        error: function(XMLHttpRequest, textStatus, errorThrown) {
            console.log(XMLHttpRequest.status);
            console.log(XMLHttpRequest.readyState);
            console.log(textStatus);
        }
    });
};

function update(tid) {
    var res = get_detail(tid);
    console.log(res);
    $('#myModal1').modal('show');
    $('#myModal1 form textarea').html(res.todo);
    $('#myModal1 form').submit(function() {
        $.ajax({
            type: "POST",
            data: $('#myModal1 form').serialize(),
            url: "/detail/" + tid + "/",
            cache: false,
            success: function(textStatus) {
                get_list();
                get_flist();
                $('#myModal1').modal('hide');
                $('#myModal1 form')[0].reset();
            },
            error: function(XMLHttpRequest, textStatus, errorThrown) {
                console.log(XMLHttpRequest.status);
                console.log(XMLHttpRequest.readyState);
                console.log(textStatus);
            }
        });
        return false;
    });
};

function change(tid) {
    $.ajax({
        type: "GET",
        url: "/change/" + tid,
        cache: false,
        success: function(textStatus) {
            get_list();
            get_flist();
        },
        error: function(XMLHttpRequest, textStatus, errorThrown) {
            console.log(XMLHttpRequest.status);
            console.log(XMLHttpRequest.readyState);
            console.log(textStatus);
        }
    });
}

function get_detail(tid) {
    var qwe;
    $.ajax({
        type: "GET",
        url: "/list/" + tid + ".json/",
        cache: false,
        async: false,
        success: function(json, textStatus) {
            // console.log(json);
            qwe = json;
        },
        error: function(XMLHttpRequest, textStatus, errorThrown) {
            console.log(XMLHttpRequest.status);
            console.log(XMLHttpRequest.readyState);
            console.log(textStatus);
        }
    });
    return qwe;
}

function get_list() {
    $.ajax({
        type: "GET",
        url: "/list.json/",
        cache: false,
        async: false,
        success: function(json, textStatus) {
            // console.log(json.results);
            list_todo(json.results);
        },
        error: function(XMLHttpRequest, textStatus, errorThrown) {
            console.log(XMLHttpRequest.status);
            console.log(XMLHttpRequest.readyState);
            console.log(textStatus);
        }
    });
}

function get_flist() {
    $.ajax({
        type: "GET",
        url: "/flist.json/",
        async: false,
        cache: false,
        success: function(json, textStatus) {
            // console.log(json.results);
            list_ftodo(json.results);
        },
        error: function(XMLHttpRequest, textStatus, errorThrown) {
            console.log(XMLHttpRequest.status);
            console.log(XMLHttpRequest.readyState);
            console.log(textStatus);
        }
    });
}

function list_todo(list) {
    var tb1 = "",
        tb2 = "",
        tb3 = "",
        tb = '<tr class="active"><td>内容</td><td>创建时间</td><td>操作</td></tr>';
    $("#list_table").fadeOut(function() {
        $("#list_table").empty();
        var len = list.length;
        for (var i = 0; i < len; i++) {
            var timeStamp = new Date(list[i].pubtime).getTime();
            var time = format(timeStamp);
            switch (list[i].priority) {
                case '1':
                    tb1 += '<tr class="danger"><td>' + list[i].todo + '</td><td>' + time + '</td><td><div class="span2"><a onclick = change(' + list[i].tid + ')><span class="glyphicon glyphicon-ok"></span></a><a   onclick = update(' + list[i].tid + ') ><span class="glyphicon glyphicon-edit"></span></a><a class="btn btn-danger btn-xs pull-right" onclick = del(' + list[i].tid + ')><span class="glyphicon glyphicon-trash"><span></a></div></td></tr>';
                    break;
                case '2':
                    tb2 += '<tr class="warning"><td>' + list[i].todo + '</td><td>' + time + '</td><td><div class="span2"><a onclick = change(' + list[i].tid + ')><span class="glyphicon glyphicon-ok"></span></a><a onclick = update(' + list[i].tid + ')><span class="glyphicon glyphicon-edit"></span></a><a class="btn btn-danger btn-xs pull-right" onclick = del(' + list[i].tid + ')><span class="glyphicon glyphicon-trash"><span></a></div></td></tr>';
                    break;
                default:
                    tb3 += '<tr class="success"><td>' + list[i].todo + '</td><td>' + time + '</td><td><div class="span2"><a onclick = change(' + list[i].tid + ')><span class="glyphicon glyphicon-ok"></span></a><a onclick = update(' + list[i].tid + ')><span class="glyphicon glyphicon-edit"></span></a><a class="btn btn-danger btn-xs pull-right" onclick = del(' + list[i].tid + ')><span class="glyphicon glyphicon-trash"><span></a></div></td></tr>';
            }
        }
        $("#list_table").prepend(tb, tb1, tb2, tb3);
    });
    $("#list_table").fadeIn();
}

function getLocalTime(nS) {
    return new Date(parseInt(nS) * 1000).toLocaleString().replace(/:\d{1,2}$/, ' ');
}

function format(shijianchuo) {
    function add0(m) {
        return m < 10 ? '0' + m : m
    }
    //shijianchuo是整数，否则要parseInt转换
    var time = new Date(shijianchuo);
    var y = time.getFullYear();
    var m = time.getMonth() + 1;
    var d = time.getDate();
    var h = time.getHours();
    var mm = time.getMinutes();
    var s = time.getSeconds();
    return y + '-' + add0(m) + '-' + add0(d) + ' ' + add0(h) + ':' + add0(mm) + ':' + add0(s);
}

function list_ftodo(list) {
    var len = list.length;
    var tb1 = "",
        tb = '<tr class="active"><td>内容</td><td>完成时间</td><td>操作</td></tr> ';
    $("#dine_table").fadeOut(function() {
        $("#dine_table").empty();
        for (var i = 0; i < len; i++) {
            var timeStamp = new Date(list[i].lastdate).getTime();
            var time = format(timeStamp);
            tb1 += '<tr class="info"><td class="ftodo">' + list[i].todo + '</td><td>' + time + '</td><td><div class="span2"><a onclick = change(' + list[i].tid + ')><span class="glyphicon glyphicon-repeat"></span></a><a class="btn btn-danger btn-xs pull-right" onclick = del(' + list[i].tid + ')><span class="glyphicon glyphicon-trash"><span></a></div></td></tr>';
        }
        $("#dine_table").prepend(tb, tb1);
    });
    $("#dine_table").fadeIn();
}
$.fn.serializeObject = function() {
    var o = {};
    var a = this.serializeArray();
    $.each(a, function() {
        if (o[this.name]) {
            if (!o[this.name].push) {
                o[this.name] = [o[this.name]];
            }
            o[this.name].push(this.value || '');
        } else {
            o[this.name] = this.value || '';
        }
    });
    return o;
};
// function update(tid) {
//     var res = get_detail(tid);
//     console.log(res);
//     $('#myModal1').modal('show');
//     $('#myModal1 form textarea').html(res.todo);
//     $('#myModal1 form').submit(function() {
//         $.ajax({
//             type: "PUT",
//             data: $('#myModal1 form').serializeObject(),
//             url: "/todos/",
//             cache: false,
//             // headers: {
//             //     'X-CSRFToken': '{{ csrf_token }}'
//             // },
//             success: function(textStatus) {
//                 get_list();
//                 get_flist();
//                 $('#myModal1').modal('hide');
//                 $('#myModal1 form')[0].reset();
//             },
//             error: function(XMLHttpRequest, textStatus, errorThrown) {
//                 console.log(XMLHttpRequest.status);
//                 console.log(XMLHttpRequest.readyState);
//                 console.log(textStatus);
//             }
//         });
//         return false;
//     });
// };