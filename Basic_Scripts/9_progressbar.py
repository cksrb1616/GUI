import time
import tkinter.ttk as ttk # progressbar 가져오기
from tkinter import *

root = Tk()
root.title("Nado GUI")
root.geometry("640x480") # 가로 * 세로

# 다운로드 초록색 왔다갔다 하는 창
# 다운로드 차오르는 창
# progressbar = ttk.Progressbar(root, maximum=100, mode="indeterminate") # 초록색이 왔다갔다 하는 탐색기 같은 느낌의 indeterminate
# progressbar = ttk.Progressbar(root, maximum=100, mode="determinate") # 다운로드 처럼 차오름 determinate
# progressbar.start(10) # 10 ms 마다 움직임
# progressbar.pack()

# def btncmd():
#     progressbar.stop() # 작동 중지

# btn = Button(root, text="중지", command=btncmd)
# btn.pack()

p_var2 = DoubleVar() # 소숫점이 있는 숫자를 반영하기 위해
progressbar2 = ttk.Progressbar(root, maximum=100, length=150, variable=p_var2)
progressbar2.pack()

def btncmd2():
    for i in range(1, 101): # 1 ~ 100
        time.sleep(0.01) # 0.01 초 대기

        p_var2.set(i) # progress bar 의 값 설정 100 가 다 차오른 그래프만 보임
        progressbar2.update() # ui 업데이트 i 가 동작할 때 마다 gui에 반영되서 천천히 올라가는게 보임
        print(p_var2.get())

btn = Button(root, text="시작", command=btncmd2)
btn.pack()

root.mainloop()