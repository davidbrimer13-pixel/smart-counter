# Microsoft MakeCode Python for micro:bit
# Press A to choose a start number from 1 to 9, then press B to count down.
# Every buzzer tone is middle C (C4, 262 Hz).

start_number = 5
MIDDLE_C = 262


def play_number_tone(number, duration):
    music.play_tone(MIDDLE_C, duration)


def on_button_pressed_a():
    global start_number
    start_number += 1
    if start_number > 9:
        start_number = 1
    basic.show_number(start_number)
    play_number_tone(start_number, 180)


def on_button_pressed_b():
    global start_number
    for number in range(start_number, -1, -1):
        basic.show_number(number)
        play_number_tone(number, 700)
        basic.pause(300)

    basic.show_icon(IconNames.YES)
    play_number_tone(start_number, 300)
    basic.pause(700)
    basic.show_number(start_number)


input.on_button_pressed(Button.A, on_button_pressed_a)
input.on_button_pressed(Button.B, on_button_pressed_b)

basic.show_string("A SET B GO")
basic.show_number(start_number)
