$(document).ready(function() {



    const binding = $("#binding") 
    const binding2 = $("#binding2")


    // if($(window).width < 1026){
    //     document.getElementById("fadeshow1").style.display = "none";
    //     alert("ok")
    //    }

    window.onresize = function(event) {
        if($(window).width() < 960){
            binding.hide()
            binding2.hide()
        }
        else {
            binding.show()
            binding2.show()
        }
}


});