from lib2to3.pgen2.tokenize import TokenError
import tkinter
import tkinter.font as font
import function


app = tkinter.Tk()
app.geometry("300x165")
app.title("Among Cheat")
app.maxsize(300, 165)
app.minsize(300, 165)
app.iconbitmap("src/icon.ico")
police = font.Font(family='Courier', size=10)

img = tkinter.PhotoImage(file="src/background.png")
bg = tkinter.Label(app,image=img)
bg.place(x=-2, y=-1)

speedvalue = tkinter.Entry(app)
speedvalue.place(x=92, y=60)

setspeedButton = tkinter.Button(app, text="Set speed.", command=lambda: function.speedhack(speedvalue.get()))
setspeedButton.place(x=110, y=100)
setspeedButton['font'] = police

author = tkinter.Label(app, text="by akira :)", background="black", fg="white")
author.place(x=220, y=145)
author['font'] = font.Font(family='Courier', size=8)



app.mainloop()