$(document).ready(function() {



    const binding = $("#binding")
    const binding2 = $("#binding2")

    const smallMarble = $("#home-container")
    const mediumMarble = $("#home-container-md")
    const largeMarble = $("#home-container-lg")

    smallMarble.hide()
    mediumMarble.hide()
    largeMarble.hide()


// hide or show scrolls based on window width


    window.onresize = function(event) {

        if($('#row1').width() <= 650)  {
            binding.hide()
            binding2.hide()
            smallMarble.show()
            mediumMarble.hide()
            largeMarble.hide()
        }
        else if($('#row1').width() > 650 && $('#row1').width() <= 1080)  {
            binding.hide()
            binding2.hide()
            smallMarble.hide()
            mediumMarble.show()
            largeMarble.hide()
        }

        else if($('#row1').width() > 1080) {
            binding.show()
            binding2.show()
            smallMarble.hide()
            mediumMarble.hide()
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