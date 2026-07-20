from pyray import *
import random
from typing import List

GROUND_Y = 650
GRAVITY = 1800
JUMP = -700

class Player:
    def __init__(self):
        self.x = 100
        self.y = 500
        self.width = 50
        self.height = 50
        self.velocity = 0
        self.on_ground = True

    def get_rect(self):
        return Rectangle(
            self.x,
            self.y,
            self.width,
            self.height
        )


class Obstacle:
    def __init__(self):
        self.x = 1280
        self.y = 590
        self.width = 30
        self.height = 60
        self.speed = 400

    def update(self, dt):
        self.x -= self.speed * dt

    def draw(self):
        draw_rectangle(
            int(self.x),
            int(self.y),
            self.width,
            self.height,
            GREEN
        )

    def get_rect(self):
        return Rectangle(
            self.x,
            self.y,
            self.width,
            self.height
        )


def main():

    init_window(1280, 720, "Dinosaur Game")
    set_target_fps(60)

    player = Player()
    obstacles: List[Obstacle] = []

    spawn_timer = 0
    spawn_interval = random.uniform(1, 3)

    game_over = False

    while not window_should_close() and not game_over:

        delta = get_frame_time()

        # Obstacles

        for obstacle in obstacles:
            obstacle.update(delta)

        # Remove obstacles off screen
        obstacles = [
            obstacle
            for obstacle in obstacles
            if obstacle.x > -100
        ]


        
        spawn_timer += delta

        if spawn_timer >= spawn_interval:
            obstacles.append(Obstacle())

            spawn_timer = 0
            spawn_interval = random.uniform(1, 3)

        if player.on_ground and is_key_pressed(KeyboardKey.KEY_SPACE):
            player.velocity = JUMP
            player.on_ground = False


        player.velocity += GRAVITY * delta
        player.y += player.velocity * delta


        if player.y >= GROUND_Y - player.height:
            player.y = GROUND_Y - player.height
            player.velocity = 0
            player.on_ground = True


        # Collisions

        for obstacle in obstacles:
            if check_collision_recs(
                player.get_rect(),
                obstacle.get_rect()
            ):
                game_over = True


        # Drawing

        begin_drawing()

        clear_background(RAYWHITE)

        draw_line(
            0,
            GROUND_Y,
            1280,
            GROUND_Y,
            BLACK
        )

        draw_rectangle(
            int(player.x),
            int(player.y),
            player.width,
            player.height,
            GRAY
        )

        for obstacle in obstacles:
            obstacle.draw()

        end_drawing()

    # Game Over

    while not window_should_close():

        begin_drawing()

        clear_background(RAYWHITE)

        draw_text(
            "Game Over",
            450,
            300,
            55,
            RED
        )

        draw_text(
            "Press ESC to quit",
            450,
            380,
            25,
            BLACK
        )

        end_drawing()


    close_window()


if __name__ == "__main__":
    main()