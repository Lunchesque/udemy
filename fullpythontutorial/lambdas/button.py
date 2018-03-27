import tkinter as tk

root = tk.Tk()
frame = tk.Frame(root)
frame.pack()

# def say_hi():
#     print("HELLO!")

button1 = tk.Button(frame,
                    text="Say Hello",
                    fg="red",
                    command=lambda:print("Hello!"))

button2 = tk.Button(frame,
                    text="say Goodbye",
                    fg="red",
                    command=lambda:print("Goodbye"))

button1.pack(side=tk.LEFT)
button2.pack(side=tk.RIGHT)
root.mainloop()
