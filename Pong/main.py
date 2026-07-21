from raylibpy import *


# ==========================
# settings
# ==========================

SCREEN_WIDTH = 900
SCREEN_HEIGHT = 600

PADDLE_WIDTH = 20
PADDLE_HEIGHT = 100

BALL_SIZE = 20

PLAYER_SPEED = 7
AI_SPEED = 5

BALL_SPEED = 6


# ==========================
# objects
# ==========================

class Paddle:

    def __init__(self, x, y):

        self.x = x
        self.y = y

        self.width = PADDLE_WIDTH
        self.height = PADDLE_HEIGHT


    def draw(self):

        draw_rectangle(
            self.x,
            self.y,
            self.width,
            self.height,
            WHITE
        )


    def move(self, amount):

        self.y += amount

        self.y = max(
            0,
            min(
                SCREEN_HEIGHT - self.height,
                self.y
            )
        )


class Ball:

    def __init__(self):

        self.reset()


    def reset(self):

        self.x = SCREEN_WIDTH // 2
        self.y = SCREEN_HEIGHT // 2

        self.speed_x = BALL_SPEED
        self.speed_y = BALL_SPEED



    def update(self):

        self.x += self.speed_x
        self.y += self.speed_y


        if self.y <= 0 or self.y >= SCREEN_HEIGHT - BALL_SIZE:

            self.speed_y *= -1



    def draw(self):

        draw_rectangle(
            self.x,
            self.y,
            BALL_SIZE,
            BALL_SIZE,
            WHITE
        )



# ==========================
# game
# ==========================

class PongGame:

    def __init__(self):

        self.player = Paddle(
            30,
            SCREEN_HEIGHT // 2 - PADDLE_HEIGHT // 2
        )

        self.ai = Paddle(
            SCREEN_WIDTH - 50,
            SCREEN_HEIGHT // 2 - PADDLE_HEIGHT // 2
        )


        self.ball = Ball()


        self.player_score = 0
        self.ai_score = 0



    def update(self):

        # player controls

        if is_key_down(KEY_W):

            self.player.move(-PLAYER_SPEED)


        if is_key_down(KEY_S):

            self.player.move(PLAYER_SPEED)



        # AI movement

        if self.ai.y + self.ai.height / 2 < self.ball.y:

            self.ai.move(AI_SPEED)


        elif self.ai.y + self.ai.height / 2 > self.ball.y:

            self.ai.move(-AI_SPEED)



        self.ball.update()


        # paddle collision

        if self.check_collision(
            self.ball,
            self.player
        ):

            self.ball.speed_x *= -1



        if self.check_collision(
            self.ball,
            self.ai
        ):

            self.ball.speed_x *= -1



        # scoring

        if self.ball.x < 0:

            self.ai_score += 1
            self.ball.reset()



        if self.ball.x > SCREEN_WIDTH:

            self.player_score += 1
            self.ball.reset()



    def draw(self):

        self.player.draw()

        self.ai.draw()

        self.ball.draw()


        draw_text(
            str(self.player_score),
            SCREEN_WIDTH // 4,
            40,
            50,
            WHITE
        )


        draw_text(
            str(self.ai_score),
            SCREEN_WIDTH * 3 // 4,
            40,
            50,
            WHITE
        )


        draw_line(
            SCREEN_WIDTH // 2,
            0,
            SCREEN_WIDTH // 2,
            SCREEN_HEIGHT,
            WHITE
        )



    def check_collision(self, ball, paddle):

        return (
            ball.x < paddle.x + paddle.width
            and
            ball.x + BALL_SIZE > paddle.x
            and
            ball.y < paddle.y + paddle.height
            and
            ball.y + BALL_SIZE > paddle.y
        )



# ==========================
# main
# ==========================

def main():

    init_window(
        SCREEN_WIDTH,
        SCREEN_HEIGHT,
        "pong"
    )

    set_target_fps(60)


    game = PongGame()


    while not window_should_close():

        game.update()


        begin_drawing()

        clear_background(BLACK)

        game.draw()

        end_drawing()


    close_window()



if __name__ == "__main__":

    main()