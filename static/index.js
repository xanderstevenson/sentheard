$(document).ready(function() {



    const binding = $("#binding") 
    const binding2 = $("#binding2")


// hide or show scrolls based on window width


    window.onresize = function(event) {
        if($('#row1').width() < 960)  {
            binding.hide()
            binding2.hide()
        }
        else {
            binding.show()
            binding2.show()
        }
    }

    
// hide scrolls if you click on them

    $('.bindings').click(()=> {
        $('.bindings').hide()
    })

}); 