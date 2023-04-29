from tkinter import *
def quiz():
    root = Tk()
    root.title("Question")
    root['bg'] = 'dark blue'
    label_t = Label(root,text = 'Quiz', font = ('JetBrains Mono',50), bg="dark blue" )
    label_t.place(x = 700, y = 50)

    label1 = Label(root,text = 'Username: ', font = ('JetBrains Mono',50), bg="dark blue" )
    label1.place(x = 250, y = 275)
    entry_1 = Entry(root,font=('JetBrains Mono', 30))
    entry_1.place(x = 650,y = 300)
    button = Button(root,text='Submit',font=('JetBrains Mono', 30))
    root.mainloop()