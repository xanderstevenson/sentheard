

$(document).ready(function() {

    const binding = $("#binding")
    const binding2 = $("#binding2")

    const smallMarble = $("#home-container")
    const mediumMarble = $("#home-container-md")
    const largeMarble = $("#home-container-lg")

    smallMarble.hide()
    mediumMarble.hide()
    largeMarble.hide()

    $('#logo').hide()





    const hcSmTxt = $('#hc-sm-txt')

        const verse = ['You\'ll record personalized momentos for your family, friends and descendants to cherish.',
        'Audio, Video and Images, recorded by you, to pass along to the next generation.',
        'We are the Creator and Industry Leader in Digital Inheritance Services']



        const newText = ()=>{

            if(hcSmTxt.text.length == 0 || hcSmTxt.text() == ''){
                return(verse[0])
            }
            else if(hcSmTxt.text() == verse[0]){
                return(verse[1])
            }
            else if(hcSmTxt.text() == verse[1]){
                return(verse[2])
            }
            else if(hcSmTxt.text() == verse[2]){
                return(verse[0])
            }
            else {
                return(hcSmTxt.text + '<--- text present')
            }

        }


        setInterval(()=>{
            $('#logo').fadeIn(2500);
            hcSmTxt.text(newText)
            $('#logo').fadeOut(2500);
        }, 5000)


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

/// rotate text






});