def on_button_pressed_a():
    global texto
    basic.show_leds("""
        . . . . .
        . # # # .
        . # # # .
        . # # # .
        . . . . .
        """)
    texto = "" + texto + "."
    music.play(music.create_sound_expression(WaveShape.SINE,
            5000,
            0,
            255,
            0,
            100,
            SoundExpressionEffect.NONE,
            InterpolationCurve.LINEAR),
        music.PlaybackMode.UNTIL_DONE)
    basic.pause(200)
    basic.clear_screen()
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_ab():
    global texto
    radio.send_string(texto)
    texto = ""
    music.play(music.create_sound_expression(WaveShape.SINE,
            1,
            5000,
            255,
            0,
            200,
            SoundExpressionEffect.NONE,
            InterpolationCurve.LINEAR),
        music.PlaybackMode.UNTIL_DONE)
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def on_received_string(receivedString):
    music.play(music.create_sound_expression(WaveShape.SINE,
            5000,
            1,
            255,
            0,
            200,
            SoundExpressionEffect.NONE,
            InterpolationCurve.LINEAR),
        music.PlaybackMode.UNTIL_DONE)
    basic.show_string(receivedString)
    if receivedString == ".-":
        basic.show_string("A")
    elif receivedString == "-...":
        basic.show_string("B")
    elif receivedString == "-.-.":
        basic.show_string("C")
    elif receivedString == "-..":
        basic.show_string("D")
    elif receivedString == ".":
        basic.show_string("E")
    elif receivedString == "..-.":
        basic.show_string("F")
    elif receivedString == "--.":
        basic.show_string("G")
    elif receivedString == "....":
        basic.show_string("H")
    elif receivedString == "..":
        basic.show_string("I")
    elif receivedString == ".---":
        basic.show_string("J")
    elif receivedString == "-.-":
        basic.show_string("K")
    elif receivedString == ".-..":
        basic.show_string("L")
    elif receivedString == "--":
        basic.show_string("M")
    elif receivedString == "-.":
        basic.show_string("N")
    elif receivedString == "---":
        basic.show_string("O")
    elif receivedString == ".--.":
        basic.show_string("P")
    elif receivedString == "--.-":
        basic.show_string("Q")
    elif receivedString == "-.-":
        basic.show_string("R")
    elif receivedString == "...":
        basic.show_string("S")
    elif receivedString == "-":
        basic.show_string("T")
    elif receivedString == "..-":
        basic.show_string("U")
    elif receivedString == "...-":
        basic.show_string("V")
    elif receivedString == ".--":
        basic.show_string("W")
    elif receivedString == "-..-":
        basic.show_string("X")
    elif receivedString == "-.--":
        basic.show_string("Y")
    elif receivedString == "--..":
        basic.show_string("Z")
    basic.pause(200)
    basic.clear_screen()
radio.on_received_string(on_received_string)

def on_button_pressed_b():
    global texto
    basic.show_leds("""
        . . . . .
        . . . . .
        . # # # .
        . . . . .
        . . . . .
        """)
    texto = "" + texto + "-"
    music.play(music.create_sound_expression(WaveShape.SINE,
            5000,
            35,
            255,
            0,
            300,
            SoundExpressionEffect.NONE,
            InterpolationCurve.LINEAR),
        music.PlaybackMode.UNTIL_DONE)
    basic.pause(200)
    basic.clear_screen()
input.on_button_pressed(Button.B, on_button_pressed_b)

texto = ""
radio.set_group(1)
radio.set_transmit_power(7)
texto = ""