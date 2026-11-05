# Microsoft MakeCode Python for micro:bit
# Press A to choose a start number from 1 to 9, then press B to count down.
# The tone gets higher as the displayed number gets lower.

start_number = 5


def play_number_tone(number, duration):
    # Lower numbers sound higher/brighter; higher numbers sound lower/deeper.
    frequency = 440 + (9 - number) * 55
    music.play_tone(frequency, duration)


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
    music.play_tone(988, 300)
    basic.pause(700)
    basic.show_number(start_number)


input.on_button_pressed(Button.A, on_button_pressed_a)
input.on_button_pressed(Button.B, on_button_pressed_b)

basic.show_string("A SET B GO")
basic.show_number(start_number)
