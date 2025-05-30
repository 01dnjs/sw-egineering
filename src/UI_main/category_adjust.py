import tkinter as tk
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from tkinter import messagebox

def category_adjust(root, user_number, category_id):
    from category_manage import category_manage
        
    #DB연결
    import os
    import sys
    sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))  #나보다 위 디렉토리에 있음
    from database.category_db import CategoryDB

    category_db = CategoryDB()

    for widget in root.winfo_children():
            widget.destroy()  

    def set_placeholder(entry_widget, placeholder_text, is_password=False):
        """입력 필드에 플레이스홀더를 설정 (비밀번호 필드 대응)"""
        entry_widget.insert(0, placeholder_text)
        entry_widget.has_placeholder = True  
        entry_widget.config(style="Placeholder.TEntry")  

        def on_focus_in(event):
            if entry_widget.has_placeholder:
                entry_widget.delete(0, tk.END)
                entry_widget.config(style="Normal.TEntry")  
                entry_widget.has_placeholder = False  

        def on_focus_out(event):
            if not entry_widget.get().strip():  
                entry_widget.insert(0, placeholder_text)
                entry_widget.config(style="Placeholder.TEntry")  
                if is_password:
                    entry_widget.config(show="")  
                entry_widget.has_placeholder = True  

        entry_widget.bind("<FocusIn>", on_focus_in)
        entry_widget.bind("<FocusOut>", on_focus_out)

    def back_to_category():
        category_manage(root, user_number)

    def create_category(category_name):
        if (category_name.has_placeholder or category_name.get().strip() == ""):
            messagebox.showwarning("경고", "카테고리가 입력되지 않았습니다.")
            return

        #데이터베이스에 등록
        new_category = category_name.get().strip()
        if category_db.update_category(category_id, new_category, user_number): 
            #print(category_db.update_category(category_id, new_category, user_number))
            messagebox.showinfo("성공", "카테고리 수정 완료.")
            back_to_category()
        else:
            messagebox.showwarning("실패", "중복된 카테고리 이름입니다.")

    root.geometry("320x250")
    root.title("카테고리")

    # 뒤로가기 버튼 (오른쪽 상단)
    back_button = ttk.Button(root, text="뒤로가기", bootstyle="secondary", command=back_to_category)
    back_button.pack(anchor="ne", padx=10, pady=10)

    title_label = ttk.Label(root, text="카테고리 수정", font=("Arial", 18, "bold"), bootstyle="primary")
    title_label.pack(pady=10)

    # 카테고리 입력
    category_name_entry = ttk.Entry(root, width=30, bootstyle="info", style="Placeholder.TEntry")
    category_name_entry.pack(pady=5)
    set_placeholder(category_name_entry, "수정할 카테고리 이름")

    # 수정 버튼 (양쪽 여백 추가)
    signup_button = ttk.Button(root, text="수정", bootstyle="success", command=lambda: create_category(category_name_entry))
    signup_button.pack(pady=20, padx=10, anchor="center")
