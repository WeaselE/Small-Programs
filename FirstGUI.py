import tkinter as tk

#Window initialized
window = tk.Tk()

#Window 1 with just text
greeting = tk.Label(text="Hello World",
                    foreground="white",
                    background="black",
                    width=10,
                    height=3)
greeting.pack()
window.mainloop()

#Window 2 with just a button
button = tk.Button(text="Click Here",
                    foreground="black",
                    background="red",
                    height=4,
                    width=20)
button.pack()
window.mainloop()

#Window 3 Input Entry
entry = tk.Entry(foreground="black",
                background="blue",
                width=50)
entry.pack()
window.mainloop()

#Retrieval of entry currently not working, bug will be fixed later.
answer = entry.get()
print(answer)