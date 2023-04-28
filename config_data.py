import pandas as pd
import turtle
data = pd.read_csv("Viet_Nam.csv")
print(data)

def get_mouse_click(x,y):
    print(x,y)
    
turtle.onscreenclick(get_mouse_click)
screen = turtle.Screen()
screen.title("VietNam Quiz game")
image = "Viet_Nam.gif"
screen.addshape(image)
turtle.shape(image)
turtle.mainloop()