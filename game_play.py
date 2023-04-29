import turtle
import pandas as pd

from UI import get_province_input,animate_entry

def game(): 
    guessed_province = []
    while len(guessed_province) < 63 :
        answer = get_province_input()
        if(len(guessed_province) == 63 or answer == "Cancel"):
            break
        data = pd.read_csv("Viet_Nam.csv")
        all_VietNam_province = data.province.to_list()
        if answer in all_VietNam_province:
            if answer in guessed_province:
                pass
            else:
                guessed_province.append(answer)
            t = turtle.Turtle()
            t.hideturtle()
            t.penup()
            province_data = data[data.province == answer]
            t.goto(int(province_data.x),int(province_data.y))
            t.write(answer)          
        

    if answer == "":
        turtle.Screen().bye()
    turtle.mainloop()

