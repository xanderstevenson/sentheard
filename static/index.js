
$(document).ready(function () {


    const joinInstructions = $("#join-instructions")
    const joinInstructWords = $("#join-instructions p")
    joinInstructions.css("display", "none")
    joinInstructWords.css("display", "none")
    // scrolls / pillars
    const binding = $("#binding")
    const binding2 = $("#binding2")
    binding.fadeOut(3000)
    binding2.fadeOut(3000)
    // rectangles of marble on home screen
    const smallMarble = $("#home-container")
    const mediumMarble = $("#home-container-md")
    const largeMarble = $("#home-container-lg")
    // hide the 3 marble frames from the start or all three will display (see window.resize)
    smallMarble.css("display", "none")
    mediumMarble.css("display", "none")
    largeMarble.css("display", "none")
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

    hcSmTxt.css("display", "none")
    hcMdTxt.css("display", "none")
    hcLgTxt.css("display", "none")

    // hide the 3 logos from the start or all three will display (see window.resize)
    smLogo.css("display", "none")
    mdLogo.css("display", "none")
    lgLogo.css("display", "none")
    // hide the 3 family images from the start or all three will display (see window.resize)
    smImg.css("display", "none")
    mdImg.css("display", "none")
    lgImg.css("display", "none")
    const handPrayLg = $('#hand-pray-lg')
    const handPrayMd = $('#hand-pray-md')
    const handPraySm = $('#hand-pray-sm')

    handPrayLg.css("display", "none")
    handPrayMd.css("display", "none")
    handPraySm.css("display", "none")

const theCloudTitle= $('#cloud-bg-title')
const theBanner= $('#banner')
const navBtn = $('.nav-btn')

const changeCloudTitleSides = ()=>{
    borders = ['border-left-color', 'border-top-color', 'border-right-color', 'border-bottom-color']
    let origColor = 'rgb(189, 161, 119)'
    let goldenRod = 'rgb(238, 232, 170)'
    for(let i=0; i < 4; i++){

        if(theCloudTitle.css(borders[i]) == origColor){
            theCloudTitle.css(borders[i], goldenRod).delay(3000)
            theCloudTitle.css('box-shadow', '2px 4px 22px rgb(238, 232, 170)').delay(3000)
            navBtn.css('box-shadow', '2px -4px 12px rgb(238, 232, 170)').delay(3000)
            theBanner.css('box-shadow', '0px 6px 42px rgb(238, 232, 170)').delay(3000)
            // theBanner.css('box-shadow', '0px 6px 12px rgb(65, 65, 58)').delay(3000)
            joinButton.css('box-shadow', '0px 4px 20px rgb(238, 232, 170)').delay(3000)
        }

        else {
          theCloudTitle.css(borders[i], origColor).delay(3000)
            theCloudTitle.css('box-shadow', '2px 4px 10px rgb(189, 161, 119)').delay(3000)
            navBtn.css('box-shadow', '2px -4px 12px rgb(189, 161, 119)').delay(3000)
            theBanner.css('box-shadow', '0px 6px 12px rgb(65, 65, 58)').delay(3000)
            // theBanner.css('box-shadow', '0px 6px 22px rgb(238, 232, 170)').delay(3000)
                        joinButton.css('box-shadow', '0px 4px 10px gray').delay(3000)
        }

    }
}
    // flashing "Join for Free"
    const joinButton = $('.join-button')
    joinButton.css("display", "none")

    // different texts for home screen rotation
    const verse = ['Record your stories with audio, video, images and text and pass them along to future generations.',
        'Create personalized momentos for your family, friends and descendants to cherish.',
        'We are the creator of, and world leader in, digital inheritance services.',
        'Share your past and recent memories with a select few, now, and for Eternity.'
    ]

    // different family images for homescreen
    const imageS = ['https://res.cloudinary.com/dx5eoz5dw/image/upload/v1574546898/SentHeard/family_computer-3gen.jpg',
        'https://res.cloudinary.com/dx5eoz5dw/image/upload/v1574552113/SentHeard/granma-granddaughter.jpg',
        'https://res.cloudinary.com/dx5eoz5dw/image/upload/v1574552114/SentHeard/asian-family-history.jpg',
        'https://res.cloudinary.com/dx5eoz5dw/image/upload/v1574717218/SentHeard/Family-Teach-Genealogy_xzfyvq.jpg'
    ]

    // different buttons for neon interval
    // const freeButtons = ["{% static '/images/landing_page/499-per-month.png'%}", "{% static '/images/landing_page/2ndFreeSign.png'%}"]

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


        setInterval(() => {


            marble.fadeTo(3000, 1, 'swing', () => {
                marble.fadeIn(3000)
            }).delay(2000)
            image.fadeTo(3000, 1, 'swing', () => {
                image.fadeIn(3000)
            }).delay(2000)
            joinButton.fadeTo(3000, 1, 'swing', () => {
                joinButton.fadeIn()

            }).delay(2000)
            logo.fadeTo(3000, 1, 'swing', () => {
                logo.fadeIn(3000)
            }).delay(2000)

        changeCloudTitleSides()


            marble.fadeTo(3000, 0, () => {
                marble.fadeOut();
                marble.text(newText)
            })
            image.fadeTo(3000, 0, () => {
                image.fadeOut();
                image.attr('src', newImage)
            })
            joinButton.fadeTo(3000, 1, () => {
                joinButton.fadeOut()

            })
            logo.fadeTo(3000, 0, () => {
                logo.fadeOut()
            });



        }, 3000)

    }


    textMarbleAll(hcSmTxt, smLogo, smImg, joinButton)
    textMarbleAll(hcMdTxt, mdLogo, mdImg, joinButton)
    textMarbleAll(hcLgTxt, lgLogo, lgImg, joinButton)

    // interval function to make flashing neon "Join for Free"




    // Fade in appropriate marble frame size on screen load

    window.onload = function (event) {
        // $('#title-box').toggleClass('titleBoxGlow')

        if ($('#row1').width() <= 650) {
            smallMarble.delay(3000).fadeIn(3000)
            mediumMarble.css("display", "none")
            largeMarble.css("display", "none")

        } else if ($('#row1').width() > 650 && $('#row1').width() <= 1080) {
            mediumMarble.delay(3000).fadeIn(3000)
            largeMarble.css("display", "none")
            smallMarble.css("display", "none")

        } else if ($('#row1').width() > 1080) {
            largeMarble.delay(3000).fadeIn(3000)
            smallMarble.css("display", "none")
            mediumMarble.css("display", "none")
        }
    }

    // show the correct marble frame based on screen size
    window.onresize = function (event) {
        if ($('#row1').width() <= 650) {
            smallMarble.show()
            mediumMarble.css("display", "none")
            largeMarble.css("display", "none")
        } else if ($('#row1').width() > 650 && $('#row1').width() <= 1080) {
            smallMarble.css("display", "none")
            mediumMarble.show()
            largeMarble.css("display", "none")
        } else if ($('#row1').width() > 1080) {
            smallMarble.css("display", "none")
            mediumMarble.css("display", "none")
            largeMarble.show()
        }
    }


    // hide scrolls if you click on them

    $('.bindings').click(() => {
        $('.bindings').hide()
    })



const gum = $('#gum')
const recorded = $('#recorded')

// gum.hide()



const start = $('#start')
const download = $('#download')
const play = $('#play')
const record = $('#record')
const tryAgain = $('#tryAgain')
const saveVid = $('#save')

record.hide()
play.hide()
download.hide()
tryAgain.hide()
saveVid.hide()
recorded.css('display', 'none')



const buttonPoppin = ()=>{

var start_count = 0

    start.click(()=>{
        start.css('display', 'none')
        record.show()
        gum.show()
        recorded.css('display', 'none')


            record.click(()=>{
            start.css('display', 'none')


                    record.click(()=>{
                        record.css("display", "none")
                        play.show()
                        download.show()
                        tryAgain.show()
                        saveVid.show()


                                play.click(()=> {
                                    gum.css("display", "none")
                                    recorded.show()
                                    play.css("display", "none")

                                })


                                tryAgain.click(()=>{
                                   location.reload();
                                })


                    })

            })

    })


}

buttonPoppin()


});