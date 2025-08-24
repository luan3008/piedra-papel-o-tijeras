let Mano = 0
input.onGesture(Gesture.Shake, function on_gesture_shake() {
    
    Mano = randint(1, 3)
    if (Mano == 1) {
        basic.showIcon(IconNames.SmallSquare)
    } else if (Mano == 2) {
        basic.showIcon(IconNames.Square)
    } else {
        basic.showIcon(IconNames.Scissors)
    }
    
})
