input.onButtonPressed(Button.A, function () {
    basic.showLeds(`
        . . . . .
        . # # # .
        . # # # .
        . # # # .
        . . . . .
        `)
    texto = "" + texto + "."
    music.play(music.createSoundExpression(WaveShape.Sine, 5000, 0, 255, 0, 100, SoundExpressionEffect.None, InterpolationCurve.Linear), music.PlaybackMode.UntilDone)
    basic.pause(200)
    basic.clearScreen()
})
input.onButtonPressed(Button.AB, function () {
    radio.sendString(texto)
    texto = ""
    music.play(music.createSoundExpression(WaveShape.Sine, 1, 5000, 255, 0, 200, SoundExpressionEffect.None, InterpolationCurve.Linear), music.PlaybackMode.UntilDone)
})
radio.onReceivedString(function (receivedString) {
    music.play(music.createSoundExpression(WaveShape.Sine, 5000, 1, 255, 0, 200, SoundExpressionEffect.None, InterpolationCurve.Linear), music.PlaybackMode.UntilDone)
    basic.showString(receivedString)
    if (receivedString == ".-") {
        basic.showString("A")
    } else if (receivedString == "-...") {
        basic.showString("B")
    } else if (receivedString == "-.-.") {
        basic.showString("C")
    } else if (receivedString == "-..") {
        basic.showString("D")
    } else if (receivedString == ".") {
        basic.showString("E")
    } else if (receivedString == "..-.") {
        basic.showString("F")
    } else if (receivedString == "--.") {
        basic.showString("G")
    } else if (receivedString == "....") {
        basic.showString("H")
    } else if (receivedString == "..") {
        basic.showString("I")
    } else if (receivedString == ".---") {
        basic.showString("J")
    } else if (receivedString == "-.-") {
        basic.showString("K")
    } else if (receivedString == ".-..") {
        basic.showString("L")
    } else if (receivedString == "--") {
        basic.showString("M")
    } else if (receivedString == "-.") {
        basic.showString("N")
    } else if (receivedString == "---") {
        basic.showString("O")
    } else if (receivedString == ".--.") {
        basic.showString("P")
    } else if (receivedString == "--.-") {
        basic.showString("Q")
    } else if (receivedString == "-.-") {
        basic.showString("R")
    } else if (receivedString == "...") {
        basic.showString("S")
    } else if (receivedString == "-") {
        basic.showString("T")
    } else if (receivedString == "..-") {
        basic.showString("U")
    } else if (receivedString == "...-") {
        basic.showString("V")
    } else if (receivedString == ".--") {
        basic.showString("W")
    } else if (receivedString == "-..-") {
        basic.showString("X")
    } else if (receivedString == "-.--") {
        basic.showString("Y")
    } else if (receivedString == "--..") {
        basic.showString("Z")
    }
    basic.pause(200)
    basic.clearScreen()
})
input.onButtonPressed(Button.B, function () {
    basic.showLeds(`
        . . . . .
        . . . . .
        . # # # .
        . . . . .
        . . . . .
        `)
    texto = "" + texto + "-"
    music.play(music.createSoundExpression(WaveShape.Sine, 5000, 35, 255, 0, 300, SoundExpressionEffect.None, InterpolationCurve.Linear), music.PlaybackMode.UntilDone)
    basic.pause(200)
    basic.clearScreen()
})
let texto = ""
radio.setGroup(1)
radio.setTransmitPower(7)
texto = ""
