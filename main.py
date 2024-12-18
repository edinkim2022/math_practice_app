import random
import time
import tkinter as tk
from tkinter import messagebox

class MathPracticeApp:
    def __init__(self, root):
        self.root = root
        self.root.title("사칙연산 연습")
        
        # 문제 레이블
        self.problem_label = tk.Label(root, text="문제: ", font=("Helvetica", 16))
        self.problem_label.pack(pady=10)
        
        # 답 입력 필드
        self.answer_entry = tk.Entry(root, font=("Helvetica", 14))
        self.answer_entry.pack(pady=10)
        
        # 시간 레이블
        self.time_label = tk.Label(root, text="시간: 0.0초", font=("Helvetica", 12))
        self.time_label.pack(pady=10)
        
        # 종료 버튼
        self.quit_button = tk.Button(root, text="게임 종료", font=("Helvetica", 14), command=self.quit_game)
        self.quit_button.pack(pady=10)
        
        self.problem = ""
        self.answer = 0
        self.start_time = 0
        self.error_margin = 0.05  # 5% 오차범위 설정
        
        self.answer_entry.bind("<Return>", self.check_answer)  # Enter 키로 정답 제출
        self.answer_entry.bind("<space>", self.check_answer)  # Space 바도 정답 제출
        
        self.generate_problem()

    def generate_problem(self):
        # 연산자를 무작위로 선택
        operator = random.choice(['+', '-', '*', '/'])
        
        if operator in ['+', '-']:
            # 덧셈과 뺄셈: X와 Y의 범위는 101~99,999
            num1 = random.randint(101, 99999)
            num2 = random.randint(101, 99999)
            
            if operator == '-':
                # 뺄셈에서는 num1이 num2보다 커야 한다
                if num1 < num2:
                    num1, num2 = num2, num1  # num1과 num2의 값을 바꿈
            
        elif operator in ['*', '/']:
            # 곱셈과 나눗셈: X는 101~99,999, Y는 1~9
            num1 = random.randint(101, 99999)
            num2 = random.randint(2, 9)
        
        # 문제 텍스트를 포맷에 맞게 설정
        self.problem = f"{self.format_number(num1)} {operator} {self.format_number(num2)}"
        self.answer = self.calculate_answer(num1, num2, operator)
        
        self.problem_label.config(text=f"문제: {self.problem}")
        
        # 시작 시간 기록
        self.start_time = time.time()

    def calculate_answer(self, num1, num2, operator):
        if operator == '+':
            return num1 + num2
        elif operator == '-':
            return num1 - num2
        elif operator == '*':
            return num1 * num2
        elif operator == '/':
            return num1 / num2

    def check_answer(self, event=None):
        try:
            user_answer = float(self.answer_entry.get())
            elapsed_time = time.time() - self.start_time
            
            # 시간 표시 업데이트
            self.time_label.config(text=f"시간: {elapsed_time:.2f}초")
            
            # 오차 범위 계산
            if self.is_within_error_margin(user_answer):
                message = f"정답입니다! 문제를 푸는 데 걸린 시간은 {elapsed_time:.2f}초 입니다."
                if isinstance(self.answer, float):
                    message += f" (실제 답: {self.format_number(self.answer)})"
                messagebox.showinfo("정답", message)
                self.answer_entry.delete(0, tk.END)
                self.generate_problem()  # 새로운 문제 생성
            else:
                message = f"틀렸습니다. 정답은 {self.format_number(self.answer)}입니다."
                messagebox.showerror("오답", message)
                self.answer_entry.delete(0, tk.END)
                self.generate_problem()  # 새로운 문제 생성
        except ValueError:
            messagebox.showwarning("입력 오류", "유효한 숫자를 입력해주세요.")
    
    def is_within_error_margin(self, user_answer):
        # 오차범위 ±5% 이내 (덧셈, 뺄셈도 적용)
        lower_bound = self.answer * (1 - self.error_margin)
        upper_bound = self.answer * (1 + self.error_margin)
        return lower_bound <= user_answer <= upper_bound

    def format_number(self, number):
        # 천 단위 구분 기호 추가
        return f"{number:,}"

    def quit_game(self):
        # 게임 종료 확인 메시지
        if messagebox.askyesno("게임 종료", "정말로 게임을 종료하시겠습니까?"):
            self.root.quit()  # Tkinter의 종료 명령어

if __name__ == "__main__":
    root = tk.Tk()
    app = MathPracticeApp(root)
    root.mainloop()
