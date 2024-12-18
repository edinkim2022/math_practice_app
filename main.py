import random
import time
import tkinter as tk
from tkinter import messagebox
import math

class MathPracticeApp:
    def __init__(self, root):
        self.root = root
        self.root.title("사칙연산 연습")

        self.selected_operator = None
        self.problem_label = None
        self.answer_entry = None
        self.time_label = None
        self.start_time = 0
        self.error_margin = 0.05

        self.create_operator_selection()

    def create_operator_selection(self):
        """연산 유형을 선택하는 버튼 생성"""
        label = tk.Label(self.root, text="연산 유형을 선택하세요:", font=("Helvetica", 16))
        label.pack(pady=10)

        button_frame = tk.Frame(self.root)
        button_frame.pack(pady=10)

        buttons = [
            ("덧셈", "+"),
            ("뺄셈", "-"),
            ("곱셈", "*"),
            ("나눗셈", "/"),
            ("종합연습", "all")
        ]

        for text, operator in buttons:
            btn = tk.Button(button_frame, text=text, font=("Helvetica", 14),
                            command=lambda op=operator: self.start_game(op))
            btn.pack(side=tk.LEFT, padx=5)

    def start_game(self, operator):
        """연산 유형을 설정하고 연습 시작"""
        self.selected_operator = operator

        # 기존 선택지 UI 제거
        for widget in self.root.winfo_children():
            widget.destroy()

        # 연습 UI 생성
        self.create_practice_ui()
        self.generate_problem()

    def create_practice_ui(self):
        """연습용 UI 생성"""
        self.problem_label = tk.Label(self.root, text="문제: ", font=("Helvetica", 16))
        self.problem_label.pack(pady=10)

        self.answer_entry = tk.Entry(self.root, font=("Helvetica", 14))
        self.answer_entry.pack(pady=10)
        self.answer_entry.bind("<Return>", self.check_answer)

        self.time_label = tk.Label(self.root, text="시간: 0.0초", font=("Helvetica", 12))
        self.time_label.pack(pady=10)

        quit_button = tk.Button(self.root, text="게임 종료", font=("Helvetica", 14), command=self.quit_game)
        quit_button.pack(pady=10)

    def generate_problem(self):
        """문제를 생성"""
        operator = self.selected_operator
        if operator == 'all':
            operator = random.choice(['+', '-', '*', '/'])

        num1 = random.randint(101, 99999)
        num2 = random.randint(2, 9 if operator in ['*', '/'] else 99999)
        if operator == '-' and num1 < num2:
            num1, num2 = num2, num1

        self.problem = f"{self.format_number(num1)} {operator} {self.format_number(num2)}"
        self.answer = self.calculate_answer(num1, num2, operator)
        self.problem_label.config(text=f"문제: {self.problem}")
        self.start_time = time.time()

    def calculate_answer(self, num1, num2, operator):
        """정답 계산"""
        operations = {
            '+': lambda x, y: x + y,
            '-': lambda x, y: x - y,
            '*': lambda x, y: x * y,
            '/': lambda x, y: round(x / y, 2)
        }
        return operations[operator](num1, num2)

    def check_answer(self, event=None):
        """사용자가 입력한 답 확인"""
        try:
            user_answer = float(self.answer_entry.get())
            elapsed_time = time.time() - self.start_time
            self.time_label.config(text=f"시간: {elapsed_time:.2f}초")

            if self.is_within_error_margin(user_answer):
                if math.isclose(self.answer, user_answer):
                    # 정답
                    messagebox.showinfo("정답", f"정답입니다! (원 정답: {self.answer})\n걸린 시간: {elapsed_time:.2f}초")
                else:
                    # 오차범위 내
                    messagebox.showinfo("오차범위 내 정답", 
                                        f"오차범위 내의 답입니다.\n원 정답: {self.answer}\n걸린 시간: {elapsed_time:.2f}초")
                self.answer_entry.delete(0, tk.END)
                self.generate_problem()
            else:
                # 오차범위를 벗어난 경우
                messagebox.showerror("오답", f"틀렸습니다.\n원 정답: {self.answer}")
                self.answer_entry.delete(0, tk.END)
        except ValueError:
            messagebox.showwarning("입력 오류", "유효한 숫자를 입력해주세요.")

    def is_within_error_margin(self, user_answer):
        """오차 범위 내에서 정답 여부 확인"""
        return math.isclose(self.answer, user_answer, rel_tol=self.error_margin)

    def format_number(self, number):
        """숫자를 천 단위 구분 기호로 포맷팅"""
        return f"{number:,}"

    def quit_game(self):
        """게임 종료"""
        if messagebox.askyesno("게임 종료", "정말로 게임을 종료하시겠습니까?"):
            self.root.quit()

if __name__ == "__main__":
    root = tk.Tk()
    app = MathPracticeApp(root)
    root.mainloop()
