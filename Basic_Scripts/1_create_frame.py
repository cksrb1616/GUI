from tkinter import *

a = Tk()
a.title("First GUI") # Title
a.geometry("640x480") # Size of the window
#a.geometry("640x480+300+100") # SIZE + x position + y position

a.resizable(False, False) # x너비 y높이 값 변경 불가 (창 크기)
a.mainloop() # keep the window opened

