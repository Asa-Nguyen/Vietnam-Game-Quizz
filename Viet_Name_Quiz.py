import turtle
import pandas as pd
import tkinter as tk
from game_play import game

if __name__ == "__main__":
    turtle.title('Hello Tux')
    screen = turtle.Screen()
    screen.title("VietNam Quiz game")
    image = "Viet_Nam.gif"
    screen.addshape(image)
    turtle.shape(image)
    game()



