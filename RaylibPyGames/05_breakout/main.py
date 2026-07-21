import random
from pyray import *


def main():
    width, height = 900, 700
    init_window(width, height, "Breakout")
    set_target_fps(60)

    paddle_w = 120
    paddle_h = 18
    paddle_x = width // 2 - paddle_w // 2
    paddle_y = height - 40
    paddle_speed = 8

    ball_x = width // 2
    ball_y = height // 2
    ball_vx = 5
    ball_vy = -5

    bricks = []
    brick_cols = 8
    brick_rows = 5
    brick_w = 100
    brick_h = 28
    brick_gap = 8
    start_x = 40
    start_y = 80

    for row in range(brick_rows):
        for col in range(brick_cols):
            bricks.append([start_x + col * (brick_w + brick_gap), start_y + row * (brick_h + brick_gap), True])

    score = 0

    while not window_should_close():
        if is_key_down(KEY_LEFT):
            paddle_x -= paddle_speed
        if is_key_down(KEY_RIGHT):
            paddle_x += paddle_speed
        paddle_x = max(0, min(width - paddle_w, paddle_x))

        ball_x += ball_vx
        ball_y += ball_vy

        if ball_x <= 0 or ball_x >= width:
            ball_vx *= -1
        if ball_y <= 0:
            ball_vy *= -1

        if (
            paddle_x < ball_x < paddle_x + paddle_w
            and paddle_y < ball_y + 10 < paddle_y + paddle_h
            and ball_vy > 0
        ):
            ball_vy *= -1
            ball_y = paddle_y - 11

        for brick in bricks:
            if brick[2]:
                hit = brick[0] <= ball_x <= brick[0] + brick_w and brick[1] <= ball_y <= brick[1] + brick_h
                if hit:
                    brick[2] = False
                    ball_vy *= -1
                    score += 10
                    break

        if ball_y > height:
            ball_x = width // 2
            ball_y = height // 2
            ball_vy = -5
            score = max(0, score - 20)

        begin_drawing()
        clear_background(RAYWHITE)

        for index, brick in enumerate(bricks):
            if brick[2]:
                color = [ORANGE, RED, GOLD, PURPLE, SKYBLUE][index % 5]
                draw_rectangle(brick[0], brick[1], brick_w, brick_h, color)
        draw_rectangle(paddle_x, paddle_y, paddle_w, paddle_h, DARKBLUE)
        draw_circle(ball_x, ball_y, 10, MAROON)

        draw_text(f"Score: {score}", 20, 20, 24, DARKGRAY)
        draw_text("Break all the bricks", 20, 50, 18, GRAY)

        end_drawing()

    close_window()


if __name__ == "__main__":
    main()
