

$('.correct').addClass("show");
$('.correct').removeClass("hide");
$('.correct').addClass("showAlert");
setTimeout(function(){
    $('.correct').removeClass("show");
    $('.correct').addClass("hide");
},5000);
$('.close-btn').click(function(){
    $('.correct').removeClass("show");
    $('.correct').addClass("hide");
});

$('.alert').addClass("show");
$('.alert').removeClass("hide");
$('.alert').addClass("showAlert");
setTimeout(function(){
    $('.alert').removeClass("show");
    $('.alert').addClass("hide");
},5000);
$('.close-btn').click(function(){
    $('.alert').removeClass("show");
    $('.alert').addClass("hide");
});