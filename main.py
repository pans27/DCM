from tkinter import *
from tkinter import messagebox
root=Tk()
root.title("Pacemaker User Terminal")
root.geometry("500x300+100+100")
login=Button(root)
login["text"]="Login"
login.pack()
register=Button(root)
register["text"]="Register"
register.pack()
def loginPressed(e):
    messagebox.showinfo("Message","type below")

login.bind("<Button-1>",loginPressed)
register.bind("<Button-1>",loginPressed)
root.mainloop()