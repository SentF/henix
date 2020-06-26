$(document).ready(function () {
    $('#btn_key').click(function () {
        Swal.fire({
            html:
                '<p style="font-size: 14px; color: #FF5C00; margin-bottom: 8px;">Thank you for buying</p>'+
                '<p style="color: #fff"> Get the key to activate the hack.</p>'+
                '<div class="fake_input">' +
                    '<text style="text-align: left; font-size: 16px; margin-left: 8px" class="blue_text">H12TJI21F2130JI0TDSSPAD412</text>' +
                    '<button onclick="copy()" class="copy_icon"></button>'+
                '</div>'+
                '<button onclick="closeSwal()" style="margin-top: 16px; width: 286px; height: 42px; background: #FF5C00; color: #fff; border-radius: 5px; border: #FF5C00">Done</button>'
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

}

function closeSwal() {
    Swal.close()
}