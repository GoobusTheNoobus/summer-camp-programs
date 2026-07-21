# Larp Larp Larp Sahur will come for you if you don't make this game better

from raylibpy import *
import random


# Variables to change

SCREEN_WIDTH = 900
SCREEN_HEIGHT = 600

PLAYER_SPEED = 5
PLAYER_SIZE = 40

ENEMY_SIZE = 30
ENEMY_SPEED = 2


# Enemy & Player

class Player:
    def __init__(self):
        self.x = SCREEN_WIDTH // 2
        self.y = SCREEN_HEIGHT // 2
        self.size = PLAYER_SIZE
        self.color = BLUE

    def update(self):
        if is_key_down(KEY_W):
            self.y -= PLAYER_SPEED

        if is_key_down(KEY_S):
            self.y += PLAYER_SPEED

        if is_key_down(KEY_A):
            self.x -= PLAYER_SPEED

        if is_key_down(KEY_D):
            self.x += PLAYER_SPEED

        self.x = max(
            0,
            min(SCREEN_WIDTH - self.size, self.x)
        )

        self.y = max(
            0,
            min(SCREEN_HEIGHT - self.size, self.y)
        )

    def draw(self):
        draw_rectangle(
            int(self.x),
            int(self.y),
            self.size,
            self.size,
            self.color
        )


class Enemy:
    def __init__(self):
        self.x = random.randint(
            0,
            SCREEN_WIDTH - ENEMY_SIZE
        )

        self.y = random.randint(
            0,
            SCREEN_HEIGHT - ENEMY_SIZE
        )

        self.size = ENEMY_SIZE
        self.color = RED

    def update(self):
        self.y += ENEMY_SPEED

        if self.y > SCREEN_HEIGHT:
            self.y = -self.size

            self.x = random.randint(
                0,
                SCREEN_WIDTH - self.size
            )

    def draw(self):
        draw_rectangle(
            int(self.x),
            int(self.y),
            self.size,
            self.size,
            self.color
        )

# Game

class Game:
    def __init__(self):
        self.player = Player()
        self.enemies = []

        self.score = 0

        self.spawn_enemies(10)

    def spawn_enemies(self, amount):

        for _ in range(amount):
            self.enemies.append(Enemy())

    def update(self):

        self.player.update()

        for current_enemy in self.enemies:

            current_enemy.update()

            if self.check_collision(
                self.player,
                current_enemy
            ):
                self.score += 1
                current_enemy.y = -current_enemy.size

    def draw(self):

        self.player.draw()

        for current_enemy in self.enemies:
            current_enemy.draw()

        draw_text(
            f"score: {self.score}",
            20,
            20,
            30,
            WHITE
        )

    def check_collision(self, a, b):

        return (
            a.x < b.x + b.size and
            a.x + a.size > b.x and
            a.y < b.y + b.size and
            a.y + a.size > b.y
        )


# ==========================
# main
# ==========================

def main():

    init_window(
        SCREEN_WIDTH,
        SCREEN_HEIGHT,
        "I den nnue"
    )

    set_target_fps(60)

    current_game = Game()

    while not window_should_close():

        current_game.update()

        begin_drawing()

        clear_background(BLACK)

        current_game.draw()

        end_drawing()

    close_window()


if __name__ == "__main__":
    main()