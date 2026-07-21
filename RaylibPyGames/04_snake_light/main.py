import random
from pyray import *


def main():
    width, height = 800, 600
    cell = 20
    cols = width // cell
    rows = height // cell
    init_window(width, height, "Snake Light")
    set_target_fps(10)

    snake = [[cols // 2, rows // 2]]
    direction = [1, 0]
    next_direction = [1, 0]
    food = [random.randint(0, cols - 1), random.randint(0, rows - 1)]
    score = 0
    game_over = False

    while not window_should_close():
        if is_key_pressed(KEY_UP) and direction != [0, 1]:
            next_direction = [0, -1]
        elif is_key_pressed(KEY_DOWN) and direction != [0, -1]:
            next_direction = [0, 1]
        elif is_key_pressed(KEY_LEFT) and direction != [1, 0]:
            next_direction = [-1, 0]
        elif is_key_pressed(KEY_RIGHT) and direction != [-1, 0]:
            next_direction = [1, 0]

        if not game_over:
            direction = next_direction
            head = [snake[0][0] + direction[0], snake[0][1] + direction[1]]

            if head[0] < 0 or head[0] >= cols or head[1] < 0 or head[1] >= rows or head in snake:
                game_over = True
            else:
                snake.insert(0, head)
                if head == food:
                    score += 1
                    food = [random.randint(0, cols - 1), random.randint(0, rows - 1)]
                else:
                    snake.pop()

        begin_drawing()
        clear_background(RAYWHITE)

        for x in range(0, width, cell):
            draw_line(x, 0, x, height, LIGHTGRAY)
        for y in range(0, height, cell):
            draw_line(0, y, width, y, LIGHTGRAY)

        draw_rectangle(food[0] * cell, food[1] * cell, cell, cell, RED)
        for index, segment in enumerate(snake):
            color = DARKGREEN if index == 0 else GREEN
            draw_rectangle(segment[0] * cell, segment[1] * cell, cell, cell, color)

        draw_text(f"Score: {score}", 20, 20, 24, DARKGRAY)
        if game_over:
            draw_text("You crashed", width // 2 - 90, height // 2 - 20, 40, MAROON)
            draw_text("Close and restart", width // 2 - 100, height // 2 + 25, 20, DARKGRAY)

        end_drawing()

    close_window()


if __name__ == "__main__":
    main()
