import math
import random
from pyray import *


def main():
    width, height = 1000, 700
    init_window(width, height, "Mini Golf")
    set_target_fps(60)

    ball_x = 120.0
    ball_y = height - 120.0
    ball_vx = 0.0
    ball_vy = 0.0
    dragging = False
    drag_start = (0, 0)
    strokes = 0

    hole_x = width - 120
    hole_y = 120
    hole_r = 18
    sand = Rectangle(380, 220, 170, 140)
    wall = Rectangle(580, 360, 220, 40)

    while not window_should_close():
        if is_mouse_button_pressed(MOUSE_LEFT_BUTTON):
            dragging = True
            drag_start = (get_mouse_x(), get_mouse_y())

        if is_mouse_button_released(MOUSE_LEFT_BUTTON) and dragging:
            dragging = False
            end_x = get_mouse_x()
            end_y = get_mouse_y()
            ball_vx += (drag_start[0] - end_x) * 0.06
            ball_vy += (drag_start[1] - end_y) * 0.06
            strokes += 1

        ball_x += ball_vx
        ball_y += ball_vy
        ball_vx *= 0.985
        ball_vy *= 0.985

        if ball_x < 0 or ball_x > width:
            ball_vx *= -0.8
        if ball_y < 0 or ball_y > height:
            ball_vy *= -0.8

        if ball_x > sand.x and ball_x < sand.x + sand.width and ball_y > sand.y and ball_y < sand.y + sand.height:
            ball_vx *= 0.98
            ball_vy *= 0.98

        if ball_x + 10 > wall.x and ball_x - 10 < wall.x + wall.width and ball_y + 10 > wall.y and ball_y - 10 < wall.y + wall.height:
            if abs(ball_vx) > abs(ball_vy):
                ball_vx *= -0.8
            else:
                ball_vy *= -0.8

        if math.hypot(ball_x - hole_x, ball_y - hole_y) < hole_r and abs(ball_vx) < 0.4 and abs(ball_vy) < 0.4:
            ball_x = hole_x
            ball_y = hole_y
            ball_vx = 0
            ball_vy = 0

        begin_drawing()
        clear_background(DARKGREEN)

        draw_circle_lines(hole_x, hole_y, hole_r, BLACK)
        draw_circle(hole_x, hole_y, hole_r - 2, DARKBROWN)
        draw_rectangle_rec(sand, BEIGE)
        draw_rectangle_rec(wall, GRAY)
        draw_circle(int(ball_x), int(ball_y), 10, WHITE)
        draw_circle_lines(int(ball_x), int(ball_y), 10, BLACK)

        if dragging:
            draw_line(int(ball_x), int(ball_y), get_mouse_x(), get_mouse_y(), RED)

        draw_text(f"Strokes: {strokes}", 20, 20, 24, WHITE)
        draw_text("Drag and release to shoot", 20, 50, 18, WHITE)

        end_drawing()

    close_window()


if __name__ == "__main__":
    main()
