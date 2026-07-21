import random
from pyray import *


def main():
    width, height = 800, 650
    init_window(width, height, "Memory Match")
    set_target_fps(60)

    symbols = ["A", "B", "C", "D", "E", "F"]
    deck = symbols + symbols
    random.shuffle(deck)

    cols = 4
    rows = 3
    card_w = 150
    card_h = 140
    gap = 15
    start_x = 40
    start_y = 70

    revealed = []
    matched = []
    first_pick = None
    second_pick = None
    flip_timer = 0

    while not window_should_close():
        mouse_x = get_mouse_x()
        mouse_y = get_mouse_y()

        if is_mouse_button_pressed(MOUSE_LEFT_BUTTON) and len(revealed) < 2:
            for index in range(len(deck)):
                row = index // cols
                col = index % cols
                x = start_x + col * (card_w + gap)
                y = start_y + row * (card_h + gap)
                inside = x <= mouse_x <= x + card_w and y <= mouse_y <= y + card_h
                if inside and index not in matched and index not in revealed:
                    revealed.append(index)
                    if first_pick is None:
                        first_pick = index
                    else:
                        second_pick = index
                        flip_timer = 60
                    break

        if flip_timer > 0:
            flip_timer -= 1
            if flip_timer == 0 and first_pick is not None and second_pick is not None:
                if deck[first_pick] == deck[second_pick]:
                    matched.extend([first_pick, second_pick])
                revealed.clear()
                first_pick = None
                second_pick = None

        begin_drawing()
        clear_background(RAYWHITE)
        draw_text("Memory Match", 20, 20, 28, DARKGRAY)
        draw_text("Click two cards to find pairs", 20, 50, 18, GRAY)

        for index, symbol in enumerate(deck):
            row = index // cols
            col = index % cols
            x = start_x + col * (card_w + gap)
            y = start_y + row * (card_h + gap)
            if index in matched or index in revealed:
                draw_rectangle(x, y, card_w, card_h, SKYBLUE)
                text_width = measure_text(symbol, 64)
                draw_text(symbol, x + card_w // 2 - text_width // 2, y + 40, 64, WHITE)
            else:
                draw_rectangle(x, y, card_w, card_h, DARKBLUE)
                draw_rectangle_lines(x, y, card_w, card_h, WHITE)

        if len(matched) == len(deck):
            draw_text("All pairs found!", width // 2 - 120, height - 50, 30, MAROON)

        end_drawing()

    close_window()


if __name__ == "__main__":
    main()
