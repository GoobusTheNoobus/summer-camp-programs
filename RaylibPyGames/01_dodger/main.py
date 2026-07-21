import random
import raylibpy as rl


def main():
    width, height = 800, 600
    rl.init_window(width, height, "Dodger")
    rl.set_target_fps(60)

    player_w = 60
    player_h = 24
    player_x = width // 2 - player_w // 2
    player_y = height - 60
    player_speed = 6

    enemies = []
    spawn_timer = 0
    score = 0
    game_over = False

    while not rl.window_should_close():
        if not game_over:
            if rl.is_key_down(rl.KEY_LEFT):
                player_x -= player_speed
            if rl.is_key_down(rl.KEY_RIGHT):
                player_x += player_speed
            player_x = max(0, min(width - player_w, player_x))

            spawn_timer += 1
            if spawn_timer >= 28:
                enemies.append([random.randint(0, width - 28), -28, random.randint(4, 8)])
                spawn_timer = 0

            for enemy in enemies[:]:
                enemy[1] += enemy[2]
                if (
                    player_x < enemy[0] + 28
                    and player_x + player_w > enemy[0]
                    and player_y < enemy[1] + 28
                    and player_y + player_h > enemy[1]
                ):
                    game_over = True
                if enemy[1] > height:
                    enemies.remove(enemy)
                    score += 1
        else:
            if rl.is_key_pressed(rl.KEY_R):
                enemies.clear()
                player_x = width // 2 - player_w // 2
                score = 0
                game_over = False
                spawn_timer = 0

        rl.begin_drawing()
        rl.clear_background(rl.RAYWHITE)

        rl.draw_rectangle(player_x, player_y, player_w, player_h, rl.BLUE)
        for enemy in enemies:
            rl.draw_rectangle(enemy[0], enemy[1], 28, 28, rl.RED)

        rl.draw_text(f"Score: {score}", 20, 20, 24, rl.DARKGRAY)
        rl.draw_text("Arrows to move", 20, 50, 18, rl.GRAY)

        if game_over:
            draw_text("GAME OVER", width // 2 - 110, height // 2 - 20, 40, MAROON)
            draw_text("Press R to restart", width // 2 - 100, height // 2 + 25, 20, DARKGRAY)

        rl.end_drawing()

    rl.close_window()


if __name__ == "__main__":
    main()
