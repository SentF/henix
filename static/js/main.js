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

    $('#btn_buy').click(function () {
        Swal.fire({
            html:
                '<p class="title_swal">Payment</p>'+
                '<p class="text_swal"> Select payment method.</p>'+
                '<div class="payment_methods"> '+
                    '<input type="radio" name="payment_methods" class="payment_methods ">'+
                        '<p class="bitcoin_icon>"></p> '+
                        '<p class="white_text">Bitcoin</p>'+
                    '</input>'+
                    '<input type="radio" name="payment_methods" class="payment_methods ">'+
                        '<p class="paypal_icon>"></p> '+
                        '<p class="white_text">PayPal</p>'+
                    '</input>'+
                    '<input type="radio" name="payment_methods" class="payment_methods ">'+
                        '<p class="credit_card_icon>"></p> '+
                        '<p class="white_text">Credit card</p>'+
                    '</input>'+
                '</div>'+
                '<input type="email" class="form-control input_swal" id="exampleFormControlInput1" placeholder="name@example.com">'+
                '<button onclick="pay()" class="confirm_swal">Pay</button>'
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

function pay() {

}