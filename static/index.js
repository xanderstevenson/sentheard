

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

    const smLogo = $('#logo-sm')
    const mdLogo = $('#logo-md')
    const lgLogo = $('#logo-lg')

    const smImg = $('#smImg')
    const mdImg = $('#mdImg')
    const lgImg = $('#lgImg')



    smLogo.hide()
    mdLogo.hide()
    lgLogo.hide()

    smImg.hide()
    mdImg.hide()
    lgImg.hide()



        const verse = ['Record your Stories in Audio, Video, Images and Text to pass along to future generations.',
            'Create Personalized Momentos for your family, friends and descendants to cherish.',
            'We are the Creator of, and World Leader in, Digital Inheritance Services.',
            'Finally, somewhere between Heaven and Earth...you and your loved ones, can be centered.']


        const imageS = ['https://res.cloudinary.com/dx5eoz5dw/image/upload/v1574546898/SentHeard/family_computer-3gen.jpg',
        'https://res.cloudinary.com/dx5eoz5dw/image/upload/v1574552113/SentHeard/granma-granddaughter.jpg',
        'https://res.cloudinary.com/dx5eoz5dw/image/upload/v1574552114/SentHeard/asian-family-history.jpg',
        'https://res.cloudinary.com/dx5eoz5dw/image/upload/c_scale,h_517/v1574568249/SentHeard/Family-Teach-Genealogy.jpg']


const textMarbleAll = (marble, logo, image)=>{

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


        const newImage = ()=> {
            if(image.attr('src') == ''){
                return(imageS[0])
            }
            else if(image.attr('src') == imageS[0]){
                return(imageS[1])
            }
            else if(image.attr('src') == imageS[1]){
                return(imageS[2])
            }
            else if(image.attr('src') == imageS[2]){
                return(imageS[3])
            }
            else if(image.attr('src') == imageS[3]){
                return(imageS[0])
            }
            else {
                return(imageS[0])
            }
        }


        setInterval(()=>{
            $(logo).fadeIn(2500);
            image.attr('src',newImage())
            image.fadeIn(2500)
            marble.text(newText())
            image.fadeOut(2500)
            $(logo).fadeOut(2500);
        }, 5000)
}

textMarbleAll(hcSmTxt, smLogo, smImg)
textMarbleAll(hcMdTxt, mdLogo, mdImg)
textMarbleAll(hcLgTxt, lgLogo, lgImg)



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