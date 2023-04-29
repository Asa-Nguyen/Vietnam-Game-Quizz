import turtle
import pandas as pd
import tkinter as tk
from game_play import game
from quizz import quiz
from tkinter import StringVar
if __name__ == "__main__":
    turtle.title('Hello Tux')
    screen = turtle.Screen()
    screen.title("VietNam Quiz game")
    image = "Viet_Nam.gif"
    screen.addshape(image)
    turtle.shape(image)
    game()
    root = tk.Tk()
    root.geometry('1920x1080')

    questions = ["Bình Thuận nằm ở miền nào ?",
                 "Bình Định giáp tỉnh nào",
                 "Quảng Trị ở mô ?",
                 "Đắk Nông là gì của Đắk Lắk",
                 "Bến Tre có biển không? =))",
                 "Ninh Bình có giáp Ninh Thuận =))?",
                 "Đài truyền hình tỉnh nào khiến bao anh em game thủ mất ăn mất ngủ =)) ?",
                 "Khánh Hòa có thành phố biển nào ?",
                 "Biết Long An giáp thành phố Hồ Chí Minh, vậy Long An thuộc vùng nào ?",
                 "2 tỉnh thành nào có đường biên giới Việt Nam giáp với 2 quốc gia ?"
                 ]
    
    
    options = [['Miền Bắc','Miền Trung','Miền Nam','Bình Dương vô tận =))','Miền Trung'],
               ['Gia Lai - Quảng Ngãi - Phú Yên','Gia Lai - Quảng Ngãi - Quảng Nam','Quảng Trị - Quảng Ngãi - Quảng Nam','Bình Thuận - Bình Phước - Bình Dương','Gia Lai - Quảng Ngãi - Phú Yên'],
            ['Bắc','Nam','Bắc Trung Bộ','Nam Trung Bộ','Bắc Trung Bộ'],
            ['Là thành phố trực thuộc tỉnh Đắk Lắk','Hàng xóm phía nam','Là một','Hàng xóm phía Bắc','Hàng xóm phía nam'],
            ['Có','Không','Kó =))))','Cũng là không nhưng hàng xóm có','Có'],
            ['Có chứ tôi đã học bài kĩ lắm rồi','Có nhưng là có cái nịt =))',
             'Giáp Bắc Ninh chứ','Là một mà','Có nhưng là có cái nịt =))'],
            ['Cần Thơ','Vĩnh Long','Trà Vinh','Vĩnh Phúc','Vĩnh Long'],
            ['Phan Thiết','Quy Nhơn','Nha Trang','Tuy Hòa','Nha Trang'],
            ['Đồng bằng sông Cửu Long','Đông Nam Bộ','Tây Nguyên','Nam Trung Bộ','Đồng bằng sông Cửu Long'],
            ['Ninh Bình - Bình Định','Đắk Lắk - Ninh Thuận','Kon Tum - Điện Biên','Bình Định - Quảng Ngãi','Kon Tum - Điện Biên']
            ]
    


    frame = tk.Frame(root, padx=500, pady=200,bg='#fff')
    question_label = tk.Label(frame,height=5, width=40,bg='grey',fg="#fff", 
                            font=('Verdana', 20),wraplength=500)


    v1 = StringVar(frame)
    v2 = StringVar(frame)
    v3 = StringVar(frame)
    v4 = StringVar(frame)

    option1 = tk.Radiobutton(frame, bg="#fff", variable=v1, font=('Verdana', 20),
                            command = lambda : checkAnswer(option1))
    option2 = tk.Radiobutton(frame, bg="#fff", variable=v2, font=('Verdana', 20), 
                            command = lambda : checkAnswer(option2))
    option3 = tk.Radiobutton(frame, bg="#fff", variable=v3, font=('Verdana', 20), 
                            command = lambda : checkAnswer(option3))
    option4 = tk.Radiobutton(frame, bg="#fff", variable=v4, font=('Verdana', 20), 
                            command = lambda : checkAnswer(option4))

    button_next = tk.Button(frame, text='Next',bg='Orange', font=('Verdana', 20), 
                            command = lambda : displayNextQuestion())

    frame.pack(fill="both", expand="true")
    question_label.grid(row=0, column=0)

    option1.grid(sticky= 'W', row=1, column=0)
    option2.grid(sticky= 'W', row=2, column=0)
    option3.grid(sticky= 'W', row=3, column=0)
    option4.grid(sticky= 'W', row=4, column=0)

    button_next.grid(row=6, column=0)


    index = 0
    correct = 0

    # create a function to disable radiobuttons
    def disableButtons(state):
        option1['state'] = state
        option2['state'] = state
        option3['state'] = state
        option4['state'] = state


    # create a function to check the selected answer
    def checkAnswer(radio):
        global correct, index
        
        # the 4th item is the correct answer
        # we will check the user selected answer with the 4th item
        if radio['text'] == options[index][4]:
            correct +=1

        index +=1
        disableButtons('disable')


    # create a function to display the next question
    def displayNextQuestion():
        global index, correct

        if button_next['text'] == 'Restart The Quiz':
            correct = 0
            index = 0
            question_label['bg'] = 'grey'
            button_next['text'] = 'Next'

        if index == len(options):
            question_label['text'] = str(correct) + " / " + str(len(options))
            button_next['text'] = 'Restart The Quiz'
            if correct >= len(options)/2:
                question_label['bg'] = 'green'
            else:
                    question_label['bg'] = 'red'





        else:
            question_label['text'] = questions[index]
            
            disableButtons('normal')
            opts = options[index]
            option1['text'] = opts[0]
            option2['text'] = opts[1]
            option3['text'] = opts[2]
            option4['text'] = opts[3]
            v1.set(opts[0])
            v2.set(opts[1])
            v3.set(opts[2])
            v4.set(opts[3])

            if index == len(options) - 1:
                button_next['text'] = 'Check the Results'





    displayNextQuestion()

    root.mainloop()
    quiz()


