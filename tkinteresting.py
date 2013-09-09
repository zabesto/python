from Tkinter import *

form = Tk()
form.minsize(300,200)
form.title("myForm")
Label(form, text="my label", font='bold').pack()
Button(form, text="push", command=lambda x:x).pack(side=LEFT)
Button(form, text="off", command=lambda x:x).pack(side=BOTTOM)
form.mainloop()
