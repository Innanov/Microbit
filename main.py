Paper = False
Rock = False
Scissors = False
_1 = False
_3 = False
_2 = False
hand = 0

def on_button_pressed_a():
    global Paper, Rock, Scissors
    Paper = True
    Rock = False
    Scissors = False
    if _1 == Paper:
        basic.show_leds("""
            . . . . .
            . . . . .
            # # # # #
            # # # # #
            . . . . .
            """)
    elif _3 == Paper:
        basic.show_leds("""
            # . . . #
            . # . # .
            . . # . .
            . # . # .
            # . . . #
            """)
        soundExpression.sad.play()
    else:
        basic.show_icon(IconNames.YES)
        soundExpression.happy.play()
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_ab():
    global Scissors, Paper, Rock
    Scissors = True
    Paper = False
    Rock = False
    if _3 == Scissors:
        basic.show_leds("""
            . . . . .
            . . . . .
            # # # # #
            # # # # #
            . . . . .
            """)
    elif _2 == Scissors:
        basic.show_leds("""
            # . . . #
            . # . # .
            . . # . .
            . # . # .
            # . . . #
            """)
        soundExpression.sad.play()
    else:
        basic.show_icon(IconNames.YES)
        soundExpression.happy.play()
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def on_button_pressed_b():
    global Rock, Scissors, Paper
    Rock = True
    Scissors = False
    Paper = False
    if _2 == Rock:
        basic.show_leds("""
            . . . . .
            . . . . .
            # # # # #
            # # # # #
            . . . . .
            """)
    elif _1 == Rock:
        basic.show_leds("""
            # . . . #
            . # . # .
            . . # . .
            . # . # .
            # . . . #
            """)
        soundExpression.sad.play()
    elif _3 == Rock:
        basic.show_icon(IconNames.YES)
        soundExpression.happy.play()
input.on_button_pressed(Button.B, on_button_pressed_b)

def on_gesture_shake():
    global hand, _1, _2, _3
    hand = randint(1, 3)
    if hand == 1:
        basic.show_leds("""
            # # # # #
            # . . . #
            # . . . #
            # . . . #
            # # # # #
            """)
        _1 = True
        _2 = False
        _3 = False
    elif hand == 2:
        basic.show_leds("""
            . . . . .
            . # # # .
            . # # # .
            . # # # .
            . . . . .
            """)
        _2 = True
        _1 = False
        _3 = False
    else:
        basic.show_leds("""
            # # . . #
            # # . # .
            . . # . .
            # # . # .
            # # . . #
            """)
        _3 = True
        _1 = False
        _2 = False
input.on_gesture(Gesture.SHAKE, on_gesture_shake)
