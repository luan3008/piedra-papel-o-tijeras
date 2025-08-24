Mano = 0

def on_gesture_shake():
    global Mano
    Mano = randint(1, 3)
    if Mano == 1:
        basic.show_icon(IconNames.SMALL_SQUARE)
    elif Mano == 2:
        basic.show_icon(IconNames.SQUARE)
    else:
        basic.show_icon(IconNames.SCISSORS)
input.on_gesture(Gesture.SHAKE, on_gesture_shake)
