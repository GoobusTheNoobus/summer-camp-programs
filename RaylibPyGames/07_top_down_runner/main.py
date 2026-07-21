import random
from pyray import *


def main():
    width, height = 900, 650
    init_window(width, height, "Top Down Runner")
    set_target_fps(60)

    player_w = 32
    player_h = 32
    player_x = width // 2
    player_y = height // 2
    speed = 5

    obstacles = []
    spawn_timer = 0
    survived = 0
    game_over = False

    while not window_should_close():
        if not game_over:
            move_x = 0
            move_y = 0
            if is_key_down(KEY_A) or is_key_down(KEY_LEFT):
                move_x -= speed
            if is_key_down(KEY_D) or is_key_down(KEY_RIGHT):
                move_x += speed
            if is_key_down(KEY_W) or is_key_down(KEY_UP):
                move_y -= speed
            if is_key_down(KEY_S) or is_key_down(KEY_DOWN):
                move_y += speed

            player_x = max(0, min(width - player_w, player_x + move_x))
            player_y = max(0, min(height - player_h, player_y + move_y))

            spawn_timer += 1
            if spawn_timer >= 35:
                side = random.choice(["top", "bottom", "left", "right"])
                if side == "top":
                    obstacles.append([-40, random.randint(0, height), random.randint(4, 7), 0])
                elif side == "bottom":
                    obstacles.append([width + 40, random.randint(0, height), -random.randint(4, 7), 0])
                elif side == "left":
                    obstacles.append([random.randint(0, width), -40, 0, random.randint(4, 7)])
                else:
                    obstacles.append([random.randint(0, width), height + 40, 0, -random.randint(4, 7)])
                spawn_timer = 0
                survived += 1

            for obstacle in obstacles[:]:
                obstacle[0] += obstacle[2]
                obstacle[1] += obstacle[3]
                hit = (
                    player_x < obstacle[0] + 28
                    and player_x + player_w > obstacle[0]
                    and player_y < obstacle[1] + 28
                    and player_y + player_h > obstacle[1]
                )
                if hit:
                    game_over = True
                if obstacle[0] < -80 or obstacle[0] > width + 80 or obstacle[1] < -80 or obstacle[1] > height + 80:
                    obstacles.remove(obstacle)
        else:
            if is_key_pressed(KEY_R):
                player_x = width // 2
                player_y = height // 2
                obstacles.clear()
                spawn_timer = 0
                survived = 0
                game_over = False

        begin_drawing()
        clear_background(RAYWHITE)

        draw_rectangle(player_x, player_y, player_w, player_h, DARKBLUE)
        for obstacle in obstacles:
            draw_rectangle(obstacle[0], obstacle[1], 28, 28, RED)
        draw_text(f"Wave: {survived}", 20, 20, 24, DARKGRAY)
        draw_text("Move with WASD or arrows", 20, 50, 18, GRAY)

        if game_over:
            draw_rectangle(0, 0, width, height, Color(0, 0, 0, 120))
            draw_text("You got tagged", width // 2 - 120, height // 2 - 20, 40, MAROON)
            draw_text("Press R to restart", width // 2 - 105, height // 2 + 25, 20, WHITE)

        end_drawing()

    close_window()


if __name__ == "__main__":
    main()
