from convert_image import create_commands
from command_input import enter_commands
import playsound
import argparse
import time

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("image_path", type=str, default="data/dog.jpg", help="A POSIX-compatible path to the 3-channel image that must be printed.")
    parser.add_argument("n", type=int, default=10, help="The number of blocks to use for the shorter edge of the image.")
    parser.add_argument("--starting_coordinates", type=int, nargs=2, default=(0, 0), help="Starting x and z coordinates for printing (default: (0, 0)).")
    parser.add_argument("--counter_max", type=int, default=10, help="The number of seconds to count down before commands begin to be typed (default: 10).")
    parser.add_argument("--min_typing_speed", type=float, default=0.001, help="Minimum time between successive keystrokes in seconds (default: 0.001).")
    parser.add_argument("--delay", type=float, default=0.2, help="Time delay between input of successive commands in seconds (default: 0.2).")
    parser.add_argument("-y", type=int, default=-60, help="Y-coordinate for printing (default: -60).")

    args = parser.parse_args()

    image_path = args.image_path
    n = args.n
    starting_coordinates = tuple(args.starting_coordinates)
    y = args.y
    min_typing_speed = args.min_typing_speed
    delay = args.delay
    counter_max = args.counter_max

    create_commands(n, image_path, starting_coordinates, y)
    enter_commands(min_typing_speed, delay, counter_max)
    print("End")
    for i in range(3):
        playsound.playsound("data/buzzer.mp3")
        time.sleep(0.5)