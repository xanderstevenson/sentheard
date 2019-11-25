$(document).ready(function () {

    // scrolls / pillars
    const binding = $("#binding")
    const binding2 = $("#binding2")
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
    // hide the 3 logos from the start or all three will display (see window.resize)
    smLogo.hide()
    mdLogo.hide()
    lgLogo.hide()
    // hide the 3 family images from the start or all three will display (see window.resize)
    smImg.hide()
    mdImg.hide()
    lgImg.hide()
    // flashing "Join for Free"
    const joinButton = $('.join-button')
    joinButton.hide()
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

    // mega function switching verses and images on homescreen and fading the logo
    const textMarbleAll = (marble, logo, image) => {

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
                return (marble.text + '<--- text present')
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

        setInterval(() => {
            $(logo).fadeIn(2500);
            image.attr('src', newImage)
            image.fadeIn(2500)
            joinButton.fadeIn(2500)
            joinButton.attr('src', freeButtonSwitch(), 1500)
            image.fadeOut(2500)
            marble.text(newText)
            $(logo).fadeOut(2500);
        }, 5000)

    }


    textMarbleAll(hcSmTxt, smLogo, smImg)
    textMarbleAll(hcMdTxt, mdLogo, mdImg)
    textMarbleAll(hcLgTxt, lgLogo, lgImg)

    // interval function to make flashing neon "Join for Free"



    //     const freeButtonSwitch = () => {

    //       if (joinButton.attr('src') == freeButtons[0]) {
    //         return (freeButtons[1])
    //     } else if (joinButton.attr('src') == freeButtons[1]) {
    //         return (freeButtons[0])
    //     } else {
    //         return (freeButtons[0])
    //     }

    // }

    // setInterval(() => {
    //     joinButton.attr('src', freeButtonSwitch, 1500)

    // })


    // show the correct marble frame based on screen size
    window.onresize = function (event) {

        if ($('#row1').width() <= 650) {
            binding.hide()
            binding2.hide()
            smallMarble.show()
            mediumMarble.hide()
            largeMarble.hide()
        } else if ($('#row1').width() > 650 && $('#row1').width() <= 1080) {
            binding.hide()
            binding2.hide()
            smallMarble.hide()
            mediumMarble.show()
            largeMarble.hide()
        } else if ($('#row1').width() > 1080) {
            binding.show()
            binding2.show()
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