from tkinter import *

root = Tk()
root.title("First GUI")
root.geometry("640x480")

frame = Frame(root) # 프레임으로 관리하는 것이 편함
frame.pack()

scrollbar = Scrollbar(frame)
scrollbar.pack(side="right", fill="y") # 리스트박스 오른쪽에 스크롤바가 붙음 fill 로 상하 길이 맞춰서 채우기

# set 이 없으면 스크롤을 내려도 다시 올라옴 ####
listbox = Listbox(frame, selectmode="extended", height=10, yscrollcommand = scrollbar.set) # yscrollcommand: 스크롤바 집어넣겠다

for i in range(1, 32): # 1 ~ 31 일
    listbox.insert(END, str(i) + "일") # 1일, 2일, ...
listbox.pack(side="left")

scrollbar.config(command=listbox.yview) # 스크롤바 와 리스트 박스가 맞춰서 움직일 수 있도록 맵핑 이 커멘드 없이는 스크롤을 내릴 수가 없음
# 리스트박스가 내려감에 따라 스크롤일 내려갈뿐 스크롤을 내려서 조정할 수는 없음

root.mainloop()