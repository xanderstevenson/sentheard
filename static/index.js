$(document).ready(function() {



    const binding = $("#binding")
    const binding2 = $("#binding2")

    const smallMarble = $("#home-container")
    const largeMarble = $("#home-container-lg")

    smallMarble.hide()


// hide or show scrolls based on window width


    window.onresize = function(event) {
        if($('#row1').width() < 950)  {
            binding.hide()
            binding2.hide()
            smallMarble.show()
            largeMarble.hide()
        }
        else {
            binding.show()
            binding2.show()
            smallMarble.hide()
            largeMarble.show()
        }
    }


// hide scrolls if you click on them

    $('.bindings').click(()=> {
        $('.bindings').hide()
    })

// show  different marble, based on screen size


    // window.onresize = function(event) {
    //     if($('#row1').width() > 460)  {
    //         small-marble.hide()

    //     }
    //     else {
    //         small-marble.show()

    //     }
    // }



});