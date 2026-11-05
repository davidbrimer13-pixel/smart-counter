from microbit import *

# Choose a starting number with button A, then press button B to count down.
# The display can show the digits 1 through 9, so the counter wraps after 9.
start_number = 5

display.scroll("A SET B GO")
display.show(start_number)

while True:
    if button_a.was_pressed():
        start_number += 1
        if start_number > 9:
            start_number = 1
        display.show(start_number)

    if button_b.was_pressed():
        # Show each number for one second, ending at zero.
        for number in range(start_number, -1, -1):
            display.show(number)
            sleep(1000)

        display.show(Image.YES)
        sleep(1000)
        display.show(start_number)
