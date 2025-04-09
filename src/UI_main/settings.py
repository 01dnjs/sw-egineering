import tkinter as tk
import ttkbootstrap as ttk
from ttkbootstrap.constants import *

from login import sign_login # ✅ 로그인 함수 import

user_info = {
    "name": "홍길동",
    "email": "example@email.com",
    "password": "1234"
}

def toggle_dark_mode(root):
    style = ttk.Style()
    current_theme = style.theme_use()
    new_theme = "darkly" if current_theme == "flatly" else "flatly"
    style.theme_use(new_theme)

def settings_window(root):
    for widget in root.winfo_children():
        widget.destroy()
    root.title("설정")

    label = ttk.Label(root, text="설정 화면", font=("Arial", 18, "bold"), bootstyle="primary")
    label.pack(pady=20)

    info_frame = ttk.Frame(root)
    info_frame.pack(pady=10)
    ttk.Label(info_frame, text=f"이름: {user_info['name']}", font=("Arial", 12)).pack()
    ttk.Label(info_frame, text=f"이메일: {user_info['email']}", font=("Arial", 12)).pack()

    edit_button = ttk.Button(root, text="개인정보 수정", bootstyle="info", command=lambda: verify_password(root))
    edit_button.pack(pady=10)

    dark_mode_button = ttk.Button(root, text="색반전 모드", bootstyle="secondary", command=lambda: toggle_dark_mode(root))
    dark_mode_button.pack(pady=10)

    logout_button = ttk.Button(root, text="로그아웃", bootstyle="warning", command=lambda: sign_login(root))  # ✅ 메인으로
    logout_button.pack(pady=10)

    exit_button = ttk.Button(root, text="닫기", bootstyle="danger", command=root.destroy)
    exit_button.pack(pady=20)


def verify_password(root):
    for widget in root.winfo_children():
        widget.destroy()

    root.title("비밀번호 확인")

    label = ttk.Label(root, text="비밀번호를 입력하세요", font=("Arial", 14, "bold"))
    label.pack(pady=20)

    password_var = tk.StringVar()
    password_entry = ttk.Entry(root, textvariable=password_var, show="*")
    password_entry.pack(pady=10)

    def check_password():
        if password_var.get() == user_info["password"]:
            edit_info_window(root)
        else:
            error_label.config(text="비밀번호가 일치하지 않습니다.", bootstyle="danger")

    confirm_button = ttk.Button(root, text="확인", bootstyle="primary", command=check_password)
    confirm_button.pack(pady=10)

    error_label = ttk.Label(root, text="", font=("Arial", 10))
    error_label.pack()


def edit_info_window(root):
    for widget in root.winfo_children():
        widget.destroy()

    root.title("개인정보 수정")

    label = ttk.Label(root, text="개인정보 수정", font=("Arial", 18, "bold"), bootstyle="primary")
    label.pack(pady=20)

    name_var = tk.StringVar(value=user_info["name"])
    email_var = tk.StringVar(value=user_info["email"])
    password_var = tk.StringVar()

    ttk.Label(root, text="이름").pack()
    ttk.Entry(root, textvariable=name_var).pack(pady=5)

    ttk.Label(root, text="이메일").pack()
    ttk.Entry(root, textvariable=email_var).pack(pady=5)

    ttk.Label(root, text="새 비밀번호").pack()
    ttk.Entry(root, textvariable=password_var, show="*").pack(pady=5)

    def save_changes():
        user_info["name"] = name_var.get()
        user_info["email"] = email_var.get()
        if password_var.get():
            user_info["password"] = password_var.get()
        settings_window(root)  # ✅ 저장 후 UI 새로고침

    save_button = ttk.Button(root, text="저장", bootstyle="success", command=save_changes)
    save_button.pack(pady=10)

    cancel_button = ttk.Button(root, text="취소", bootstyle="danger", command=lambda: settings_window(root))
    cancel_button.pack(pady=5)


if __name__ == "__main__":
    root = ttk.Window(themename="flatly")
    settings_window(root)
    root.mainloop()
