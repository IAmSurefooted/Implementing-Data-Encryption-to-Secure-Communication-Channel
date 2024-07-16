#!/usr/bin/python3
# Author:
# 	Suraj Singh Bisht
#
import tkinter as Tkinter
import tkinter.ttk as ttk

PROGRAM_NAME = "Choose Program Mode"
text = """
Client Mode [Default]: Program will act like a chat client.
Server Mode: Program will wait for the client connection.
"""


def ask_ip_dialog():
    root = Tkinter.Tk(className=PROGRAM_NAME)
    mode = Tkinter.IntVar()
    mode.set(3)
    # 0 for Client Mode
    # 1 For Server Mode

    def out():
        root.destroy()
        return

    def mode_set(value):
        mode.set(value)
        out()
        return

    frame = ttk.LabelFrame(root, text="Choose Your Option")
    frame.pack(side='top', padx=10, pady=10, ipady=10, ipadx=10)
    ttk.Button(frame, text='Client Mode', command=lambda: mode_set(0)).grid(
        row=1, column=1, padx=10, pady=10)
    ttk.Button(frame, text='Server Mode', command=lambda: mode_set(1)).grid(
        row=1, column=2, padx=10, pady=10)
    ttk.Button(frame, text="Exit ", command=out).grid(row=1, column=3)
    # Description About Modes
    Label = Tkinter.Text(frame, width=60, height=4, font=('arial 8 italic'))
    Label.insert('1.0', text, 'end')
    Label.grid(row=3, column=1, columnspan=4, rowspan=5, padx=10, pady=10)
    Label.config(state='disabled')
    root.mainloop()
    return mode.get()


# Trigger For Script
if __name__ == '__main__':
    print(ask_ip_dialog())
