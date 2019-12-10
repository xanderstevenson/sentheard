$(document).ready(function () {


    // scrolls / pillars
    const binding = $("#binding")
    const binding2 = $("#binding2")
    binding.fadeOut(4000)
    binding2.fadeOut(4000)
    // rectangles of marble on home screen
    const smallMarble = $("#home-container")
    const mediumMarble = $("#home-container-md")
    const largeMarble = $("#home-container-lg")
    // hide the 3 marble frames from the start or all three will display (see window.resize)
    smallMarble.hide()
    mediumMarble.hide()
    largeMarble.hide()
    // home container text
    const hcSmTxt = $('#hc-sm-txt')
    const hcMdTxt = $('#hc-md-txt')
    const hcLgTxt = $('#hc-lg-txt')
    // gold SentHeard logo
    const smLogo = $('#logo-sm')
    const mdLogo = $('#logo-md')
    const lgLogo = $('#logo-lg')
    // images on families on home screen
    const smImg = $('#smImg')
    const mdImg = $('#mdImg')
    const lgImg = $('#lgImg')

    hcSmTxt.css('visibility', 'hidden')
    hcMdTxt.css('visibility', 'hidden')
    hcLgTxt.css('visibility', 'hidden')

    // hide the 3 logos from the start or all three will display (see window.resize)
    smLogo.css('visibility', 'hidden')
    mdLogo.css('visibility', 'hidden')
    lgLogo.css('visibility', 'hidden')
    // hide the 3 family images from the start or all three will display (see window.resize)
    smImg.css('visibility', 'hidden')
    mdImg.css('visibility', 'hidden')
    lgImg.css('visibility', 'hidden')
    // praying hands image
    const handPrayLg = $('#hand-pray-lg')
    const handPrayMd = $('#hand-pray-md')
    const handPraySm = $('#hand-pray-sm')

    // flashing "Join for Free"
    const joinButton = $('.join-button')
    joinButton.css('visibility', 'hidden')
    // const joinButtonSm = $('#join-buttonSm')
    // const joinButtonMd = $('#join-buttonMd')
    // const joinButtonLg = $('#join-buttonLg')
    // different texts for home screen rotation
    const verse = ['Record your stories with audio, video, images and text and pass them along to future generations.',
        'Create personalized momentos for your family, friends and descendants to cherish.',
        'We are the creator of, and world leader in, digital inheritance services.',
        'Now, more than ever, between heaven and earth, we can be centered.'
    ]

    // different family images for homescreen
    const imageS = ['https://res.cloudinary.com/dx5eoz5dw/image/upload/v1574546898/SentHeard/family_computer-3gen.jpg',
        'https://res.cloudinary.com/dx5eoz5dw/image/upload/v1574552113/SentHeard/granma-granddaughter.jpg',
        'https://res.cloudinary.com/dx5eoz5dw/image/upload/v1574552114/SentHeard/asian-family-history.jpg',
        'https://res.cloudinary.com/dx5eoz5dw/image/upload/v1574717218/SentHeard/Family-Teach-Genealogy_xzfyvq.jpg'
    ]

    // different buttons for neon interval
    const freeButtons = ['https://res.cloudinary.com/dx5eoz5dw/image/upload/v1574717416/SentHeard/free-button-black-gold_black.png',
        'https://res.cloudinary.com/dx5eoz5dw/image/upload/v1574717415/SentHeard/free-button-black-fun.png'
    ]

const homeContainers = $('.home-containers')


    // mega function switching verses and images on homescreen and fading the logo
    const textMarbleAll = (marble, logo, image, joinButton) => {

        const newText = () => {

            if (marble.text.length == 0 || marble.text() == '') {
                return (verse[0])
            } else if (marble.text() == verse[0]) {
                return (verse[1])
            } else if (marble.text() == verse[1]) {
                return (verse[2])
            } else if (marble.text() == verse[2]) {
                return (verse[3])
            } else if (marble.text() == verse[3]) {
                return (verse[0])
            } else {
                return (verse[0])
            }

        }


        const newImage = () => {
            if (image.attr('src') == '') {
                return (imageS[0])
            } else if (image.attr('src') == imageS[0]) {
                return (imageS[1])
            } else if (image.attr('src') == imageS[1]) {
                return (imageS[2])
            } else if (image.attr('src') == imageS[2]) {
                return (imageS[3])
            } else if (image.attr('src') == imageS[3]) {
                return (imageS[0])
            } else {
                return (imageS[0])
            }
        }


        const freeButtonSwitch = () => {

          if (joinButton.attr('src') == freeButtons[0]) {
            return (freeButtons[1])
        } else if (joinButton.attr('src') == freeButtons[1]) {
            return (freeButtons[0])
        } else {
            return (freeButtons[0])
        }

    }



setInterval((event) => {


    marble.fadeTo(2500, 1, 'swing', ()=> { marble.css('visibility', 'visible')  }).delay(2000)
    image.fadeTo(2500, 1, 'swing', ()=>{ image.css("visibility", "visible")  }).delay(2000)
    joinButton.fadeTo(2500, 1, 'swing', ()=>{ joinButton.css("visibility", "visible")  }).delay(2000)
    logo.fadeTo(2500, 1, 'swing', ()=>{ logo.css('visibility', 'visible') } ).delay(2000)

    marble.fadeTo(2000, 0, ()=> { marble.css('visibility', 'hidden'); marble.text(newText)  })
    image.fadeTo(2000, 0, ()=>{ image.css("visibility", "hidden"); image.attr('src', newImage)  })
    joinButton.fadeTo(2000, 1, ()=>{ joinButton.attr("src", freeButtonSwitch) ; joinButton.css("visibility", "visible") })
    logo.fadeTo(2000, 0, ()=>{ logo.css('visibility', 'hidden')} );



}, 1000)

    }


    textMarbleAll(hcSmTxt, smLogo, smImg, joinButton)
    textMarbleAll(hcMdTxt, mdLogo, mdImg, joinButton)
    textMarbleAll(hcLgTxt, lgLogo, lgImg, joinButton)

    // interval function to make flashing neon "Join for Free"




// Fade in appropriate marble frame size on screen load

    window.onload = function (event) {
        $('#title-box').toggleClass('titleBoxGlow')

        if ($('#row1').width() <= 650) {
            // binding.hide()
            // binding2.hide()
            smallMarble.fadeIn(2000)
            mediumMarble.hide()
            largeMarble.hide()
            handPraySm.fadeIn(1750).fadeOut(1250)
        } else if ($('#row1').width() > 650 && $('#row1').width() <= 1080) {
            // binding.hide()
            // binding2.hide()
            smallMarble.hide()
            mediumMarble.fadeIn(2000)
            largeMarble.hide()
            handPrayMd.fadeIn(1750).fadeOut(1250)
        } else if ($('#row1').width() > 1080) {
            // binding.show()
            // binding2.show()
            smallMarble.hide()
            mediumMarble.hide()
            largeMarble.fadeIn(2000)
            handPrayLg.fadeIn(1750).fadeOut(1250)
        }
    }

    // show the correct marble frame based on screen size
    window.onresize = function (event) {
        if ($('#row1').width() <= 650) {
            // binding.hide()
            // binding2.hide()
            smallMarble.show()
            mediumMarble.hide()
            largeMarble.hide()
        } else if ($('#row1').width() > 650 && $('#row1').width() <= 1080) {
            // binding.hide()
            // binding2.hide()
            smallMarble.hide()
            mediumMarble.show()
            largeMarble.hide()
        } else if ($('#row1').width() > 1080) {
            // binding.show()
            // binding2.show()
            smallMarble.hide()
            mediumMarble.hide()
            largeMarble.show()
        }
    }


    // hide scrolls if you click on them

    $('.bindings').click(() => {
        $('.bindings').hide()
    })



});