
$("#five").change(function() {
    if(this.checked) {
    $("#id4").css("display", "none");
    $("#id3").css("display", "none");
    $("#id2").css("display", "none");
    }else{
        $("#id4").css("display", "block");
        $("#id3").css("display", "block");
        $("#id2").css("display", "block");
    }
});

$("#four").change(function() {
    if(this.checked) {
    $("#id5").css("display", "none");
    $("#id3").css("display", "none");
    $("#id2").css("display", "none");
    }else{
        $("#id5").css("display", "block");
        $("#id3").css("display", "block");
        $("#id2").css("display", "block");
    }
});


$("#three").change(function() {
    if(this.checked) {
    $("#id4").css("display", "none");
    $("#id5").css("display", "none");
    $("#id2").css("display", "none");
    }else{
        $("#id4").css("display", "block");
        $("#id5").css("display", "block");
        $("#id2").css("display", "block");
    }
});

$("#two").change(function() {
    if(this.checked) {
    $("#id4").css("display", "none");
    $("#id5").css("display", "none");
    $("#id3").css("display", "none");
    }else{
        $("#id4").css("display", "block");
        $("#id5").css("display", "block");
        $("#id3").css("display", "block");
    }
});