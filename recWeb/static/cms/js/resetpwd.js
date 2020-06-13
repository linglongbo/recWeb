
$(function () {
    $("#submit").click(function (event) {
        // event.preventDefault
        // 是阻止按钮默认的提交表单的事件
        event.preventDefault();

        var oldpwdE = $("input[name=oldpwd]");
        var newpwdE = $("input[name=newpwd]");
        var commenpwdE = $("input[name=commenpwd]");

        var oldpwd = oldpwdE.val();
        var newpwd = newpwdE.val();
        var commenpwd = commenpwdE.val();

        // 1. 要在模版的meta标签中渲染一个csrf-token
        // 2. 在ajax请求的头部中设置X-CSRFtoken
        zlajax.post({
            'url': '/cms/resetpwd/',
            'data': {
                'oldpwd': oldpwd,
                'newpwd': newpwd,
                'commenpwd': commenpwd
            },
            'success': function (data) {
                if (data['code'] == 200){
                    zlalert.alertSuccessToast("密码修改成功！");
                    newpwdE.val("");
                    oldpwdE.val("");
                    commenpwdE.val("");
                }else {
                    var message = data['message'];
                    zlalert.alertInfo(message);
                }
            },
            'fail': function (error) {
                zlalert.alertNetworkError();
            }
        });
    });
});