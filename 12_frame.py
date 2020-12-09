from tkinter import *

root = Tk()
root.title("First GUI")
root.geometry("640x480")

Label(root, text="Choose the Menu").pack(side="top")

Button(root, text="주문하기").pack(side="bottom")

# 메뉴 프레임
frame_burger = Frame(root, relief="solid", bd=1) # relief : 테두리모양, bd : 외각선 표시
frame_burger.pack(side="left", fill="both", expand=True) # 4방향 위치, 위아래 채우기, 좌우 채우기

Button(frame_burger, text="햄버거").pack() # root 가 아닌 frame_burger 에 넣기 때문
Button(frame_burger, text="치즈버거").pack()
Button(frame_burger, text="치킨버거").pack()

# 음료 프레임
frame_drink = LabelFrame(root, text="음료") # 제목이 있는 프레임
frame_drink.pack(side="right", fill="both", expand=True)

Button(frame_drink, text="콜라").pack()
Button(frame_drink, text="사이다").pack()

root.mainloop()