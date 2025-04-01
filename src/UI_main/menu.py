import tkinter as tk
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
#from quiz_menu import quiz_menu
#from vocab import vocab_window

def main_menu(root):
    from settings import settings_window

    def open_vocab():
    #vocab_window(root)
        print("")

    def open_quiz():
        print("")
        #quiz_menu(root)

    def open_settings():
        print("")
        settings_window(root)


    for widget in root.winfo_children():  # 기존 UI 제거
        widget.destroy()

    root.title("메인 메뉴")
    root.geometry("400x500")

    title_label = ttk.Label(root, text="메인 메뉴", font=("Arial", 18, "bold"), bootstyle="primary")
    title_label.pack(pady=20)

    vocab_button = ttk.Button(root, text="단어장", bootstyle="success", command=open_vocab)
    vocab_button.pack(pady=10, fill=X, padx=50)

    quiz_button = ttk.Button(root, text="퀴즈", bootstyle="info", command=open_quiz)  # 수정된 부분
    quiz_button.pack(pady=10, fill=X, padx=50)

    settings_button = ttk.Button(root, text="설정", bootstyle="warning", command=open_settings)
    settings_button.pack(pady=10, fill=X, padx=50)

    exit_button = ttk.Button(root, text="종료", bootstyle="danger", command=root.quit)
    exit_button.pack(pady=20)

# if __name__ == "__main__":
#     root = tk.Tk()
#     main_menu(root)
#     root.mainloop()


