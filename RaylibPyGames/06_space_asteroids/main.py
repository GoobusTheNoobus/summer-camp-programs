import math
import random
from pyray import *


def wrap(value, limit):
    if value < 0:
        return value + limit
    if value > limit:
        return value - limit
    return value


def main():
    width, height = 900, 700
    init_window(width, height, "Space Asteroids")
    set_target_fps(60)

    ship_x = width / 2
    ship_y = height / 2
    ship_angle = -90
    ship_speed_x = 0.0
    ship_speed_y = 0.0
    bullets = []
    asteroids = []
    score = 0
    shot_cooldown = 0

    for _ in range(6):
        asteroids.append([
            random.randint(0, width),
            random.randint(0, height),
            random.uniform(-2.5, 2.5),
            random.uniform(-2.5, 2.5),
            random.randint(22, 48),
        ])

    while not window_should_close():
        if is_key_down(KEY_LEFT):
            ship_angle -= 4
        if is_key_down(KEY_RIGHT):
            ship_angle += 4
        if is_key_down(KEY_UP):
            radians = math.radians(ship_angle)
            ship_speed_x += math.cos(radians) * 0.18
            ship_speed_y += math.sin(radians) * 0.18

        ship_x += ship_speed_x
        ship_y += ship_speed_y
        ship_speed_x *= 0.99
        ship_speed_y *= 0.99
        ship_x = wrap(ship_x, width)
        ship_y = wrap(ship_y, height)

        if shot_cooldown > 0:
            shot_cooldown -= 1
        if is_key_pressed(KEY_SPACE) and shot_cooldown == 0:
            radians = math.radians(ship_angle)
            bullets.append([
                ship_x,
                ship_y,
                math.cos(radians) * 8.0,
                math.sin(radians) * 8.0,
                45,
            ])
            shot_cooldown = 10

        for bullet in bullets[:]:
            bullet[0] += bullet[2]
            bullet[1] += bullet[3]
            bullet[4] -= 1
            if bullet[4] <= 0:
                bullets.remove(bullet)

        for asteroid in asteroids:
            asteroid[0] = wrap(asteroid[0] + asteroid[2], width)
            asteroid[1] = wrap(asteroid[1] + asteroid[3], height)

        for bullet in bullets[:]:
            for asteroid in asteroids[:]:
                dx = bullet[0] - asteroid[0]
                dy = bullet[1] - asteroid[1]
                if dx * dx + dy * dy < asteroid[4] * asteroid[4]:
                    bullets.remove(bullet)
                    asteroids.remove(asteroid)
                    score += 10
                    asteroids.append([
                        random.randint(0, width),
                        random.randint(0, height),
                        random.uniform(-3, 3),
                        random.uniform(-3, 3),
                        random.randint(22, 48),
                    ])
                    break

        begin_drawing()
        clear_background(BLACK)

        for asteroid in asteroids:
            draw_circle(int(asteroid[0]), int(asteroid[1]), asteroid[4], BROWN)
            draw_circle_lines(int(asteroid[0]), int(asteroid[1]), asteroid[4], SKYBLUE)

        for bullet in bullets:
            draw_circle(int(bullet[0]), int(bullet[1]), 4, YELLOW)

        tip_x = ship_x + math.cos(math.radians(ship_angle)) * 18
        tip_y = ship_y + math.sin(math.radians(ship_angle)) * 18
        left_x = ship_x + math.cos(math.radians(ship_angle + 140)) * 14
        left_y = ship_y + math.sin(math.radians(ship_angle + 140)) * 14
        right_x = ship_x + math.cos(math.radians(ship_angle - 140)) * 14
        right_y = ship_y + math.sin(math.radians(ship_angle - 140)) * 14
        draw_triangle(
            Vector2(int(tip_x), int(tip_y)),
            Vector2(int(left_x), int(left_y)),
            Vector2(int(right_x), int(right_y)),
            WHITE,
        )

        draw_text(f"Score: {score}", 20, 20, 24, WHITE)
        draw_text("Arrows to fly, space to shoot", 20, 50, 18, LIGHTGRAY)

        end_drawing()

    close_window()


if __name__ == "__main__":
    main()
