import pygame
import random
import time

# 初始化Pygame
pygame.init()

# 设置窗口大小
WIDTH = 800
HEIGHT = 600
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("贪吃蛇游戏")

# 颜色定义
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# 游戏时钟
clock = pygame.time.Clock()

# 游戏变量
snake_block = 20
snake_speed = 15

# 食物生成位置
foodx = random.randint(0, WIDTH // snake_block) * snake_block
foody = random.randint(0, HEIGHT // snake_block) * snake_block

# 初始化蛇
snake_x = [WIDTH // 2]
snake_y = [HEIGHT // 2]
direction = 0  # 方向：0=上，1=右，2=下，3=左

# 分数
score = 0

# 游戏循环
while True:
    # 清除上一帧
    window.fill(BLACK)

    # 处理事件
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT and direction != 3:
                direction = 3
            elif event.key == pygame.K_RIGHT and direction != 1:
                direction = 1
            elif event.key == pygame.K_UP and direction != 0:
                direction = 0
            elif event.key == pygame.K_DOWN and direction != 2:
                direction = 2

    # 移动蛇
    head_x = snake_x[0]
    head_y = snake_y[0]

    if direction == 0:  # 上
        head_y -= snake_block
    elif direction == 1:  # 右
        head_x += snake_block
    elif direction == 2:  # 下
        head_y += snake_block
    else:  # 左
        head_x -= snake_block

    # 检查碰撞墙
    if head_x < 0 or head_x >= WIDTH or head_y < 0 or head_y >= HEIGHT:
        game_over = True
        while True:
            pygame.display.set_caption("游戏结束")
            window.fill(BLACK)
            font = pygame.font.Font(None, 74)
            text = font.render("游戏结束！按回车重新开始", True, WHITE)
            text_rect = text.get_rect(center=(WIDTH/2, HEIGHT/2))
            window.blit(text, text_rect)
            if pygame.event.get().type == pygame.KEYDOWN:
                if pygame.key.get_pressed()[pygame.K_RETURN]:
                    return
            pygame.display.flip()
            time.sleep(1)

    # 检查碰撞自身
    for i in range(1, len(snake_x)):
        if head_x == snake_x[i] and head_y == snake_y[i]:
            game_over = True
            while True:
                pygame.display.set_caption("游戏结束")
                window.fill(BLACK)
                font = pygame.font.Font(None, 74)
                text = font.render("游戏结束！按回车重新开始", True, WHITE)
                text_rect = text.get_rect(center=(WIDTH/2, HEIGHT/2))
                window.blit(text, text_rect)
                if pygame.event.get().type == pygame.KEYDOWN:
                    if pygame.key.get_pressed()[pygame.K_RETURN]:
                        return
                pygame.display.flip()
                time.sleep(1)

    # 生成食物
    if not game_over and random.randint(0, 1) == 1:
        foodx = random.randint(0, WIDTH // snake_block) * snake_block
        foody = random.randint(0, HEIGHT // snake_block) * snake_block

    # 清除旧的食物
    if len(snake_x) > 0 and snake_x[0] == foodx and snake_y[0] == foody:
        snake_x.pop(0)
        snake_y.pop(0)

    # 添加新头部
    snake_x.append(head_x)
    snake_y.append(head_y)

    # 游戏得分
    score += 1
    font = pygame.font.Font(None, 36)
    text = font.render(f"得分：{score}", True, WHITE)
    text_rect = text.get_rect(center=(WIDTH/2, 20))
    window.blit(text, text_rect)

    # 游戏速度
    clock.tick(snake_speed)

    # 绘制元素
    # 环境
    pygame.draw.rect(window, RED, [foodx, foody, snake_block, snake_block])

    # 蛇
    for x in range(len(snake_x)):
        if x == 0:
            pygame.draw.rect(window, GREEN, [snake_x[x], snake_y[x], snake_block, snake_block])
        else:
            pygame.draw.rect(window, BLACK, [snake_x[x], snake_y[x], snake_block, snake_block])

    # 显示得分
    font = pygame.font.Font(None, 36)
    text = font.render(f"得分：{score}", True, WHITE)
    text_rect = text.get_rect(center=(WIDTH/2, 20))
    window.blit(text, text_rect)

    # 更新窗口
    pygame.display.flip()

    # 检查游戏结束
    if game_over:
        break

pygame.quit()