import time
import random
from pynput.keyboard import Controller

def enter_commands(min_typing_speed=0.05, delay=1, counter_max=10):
    print("Please make Minecraft the active window, with the console active and blank.")
    for i in range(counter_max):
        print(f"Countdown: {counter_max-i} s", end=" \r")
        time.sleep(1)

    keyboard = Controller()

    with open("commands.txt", "r", encoding='utf-8') as file:
        for line in file:
            keyboard.press('/')
            time.sleep(min_typing_speed*(1+random.random()))
            keyboard.release('/')

            # type command
            for char in line:
                keyboard.type(char)
                print(char, end="")
                time.sleep(min_typing_speed*(1+random.random())) #NotABot
            
            # enter
            keyboard.press('\n')
            time.sleep(min_typing_speed*(1+random.random()))
            keyboard.release('\n')

            time.sleep(delay*(1+random.random()))

            # open chat
            keyboard.press('t')
            time.sleep(min_typing_speed*(1+random.random()))
            keyboard.release('t')

            time.sleep(delay*(1+random.random()))

if __name__ == "__main__":
    enter_commands()