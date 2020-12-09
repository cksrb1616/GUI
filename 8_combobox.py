import tkinter.ttk as ttk # combobox library
from tkinter import *

root = Tk()
root.title("First GUI")
root.geometry("640x480") # 가로 * 세로

# listbox처럼 생겼는데 radio button처럼 하나만 선택 가능한 선택지창
# values 를 리스트로 추가했음
# 글자를 입력도 가능함 -> state="readonly" 로 읽기전용 처리
values = [str(i) + "일" for i in range(1, 32)] # 1 ~ 31 까지의 숫자
combobox = ttk.Combobox(root, height=5, values=values)
combobox.pack()
combobox.set("카드 결제일") # 최초 목록 제목 설정

readonly_combobox = ttk.Combobox(root, height=10, values=values, state="readonly") # 읽기전용
readonly_combobox.current(0) # 목록 제목이 아닌 0번째 인덱스 값 선택
readonly_combobox.pack()


def btncmd():
    print(combobox.get()) # 선택된 값 표시
    print(readonly_combobox.get())

btn = Button(root, text="선택", command=btncmd)
btn.pack()

root.mainloop()