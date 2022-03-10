from tkinter import *
import random

GAME_WIDTH = 700
GAME_HEIGHT = 700
SPEED = 100
SPACE_SIZE = 50
BODY_PARTS = 3
SNAKE_COLOR = "#FFFFFF"
FOOD_COLOR = "#FFFF00"
BACKGROUND_COLOR = "#0000FF"

class Snake:
    pass

class Food:
    pass

def next_turn():
    pass

def change_direction():
    pass

def check_collisions():
    pass

def game_over():
    pass

window = Tk()
window.title("Snake Game")
window.resizable(False, False)

score = 0
direction = "down"

label = Label(text="Score: {}".format(score), font=("consolas", 20))
label.pack()

canvas = Canvas(window, width=GAME_WIDTH, height=GAME_HEIGHT, bg=BACKGROUND_COLOR)
canvas.pack()

window.update()

window_width = window.winfo_width()
window_height = window.winfo_height()
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

x = int((screen_width/2) - (window_width/2))
y = int((screen_height/2) - (window_height/2))

window.geometry(f"{window_width}x{window_height}+{x}+{y}")

window.mainloop()