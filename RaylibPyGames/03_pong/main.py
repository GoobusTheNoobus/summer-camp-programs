from pyray import *


def clamp(value, low, high):
    return max(low, min(high, value))


def main():
    width, height = 900, 540
    init_window(width, height, "Pong")
    set_target_fps(60)

    paddle_w = 18
    paddle_h = 100
    left_y = height // 2 - paddle_h // 2
    right_y = height // 2 - paddle_h // 2
    paddle_speed = 7

    ball_x = width // 2
    ball_y = height // 2
    ball_vx = 5
    ball_vy = 4
    score_left = 0
    score_right = 0

    while not window_should_close():
        if is_key_down(KEY_W):
            left_y -= paddle_speed
        if is_key_down(KEY_S):
            left_y += paddle_speed
        if is_key_down(KEY_UP):
            right_y -= paddle_speed
        if is_key_down(KEY_DOWN):
            right_y += paddle_speed

        left_y = clamp(left_y, 0, height - paddle_h)
        right_y = clamp(right_y, 0, height - paddle_h)

        ball_x += ball_vx
        ball_y += ball_vy

        if ball_y <= 0 or ball_y >= height:
            ball_vy *= -1

        if ball_x <= 40:
            if left_y <= ball_y <= left_y + paddle_h:
                ball_vx *= -1
            elif ball_x < 0:
                score_right += 1
                ball_x, ball_y = width // 2, height // 2
        if ball_x >= width - 40:
            if right_y <= ball_y <= right_y + paddle_h:
                ball_vx *= -1
            elif ball_x > width:
                score_left += 1
                ball_x, ball_y = width // 2, height // 2

        begin_drawing()
        clear_background(BLACK)

        draw_line(width // 2, 0, width // 2, height, DARKGRAY)
        draw_rectangle(20, left_y, paddle_w, paddle_h, WHITE)
        draw_rectangle(width - 40, right_y, paddle_w, paddle_h, WHITE)
        draw_circle(ball_x, ball_y, 10, SKYBLUE)
        draw_text(f"{score_left}", width // 2 - 60, 20, 40, WHITE)
        draw_text(f"{score_right}", width // 2 + 30, 20, 40, WHITE)

        end_drawing()

    close_window()


if __name__ == "__main__":
    main()
