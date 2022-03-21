
# https://realpython.com/python-gui-tkinter/

import tkinter as tk

matrice = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]
]

def handle_click(event):
    print("The button was clicked!", event, matrice)

window = tk.Tk()

for i in range(3):
    window.columnconfigure(i, weight=1, minsize=75)
    window.rowconfigure(i, weight=1, minsize=50)

    for j in range(0, 3):
        frame = tk.Frame(
            master=window,
            relief=tk.RAISED,
            borderwidth=0
        )
        frame.grid(row=i, column=j, padx=5, pady=5)
        button = tk.Button(master=frame,
                           bg="black",
                           fg="white",
                           text=f"Row {i}\nColumn {j}")
        button.bind("<Button-1>", handle_click)
        button.pack(padx=5, pady=5)
events_list = []


window.mainloop()