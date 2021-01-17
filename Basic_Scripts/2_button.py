from tkinter import *

root = Tk()
root.title("Nado GUI")

btn1 = Button(root, text="button1")
btn1.pack()

btn2 = Button(root, padx=5, pady=5, text="button2") # padx pady 글자와 버튼 테두리의 간격을 조절한다고 보면 됨
btn2.pack()

btn3 = Button(root, padx=10, pady=5, text="button3")
btn3.pack()

btn4 = Button(root, width=10, height=3, text="button_width_height") # 글자가 버튼 사이즈 보다 크면 글자가 짤림
btn4.pack()

btn5 = Button(root, fg="red", bg="yellow", text="button5") # fg :color of words, bg : background
btn5.pack()

photo = PhotoImage(file="../img.png")
btn6 = Button(root, image=photo)
btn6.pack()

def btncmd():
    print("Button is clicked")

btn7 = Button(root, text="Working Button", command=btncmd)
btn7.pack()

root.mainloop()