# 프로젝트: Math Practice App(인적성 검사 자료분석 계산 대비용)

## 소개
Math Practice App은 사용자가 사칙연산을 연습할 수 있는 Python 기반의 데스크톱 애플리케이션입니다. 

이 애플리케이션은 Tkinter를 사용하여 GUI를 제공하며, 덧셈, 뺄셈, 곱셈, 나눗셈 또는 종합적인 연산 문제를 생성하여 사용자가 직접 입력한 답을 검증합니다. 

오차 범위 내의 답변도 인식하여 피드백을 제공합니다.

---

## 주요 기능
1. **사용자 친화적 인터페이스**
    - Tkinter를 활용하여 직관적인 UI 제공.
2. **다양한 연산 선택**
    - 덧셈, 뺄셈, 곱셈, 나눗셈, 종합 연습(랜덤 연산 문제 포함) 중 선택 가능.
3. **실시간 시간 측정**
    - 문제 풀이 시간을 실시간으로 표시.
4. **오차 범위 검증**
    - 답이 오차 범위 내에 있을 경우 정답과 원래 값을 안내.
5. **즉각적인 피드백**
    - 정답 여부 및 원 정답 표시.

---

## 설치 방법

### 요구사항
- Python 3.7 이상

### 설치
1. 프로젝트를 클론합니다.
   ```bash
   git clone https://github.com/your-repo/math-practice-app.git
   cd math-practice-app
   ```

2. 필요 라이브러리를 설치합니다.
   ```bash
   pip install -r requirements.txt
   ```

3. 프로그램 실행
   ```bash
   python math_practice_app.py
   ```

---

## 파일 구조
```
math-practice-app/
├── math_practice_app.py   # 메인 프로그램
├── requirements.txt       # 필수 라이브러리
└── README.md              # 프로젝트 설명
```

---

## 사용 예시
1. 프로그램 실행 시 연산 유형(덧셈, 뺄셈 등)을 선택.
2. 문제를 풀고 답을 입력 후 Enter 키로 제출.
3. 정답 여부 및 풀이 시간 확인.
4. 게임 종료 버튼으로 애플리케이션 종료.
