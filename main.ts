let Paper = false
let Rock = false
let Scissors = false
let _1 = false
let _3 = false
let _2 = false
let hand = 0
input.onButtonPressed(Button.A, function on_button_pressed_a() {
    
    Paper = true
    Rock = false
    Scissors = false
    if (_1 == Paper) {
        basic.showLeds(`
            . . . . .
            . . . . .
            # # # # #
            # # # # #
            . . . . .
            `)
    } else if (_3 == Paper) {
        basic.showLeds(`
            # . . . #
            . # . # .
            . . # . .
            . # . # .
            # . . . #
            `)
        soundExpression.sad.play()
    } else {
        basic.showIcon(IconNames.Yes)
        soundExpression.happy.play()
    }
    
})
input.onButtonPressed(Button.AB, function on_button_pressed_ab() {
    
    Scissors = true
    Paper = false
    Rock = false
    if (_3 == Scissors) {
        basic.showLeds(`
            . . . . .
            . . . . .
            # # # # #
            # # # # #
            . . . . .
            `)
    } else if (_2 == Scissors) {
        basic.showLeds(`
            # . . . #
            . # . # .
            . . # . .
            . # . # .
            # . . . #
            `)
        soundExpression.sad.play()
    } else {
        basic.showIcon(IconNames.Yes)
        soundExpression.happy.play()
    }
    
})
input.onButtonPressed(Button.B, function on_button_pressed_b() {
    
    Rock = true
    Scissors = false
    Paper = false
    if (_2 == Rock) {
        basic.showLeds(`
            . . . . .
            . . . . .
            # # # # #
            # # # # #
            . . . . .
            `)
    } else if (_1 == Rock) {
        basic.showLeds(`
            # . . . #
            . # . # .
            . . # . .
            . # . # .
            # . . . #
            `)
        soundExpression.sad.play()
    } else if (_3 == Rock) {
        basic.showIcon(IconNames.Yes)
        soundExpression.happy.play()
    }
    
})
input.onGesture(Gesture.Shake, function on_gesture_shake() {
    
    hand = randint(1, 3)
    if (hand == 1) {
        basic.showLeds(`
            # # # # #
            # . . . #
            # . . . #
            # . . . #
            # # # # #
            `)
        _1 = true
        _2 = false
        _3 = false
    } else if (hand == 2) {
        basic.showLeds(`
            . . . . .
            . # # # .
            . # # # .
            . # # # .
            . . . . .
            `)
        _2 = true
        _1 = false
        _3 = false
    } else {
        basic.showLeds(`
            # # . . #
            # # . # .
            . . # . .
            # # . # .
            # # . . #
            `)
        _3 = true
        _1 = false
        _2 = false
    }
    
})
