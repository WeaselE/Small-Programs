from tkinter import Label, mainloop, Tk, Button, Entry


def Clicked():
    lbl.configure(text=ent.get())


if __name__ == "__main__":
    root=Tk()
    root.geometry("480x240")
    root.title("This is my first program.")

    lbl = Label(root, text="Hello World!")
    lbl.grid()

    btn = Button(root, text="Click Me", fg="green", bg="black", command=Clicked)
    btn.grid(column=2, row=0)

    ent = Entry(root, width=20)
    ent.grid(column=1, row=0)

    mainloop()
