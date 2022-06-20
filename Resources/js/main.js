
$("#five").change(function() {
    $("#hotel_count").css("opacity", "0");

    if(this.checked) {
    $(".id4").css("display", "none");
    $(".id3").css("display", "none");
    $(".id2").css("display", "none");
    }else{
        $(".id4").css("display", "block");
        $(".id3").css("display", "block");
        $(".id2").css("display", "block");
    }
});

$("#four").change(function() {
    $("#hotel_count").css("opacity", "0");

    if(this.checked) {
    $(".id5").css("display", "none");
    $(".id3").css("display", "none");
    $(".id2").css("display", "none");
    }else{
        $(".id5").css("display", "block");
        $(".id3").css("display", "block");
        $(".id2").css("display", "block");
    }
});


$("#three").change(function() {
    $("#hotel_count").css("opacity", "0");

    if(this.checked) {
    $(".id4").css("display", "none");
    $(".id5").css("display", "none");
    $(".id2").css("display", "none");
    }else{
        $(".id4").css("display", "block");
        $(".id5").css("display", "block");
        $(".id2").css("display", "block");
    }
});

$("#two").change(function() {
    $("#hotel_count").css("opacity", "0");

    if(this.checked) {
    $(".id4").css("display", "none");
    $(".id5").css("display", "none");
    $(".id3").css("display", "none");
    }else{
        $(".id4").css("display", "block");
        $(".id5").css("display", "block");
        $(".id3").css("display", "block");
    }
});

$('#range').change(function(){
    console.log($('#range').val());
    let max=$('#range').val();
    $("#rangeSliderExample3MaxResult").text(max);
    let minAmount=$("#rangeSliderExample3MinResult").text();
    let maxAmount=$("#rangeSliderExample3MaxResult").text();
});
