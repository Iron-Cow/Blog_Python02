$(document).ready(function () {
    console.log('ready works');

    // $('#login_field').click(function () {
    //     alert("ВНИМАНИЕ!!! КЛИК ПО ЛОГИНУ!!!")
    // })
    let valid_login = false;
    let valid_email = false;

    let loginExp = /^[a-zA-Z0-9][a-zA-Z0-9_]{4,14}$/
    let passExp = /^[a-zA-Z0-9]{5,10}$/
    let regExp_email = /^([a-z0-9_-]+\.)*[a-z0-9_-]+@[a-z0-9_-]+(\.[a-z0-9_-]+)*\.[a-z]{2,6}$/;
    // console.log(loginExp.test('aaa3a'));
    // console.log(loginExp.test('bas%3sadf'));
    // console.log(loginExp.test('abasdfdsaf'));
    // console.log(loginExp.test('t,1df'));

    $('#login_field').change(function () {
        let _login = $(this).val()
        // console.log(loginExp.test(_login))
        if (!loginExp.test(_login)){  // логин не валидный
            $('#login_ico').attr('src', '../../static/img/error.png')
            $('#login_err').text('Логин должен быть длинной 5-15 символов и состоять из букв и цифр!')
            valid_login = false;
        }else{// логин валидный
            console.log('tut')
            $.ajax({
                url: '/ajax_reg',
                data: 'login_field=' + _login,
                success: function (result) {
                    if (result.message_login === 'занят'){
                        $('#login_ico').attr('src', '../../static/img/error.png')
                        $('#login_err').text('Логин уже занят!!!!!!')
                        valid_login = false;
                    }else{
                        $('#login_ico').attr('src', '../../static/img/win.png')
                        $('#login_err').text('')
                        valid_login = true;
                    }
                }

            })


        }
    })

    $('#login_field').focus(function () {
        $('#login_ico').attr('src', '../../static/img/question.png')
        $('#login_err').text('')
    })



    $('#email_field').blur(function () {
        let _email = $(this).val()
        if (regExp_email.test(_email)){ // валидный емайл
            $('#email_ico').attr('src', '../../static/img/win.png')
            $('#email_err').text('')
            valid_email = true;
        }else{// не валидный емайл
            $('#email_ico').attr('src', '../../static/img/error.png')
            $('#email_err').text('Не валидная почта!!!')
            valid_email = false;
        }
    })

    $('#email_field').focus(function () {  // сброс ошибок и иконок
        $('#email_ico').attr('src', '../../static/img/question.png')
        $('#email_err').text('')
    })



    $('#papassword_confirm_field').focus(function () {  // сброс ошибок и иконок
        $('#papassword_confirm_ico').attr('src', '../../static/img/question.png')
        $('#papassword_confirm_err').text('')
    })

$('#password_confirm_field').blur(function () {
    let _pass2 = $(this).val()
    if (passExp.test(_pass2)){
         if ($("#password_field").val() === $("#password_confirm_field").val()){// не валидный
              $('#password_confirm_ico').attr('src', '../../static/img/win.png')
              $('#password_confirm_err').text('')
              valid_password2 = true;
         }else{
               $('#password_confirm_ico').attr('src', '../../static/img/error.png')
               $('#papassword_confirm_err').text('Пароли должны быть одинаковы!!!')
               valid_password2 = false;

    }}else{// не валидный
        $('#password_confirm_ico').attr('src', '../../static/img/error.png')
        $('#papassword_confirm_err').text('Пароль должен содержать буквы и цыфры, количество символов 8-16!!!')
        valid_password2 = false;
    }
})


    $('#submit').click(function () {
        if (
            valid_login === true &&
            valid_email === true
        ){
            $('.form-group').attr('onsubmit', 'return true')
        }
    })

})
