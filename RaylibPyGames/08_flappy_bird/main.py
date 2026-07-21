import random
from pyray import *


def main():
    width, height = 900, 600
    init_window(width, height, "Flappy Bird")
    set_target_fps(60)

    bird_x = 220
    bird_y = height // 2
    bird_vy = 0.0
    gravity = 0.35
    flap_strength = -6.5

    pipes = []
    pipe_timer = 0
    score = 0
    dead = False

    while not window_should_close():
        if not dead:
            if is_key_pressed(KEY_SPACE):
                bird_vy = flap_strength

            bird_vy += gravity
            bird_y += bird_vy

            pipe_timer += 1
            if pipe_timer >= 90:
                gap_y = random.randint(140, height - 140)
                pipes.append([width + 60, gap_y, False])
                pipe_timer = 0

            for pipe in pipes[:]:
                pipe[0] -= 4
                if pipe[0] + 80 < bird_x and not pipe[2]:
                    pipe[2] = True
                    score += 1
                if pipe[0] < -100:
                    pipes.remove(pipe)

                top_hit = bird_x + 24 > pipe[0] and bird_x < pipe[0] + 80 and bird_y < pipe[1] - 90
                bottom_hit = bird_x + 24 > pipe[0] and bird_x < pipe[0] + 80 and bird_y + 24 > pipe[1] + 90
                if top_hit or bottom_hit:
                    dead = True

            if bird_y < 0 or bird_y + 24 > height:
                dead = True
        else:
            if is_key_pressed(KEY_R):
                bird_y = height // 2
                bird_vy = 0.0
                pipes.clear()
                pipe_timer = 0
                score = 0
                dead = False

        begin_drawing()
        clear_background(SKYBLUE)

        draw_circle(bird_x, int(bird_y), 12, YELLOW)
        draw_circle_lines(bird_x, int(bird_y), 12, ORANGE)

        for pipe in pipes:
            draw_rectangle(pipe[0], 0, 80, pipe[1] - 90, GREEN)
            draw_rectangle(pipe[0], pipe[1] + 90, 80, height - (pipe[1] + 90), GREEN)

        draw_text(f"Score: {score}", 20, 20, 24, DARKGRAY)
        draw_text("Space to flap", 20, 50, 18, DARKGRAY)

        if dead:
            draw_text("FLAPPED TOO HARD", width // 2 - 170, height // 2 - 20, 40, MAROON)
            draw_text("Press R to restart", width // 2 - 105, height // 2 + 25, 20, WHITE)

        end_drawing()

    close_window()


if __name__ == "__main__":
    main()
