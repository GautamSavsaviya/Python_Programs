# Healthy Programmer
# 9am - 5pm
# Water - water.mp3 (3.5 litres) - Drank - log - Every 40 min
# Eyes - eyes.mp3 - every 30 min - EyDone - log - Every 30 min
# Physical activity - physical.mp3 every - 45 min - ExDone - log
# Rules
# Pygame module to play audio

from pygame import mixer
from datetime import datetime
from time import time


def play_alarm(file, stopper):
    mixer.init()
    mixer.music.load(file)
    mixer.music.play()
    while True:
        user_input = input()
        if user_input.lower() == stopper:
            mixer.music.stop()
            break


def log_data(name, msg):
    with open(f"{name.capitalize()}.txt", "a") as f:
        f.write(f"{msg.capitalize()} at {datetime.now()}\n")


if __name__ == '__main__':
    # play_alarm("water.mp3", 'stop')
    water_init_time = time()
    eye_init_time = time()
    execrise_init_time = time()
    water_alarm_sec = 40*60
    eye_alarm_sec = 30 * 60
    execrise_alarm_sec = 45 * 60
    print("Please, First enter your name: ", end="")
    user_name = input()

    while True:
        if time() - water_init_time > water_alarm_sec:
            print("Please drink the water.\nEnter 'drank' for stopping alarm")
            play_alarm("alarm.wav", "drank")
            water_init_time = time()
            log_data(f"{user_name.capitalize()} Activities Log", "Drink water")

        if time() - eye_init_time > eye_alarm_sec:
            print("Please relax some time your eyes.\nEnter 'eye done' for stopping alarm")
            play_alarm("alarm.wav", "eye done")
            eye_init_time = time()
            log_data(f"{user_name.capitalize()} Activities Log", "Relax my eyes")

        if time() - execrise_init_time > execrise_alarm_sec:
            print("Please do some execrise for relax your body.\nEnter 'execrise done' for stopping alarm")
            play_alarm("alarm.wav", "execrise done")
            execrise_init_time = time()
            log_data(f"{user_name.capitalize()} Activities Log", "Execrise done")

