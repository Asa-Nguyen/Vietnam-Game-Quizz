from tkinter import *
def quiz():
    root = Tk()
    root.geometry('1920x1080')
    root.title("Lời nhắn nhủ")
    root['bg'] = 'red'
    label_1 = Label(root,text="Đúng hay sai bao nhiêu câu không quan trọng",font = ('Arial',50),bg="yellow")
    label_1.place(x = 50, y = 50)
    label_2 = Label(root,text="Quan trọng là nhân ngày này Ad muốn ",font = ('Arial',50),bg="yellow")
    label_2.place(x = 50, y = 150)
    label_3 = Label(root,text="Chỉ cần là công dân Việt Nam ",font = ('Arial',50),bg="yellow")
    label_3.place(x = 50, y = 250)
    label_4 = Label(root,text="Ta đùm bọc, yêu thương, giúp đỡ nhau ",font = ('Arial',50),bg="yellow")
    label_4.place(x = 50, y = 350)
    label_5 = Label(root,text="Chúc mọi người 30/04 thật hạnh phúc bên gia đình",font = ('Arial',50),bg="yellow")
    label_5.place(x = 50, y = 450)

    root.mainloop()