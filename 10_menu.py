from tkinter import *

root = Tk()
root.title("First GUI")
root.geometry("640x480") # 가로 * 세로

def create_new_file():
    print("새 파일을 만듭니다.")

menu = Menu(root)
# 제일 밑의
# root.config(menu=menu)
# root.mainloop()
# 이 세 문장으로 기본 포맷은 완

def create_new_file():
    print("creat a new file.")
# File 메뉴
menu_file = Menu(menu, tearoff=0)
menu_file.add_command(label="New File", command=create_new_file)
menu_file.add_command(label="New Window")
menu_file.add_separator() # 구분자 (실선) 추가함
menu_file.add_command(label="Open File...")
menu_file.add_separator()
menu_file.add_command(label="Save All", state="disable") # 비활성화
menu_file.add_separator()
menu_file.add_command(label="Exit", command=root.quit)
menu.add_cascade(label="File", menu=menu_file) # 하부 메뉴에 만들어 둔 menu_file을 붙여넣는 File 이라는 메뉴 형성

# Edit 메뉴 (빈 값)
menu.add_cascade(label="Edit")

# Language 메뉴 추가 (radio 버튼을 통해서 택1)
menu_lang = Menu(menu, tearoff=0)
menu_lang.add_radiobutton(label="Python") # 라이도버튼 형성
menu_lang.add_radiobutton(label="Java")
menu_lang.add_radiobutton(label="C++")
menu.add_cascade(label="Language", menu=menu_lang)

# View 메뉴
menu_view = Menu(menu, tearoff=0)
menu_view.add_checkbutton(label="Show Minimap") # 체크가 가능한 메뉴항목 형성
menu.add_cascade(label="View", menu=menu_view)

root.config(menu=menu)
root.mainloop()