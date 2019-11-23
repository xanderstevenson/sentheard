

$(document).ready(function() {

    const binding = $("#binding")
    const binding2 = $("#binding2")

    const smallMarble = $("#home-container")
    const mediumMarble = $("#home-container-md")
    const largeMarble = $("#home-container-lg")

    smallMarble.hide()
    mediumMarble.hide()
    largeMarble.hide()




    const hcSmTxt = $('#hc-sm-txt')
    const hcMdTxt = $('#hc-md-txt')
    const hcLgTxt = $('#hc-lg-txt')

    const smLogo = $('#logo')
    const mdLogo = $('#logo-md')
    const lgLogo = $('#logo-lg')


    smLogo.hide()
    mdLogo.hide()
    lgLogo.hide()

        const verse = ['Record your Stories in Audio, Video, Images and Text to pass along to future generations.',
            'You\'ll record Personalized Momentos for your family, friends and descendants to cherish.',
            'We are the Creator and World Leader in Digital Inheritance Services.',
            'Somewhere between Heaven and Earth...Let\'s get centered...']


const textMarbleAll = function(marble, logo){

            const newText = ()=>{

            if(marble.text.length == 0 || marble.text() == ''){
                return(verse[0])
            }
            else if(marble.text() == verse[0]){
                return(verse[1])
            }
            else if(marble.text() == verse[1]){
                return(verse[2])
            }
            else if(marble.text() == verse[2]){
                return(verse[3])
            }
            else if(marble.text() == verse[3]){
                return(verse[0])
            }
            else {
                return(marble.text + '<--- text present')
            }

        }


        setInterval(()=>{
            $(logo).fadeIn(2500);
            marble.text(newText)
            $(logo).fadeOut(2500);
        }, 5000)
}


textMarbleAll(hcMdTxt, mdLogo)
textMarbleAll(hcLgTxt, lgLogo)

        // const newText = ()=>{

        //     if(hcSmTxt.text.length == 0 || hcSmTxt.text() == ''){
        //         return(verse[0])
        //     }
        //     else if(hcSmTxt.text() == verse[0]){
        //         return(verse[1])
        //     }
        //     else if(hcSmTxt.text() == verse[1]){
        //         return(verse[2])
        //     }
        //     else if(hcSmTxt.text() == verse[2]){
        //         return(verse[0])
        //     }
        //     else {
        //         return(hcSmTxt.text + '<--- text present')
        //     }

        // }


        // setInterval(()=>{
        //     $('#logo').fadeIn(2500);
        //     hcSmTxt.text(newText)
        //     $('#logo').fadeOut(2500);
        // }, 5000)


// hide or show scrolls based on window width


    window.onresize = function(event) {

        if($('#row1').width() <= 650)  {
            binding.hide()
            binding2.hide()
            smallMarble.show()
            mediumMarble.hide()
            largeMarble.hide()
            // setInterval(textMarbleAll(hcSmTxt, smLogo), 3000)
            textMarbleAll(hcSmTxt, smLogo)
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