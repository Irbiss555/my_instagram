let csrfToken = getCookie('csrftoken');
let baseUrl = 'http://127.0.0.1:8000/'

function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        let cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            let cookie = jQuery.trim(cookies[i]);
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
$(document).ready(function (){
    $.ajax({
                method: 'POST',
                url: `${baseUrl}api/login/`,
                data: JSON.stringify({username: 'admin', password: 'admin'}),
                contentType: 'application/json',
        success: function (response) {
            localStorage.setItem('auth_token', response.token)
        },
        error: function (response) {
                    console.log(response)
                }
        }
        ).then(function () {
            $('.btn-like').click(function (e){
            e.preventDefault()
                $.ajax({
                method: 'POST',
                url: baseUrl + `api/post/${$(e.currentTarget).data('id')}/likes/`,
                headers: {Authorization: 'Token ' + localStorage.getItem('auth_token')},
                // data: JSON.stringify({username: 'admin', password: 'admin'}),
                // dataType: 'json',
        success: function (response) {
                $(`#like-txt-${$(e.currentTarget).data('id')}`).text(`${response.likes_total} users like post`)
                let i = $(e.currentTarget).children('i').toggleClass('fa-solid fa-regular')
        },
        error: function (response) {
                    console.log(response)
                }
        }
        )
    })




    })
})