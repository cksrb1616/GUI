from tkinter import *

root = Tk()
root.title("Nado GUI")
root.geometry("640x480") # 가로 * 세로

# listbox : 고를 수 있는 리스트 위젯
listbox = Listbox(root, selectmode="extended", height=0)
listbox.insert(0, "사과")
listbox.insert(1, "딸기")
listbox.insert(2, "바나나")
listbox.insert(END, "수박") # END를 통해 알아서 제일 뒤에 붙임
listbox.insert(END, "포도")
listbox.pack()

def btncmd():
    # 삭제
    #listbox.delete(0) # 맨 앞 항목을 삭제
    #listbox.delete(END) # 제일 뒤 목을 삭제

    # 갯수 확인
    #print("리스트에는", listbox.size(), "개가 있어요")

    # 항목 확인 (시작 idx, 끝 idx)
    #print("1번째부터 3번째까지의 항목 : ", listbox.get(0, 2))

    # 선택된 항목 확인 (index 값을 반환 (ex) (1, 2, 3) )
    print("선택된 항목 : ", listbox.curselection()) # current selection

btn = Button(root, text="클릭", command=btncmd)
btn.pack()

root.mainloop()