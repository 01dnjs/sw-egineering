import tkinter as tk
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from PIL import Image, ImageTk
from tkinter import Tk, Frame

# 현재 테마 상태 변수
current_theme = "flatly"  # 기본 테마 (라이트 모드)

# 메인 윈도우 생성
root = ttk.Window(themename=current_theme)  # ttkbootstrap 사용
root.title("영단어 학습 프로그램")
root.geometry("400x600")  #320 450
root.resizable(False, False)

# 스타일 설정
style = ttk.Style()
style.configure("Placeholder.TEntry", foreground="gray")
style.configure("Normal.TEntry", foreground="black")

def quiz_menu():
    from quiz_interpret import quiz_interpret
    from quiz_four_choice import quiz_four_choice

    def go_to_menu():
        root.quit()
        #menu() 메뉴화면으로 이동하면서 현재 root는 종료

    # 홈 버튼 (오른쪽 상단)
    home_button = ttk.Button(root, text="🏠 홈", bootstyle="secondary", command=go_to_menu)
    home_button.pack(anchor="ne", padx=10, pady=10)

    # 옵션 선택 (OptionMenu)
    option_var = tk.StringVar(value="Category 1")
    options = ["Category 1", "Category 1", "Category 2", "Category 3", "Category 4"]

    #가젯 생성
    option_menu = ttk.OptionMenu(root, option_var, *options)
    option_menu.pack(pady=10)

    # 모드 선택 (OptionMenu)
    mode_var = tk.StringVar(value="Select Mode")
    modes = ["해석 맞추기", "해석 맞추기", "사지선다형 단어 맞추기", "산성비 게임", "문장 채우기 게임"]

    #이미지 불러오기
    image1 = Image.open("z.exampleForGame1.jpg")  # 불러올 이미지 경로
    image2 = Image.open("z.exampleForGame2.jpg")
    image3 = Image.open("z.exampleForGame3.jpg")
    image4 = Image.open("z.exampleForGame4.jpg")
    image1 = image1.resize((350, 300)) 
    image2 = image2.resize((350, 300)) 
    image3 = image3.resize((350, 300)) 
    image4 = image4.resize((350, 300)) 
    photo1 = ImageTk.PhotoImage(image1)  #tk에서 사용할 수 있게 변환
    photo2 = ImageTk.PhotoImage(image2)
    photo3 = ImageTk.PhotoImage(image3)
    photo4 = ImageTk.PhotoImage(image4)
    mode_explain = [photo1, photo2, photo3, photo4]

    # 모드 변경 시 그 모드에 대한 예시를 이미지로 출력
    def handle_mode_change(selected_mode):
        #인덱스 검색
        index = modes.index(selected_mode) - 1 #mode1이 중복되므로 하나 줄여야 함
        if (index < 0):
            index += 1
        
        label_display1.config(image= mode_explain[index])

    # OptionMenu 생성 시 command 추가
    mode_menu = ttk.OptionMenu(root, mode_var, *modes, command=handle_mode_change)
    mode_menu.pack(pady=10)

    # === ✅ 라벨을 위한 프레임 생성 ===
    style.configure("Custom.TFrame")  # 스타일 생성
    frame_display = ttk.Frame(root, style="Custom.TFrame")  # 스타일 적용
    frame_display.pack(pady=20)

    # 카테고리에 대한 라벨 생성 (초기값)
    label_display1 = ttk.Label(
        frame_display, 
        image=mode_explain[0],  # 모드에 따른 게임 예시. 초기 설정
        font=("나눔고딕", 16, "bold"),  # 글꼴 설정
        foreground="#3F7D58",
        bootstyle="info",  # 버튼 스타일
        wraplength=250,  # 텍스트가 자동으로 줄바꿈되도록 설정
        justify="center",  # 텍스트 중앙 정렬
        anchor="center",  # 텍스트 중앙 정렬
        borderwidth=2,  # 테두리 두께
        relief="raised" #테두리 스타일
    )
    label_display1.pack(pady=20, fill="both", expand=True)

    # 모드에 따라 다른 함수 실행
    def mode_1_function():
        quiz_interpret(root)

    def mode_2_function():
        quiz_four_choice(root)

    def mode_3_function():
        print("Mode 3 실행 중...")

    def mode_4_function():
        print("Mode 4 실행 중...")

    # Start 버튼 클릭 시 실행될 함수
    def start_button_clicked():
        selected_mode = mode_var.get()
        selected_category = option_var.get()
        
        print(f"Start 버튼 클릭됨! 선택된 카테고리: {selected_category}, 모드: {selected_mode}")

        if selected_mode == "해석 맞추기":
            mode_1_function()
        elif selected_mode == "사지선다형 단어 맞추기":
            mode_2_function()
        elif selected_mode == "산성비 게임":
            mode_3_function()
        elif selected_mode == "문장 채우기 게임":
            mode_4_function()
        else:
            print("올바른 모드를 선택해주세요.")

    # 시작 버튼 (맨 아래 배치)
    start_button = ttk.Button(root, text="시작", bootstyle="success", command=start_button_clicked)
    start_button.pack(pady=20, padx=150, fill="x")
    #root.bind("<Return>", lambda event: start_button_clicked()) #엔터키로 동작 가능


quiz_menu()

# Tkinter 이벤트 루프 실행
root.mainloop()
