# Microsoft MakeCode Python for micro:bit
# Press A to choose a start number from 1 to 9, then press B to count down.

start_number = 5


def on_button_pressed_a():
    global start_number
    start_number += 1
    if start_number > 9:
        start_number = 1
    basic.show_number(start_number)


def on_button_pressed_b():
    global start_number
    for number in range(start_number, -1, -1):
        basic.show_number(number)
        basic.pause(1000)

    basic.show_icon(IconNames.YES)
    basic.pause(1000)
    basic.show_number(start_number)


input.on_button_pressed(Button.A, on_button_pressed_a)
input.on_button_pressed(Button.B, on_button_pressed_b)

basic.show_string("A SET B GO")
basic.show_number(start_number)
