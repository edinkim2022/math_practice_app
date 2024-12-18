#Game UI 디자인 작업중, 미완

import pygame
import random

# Pygame 초기화
pygame.init()

# 화면 크기와 설정
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Math Game")

# 색상
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# 폰트
font_large = pygame.font.Font(None, 74)
font_small = pygame.font.Font(None, 36)

# 게임 변수
problem = ""
answer = 0
input_text = ""
score = 0
time_limit = 90  # 제한 시간 (초)
start_ticks = pygame.time.get_ticks()  # 시작 시간

# 문제 생성 함수
def generate_problem():
    global problem, answer
    operator = random.choice(['+', '-', '*', '/'])
    if operator in ['+', '-']:
        num1 = random.randint(101, 99999)
        num2 = random.randint(101, 99999)
        if operator == '-' and num1 < num2:  # 뺄셈에서 음수 방지
            num1, num2 = num2, num1
    elif operator in ['*', '/']:
        num1 = random.randint(101, 99999)
        num2 = random.randint(2, 9)  # 나눗셈과 곱셈에서 num2는 작은 값으로
    problem = f"{num1} {operator} {num2}"
    answer = eval(problem)

# 첫 번째 문제 생성
generate_problem()

# 게임 루프
running = True
while running:
    # 이벤트 처리
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:  # Enter 입력 시
                if input_text.isdigit() and abs(float(input_text) - answer) < 0.05 * abs(answer):  # 5% 오차 허용
                    score += 10
                else:
                    score -= 5
                input_text = ""
                generate_problem()  # 새로운 문제 생성
            elif event.key == pygame.K_BACKSPACE:
                input_text = input_text[:-1]
            else:
                input_text += event.unicode

    # 남은 시간 계산
    elapsed_time = (pygame.time.get_ticks() - start_ticks) / 1000
    remaining_time = max(0, time_limit - int(elapsed_time))
    
    if remaining_time == 0:  # 시간 초과 시 종료
        running = False

    # 화면 그리기
    screen.fill(WHITE)

    # 문제 출력
    problem_text = font_large.render(problem, True, BLACK)
    screen.blit(problem_text, (SCREEN_WIDTH // 2 - problem_text.get_width() // 2, 100))

    # 입력된 텍스트 출력
    input_render = font_large.render(input_text, True, BLUE)
    screen.blit(input_render, (SCREEN_WIDTH // 2 - input_render.get_width() // 2, 200))

    # 점수 출력
    score_text = font_small.render(f"Score: {score}", True, BLACK)
    screen.blit(score_text, (10, 10))

    # 남은 시간 출력
    timer_text = font_small.render(f"Time: {remaining_time}s", True, RED)
    screen.blit(timer_text, (SCREEN_WIDTH - 150, 10))

    # 화면 업데이트
    pygame.display.flip()

    # 초당 30 프레임으로 제한
    pygame.time.Clock().tick(30)

# 게임 종료 메시지
screen.fill(WHITE)
end_text = font_large.render(f"Game Over! Final Score: {score}", True, BLACK)
screen.blit(end_text, (SCREEN_WIDTH // 2 - end_text.get_width() // 2, SCREEN_HEIGHT // 2 - end_text.get_height() // 2))
pygame.display.flip()
pygame.time.delay(3000)

pygame.quit()
