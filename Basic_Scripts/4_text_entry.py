from tkinter import *

root = Tk()
root.title("Nado GUI")
root.geometry("640x480")

# blank text box to input text will be generated
txt = Text(root, width=30, height=5)
txt.pack()
txt.insert(END, "Input the texts")

e = Entry(root, width=30) # cannot do "enter". It's for only one line. So for ID or Passwords
e.pack()
e.insert(0, "Only one line string is possible")

def btncmd():
    # 내용 출력
    print(txt.get("1.0", END)) # 1 : 첫번째 라인, 0 : 0번째 column 위치에서 부터 끝(END) 까지 가져와라
    print(e.get()) # entry 는 간단하게 가져올 수 있음

    # 내용 삭제
    txt.delete("1.0", END)
    e.delete(0, END)

btn = Button(root, text="클릭", command=btncmd)
btn.pack()

root.mainloop()