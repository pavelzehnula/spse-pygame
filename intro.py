import pgzrun

from bat import Bat
from conf import SCREEN_WIDTH, SCREEN_HEIGHT

WIDTH = SCREEN_WIDTH
HEIGHT = SCREEN_HEIGHT

bat = Bat()

press_keys = []


def update():
    if keys.LEFT in press_keys:
        bat.move_left()
    if keys.RIGHT in press_keys:
        bat.move_right()


def draw():
    screen.fill((255, 255, 255))
    bat.draw()


def on_key_down(key):
    press_keys.append(key)


def on_key_up(key):
    press_keys.remove(key)

pgzrun.go()













def on_key_down(key):
    bat.left += 10


