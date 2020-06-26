$(document).ready(function () {
    $('#btn_key').click(function () {
        Swal.fire({
            html:
                '<p class="title_swal">Thank you for buying</p>'+
                '<p class="text_swal"> Get the key to activate the hack.</p>'+
                '<div class="fake_input">' +
                    '<text style="text-align: left; font-size: 16px; margin-left: 8px" class="blue_text">H12TJI21F2130JI0TDSSPAD412</text>' +
                    '<button onclick="copy()" class="copy_icon"></button>'+
                '</div>'+
                '<button onclick="closeSwal()" class="confirm_swal">Done</button>'
            ,
            showConfirmButton: false,
            showCloseButton: false,
            showCancelButton: false,
            focusConfirm: false,
            width: 331,
            background: '#1F2346',
        })
    });
});

function copy() {
    if ($('#tmp').length) {
        $('#tmp').remove();
    }
    var clickText = $(this).text();
    $('<textarea id="tmp" />')
        .appendTo($('.swal2-container'))
        .val($('.swal2-container text').text())
        .focus()
        .select();
    document.execCommand("copy");
    $('#tmp').remove()
}

function closeSwal() {
    Swal.close()
}