from Tkinter import *
import serial
import time

ard = serial.Serial('COM3', 115200)

def keyup(e):
    print 'up', e.char

def keydown(e):
    print 'down', e.char
    ard.write(e.char)

root = Tk()
frame = Frame(root, width=100, height=100)
frame.bind("<KeyPress>", keydown)
frame.bind("<KeyRelease>", keyup)
frame.pack()
frame.focus_set()
root.mainloop()
