import random
from pyray import *


def main():
    width, height = 800, 600
    init_window(width, height, "Catch the Stars")
    set_target_fps(60)

    basket_w = 90
    basket_h = 18
    basket_x = width // 2 - basket_w // 2
    basket_y = height - 50
    basket_speed = 7

    stars = []
    timer = 0
    score = 0
    misses = 0

    while not window_should_close():
        if is_key_down(KEY_LEFT):
            basket_x -= basket_speed
        if is_key_down(KEY_RIGHT):
            basket_x += basket_speed
        basket_x = max(0, min(width - basket_w, basket_x))

        timer += 1
        if timer >= 20:
            stars.append([random.randint(10, width - 20), -20, random.randint(3, 7)])
            timer = 0

        for star in stars[:]:
            star[1] += star[2]
            caught = (
                basket_x < star[0] < basket_x + basket_w
                and basket_y < star[1] + 20 < basket_y + basket_h + 30
            )
            if caught:
                stars.remove(star)
                score += 1
            elif star[1] > height:
                stars.remove(star)
                misses += 1

        begin_drawing()
        clear_background(RAYWHITE)

        draw_rectangle(basket_x, basket_y, basket_w, basket_h, BROWN)
        draw_rectangle(basket_x + 12, basket_y - 10, basket_w - 24, 10, GOLD)

        for star in stars:
            draw_circle(star[0], star[1], 10, YELLOW)
            draw_circle_lines(star[0], star[1], 10, ORANGE)

        draw_text(f"Stars: {score}", 20, 20, 24, DARKGRAY)
        draw_text(f"Misses: {misses}", 20, 50, 24, GRAY)
        draw_text("Move with arrows", 20, 80, 18, GRAY)

        end_drawing()

    close_window()


if __name__ == "__main__":
    main()
