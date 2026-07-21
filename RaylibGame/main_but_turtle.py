import turtle
import random
import time

def main():
    # Screen setup
    screen = turtle.Screen()
    screen.title("Dodge the Falling Objects! (Turtle Edition)")
    screen.bgcolor("white")
    screen.setup(width=800, height=600)
    screen.tracer(0) # Turn off animation for smoother movement

    # Player setup
    player = turtle.Turtle()
    player.shape("square")
    player.color("blue")
    player.shapesize(stretch_wid=2, stretch_len=2) # 40x40 pixels
    player.penup()
    player.goto(0, -250)

    # Game variables
    player_speed = 20
    enemies = []
    enemy_colors = ["red", "green", "purple", "orange", "gold", "maroon"]
    enemy_speed = 3
    score = 0
    game_over = False

    # Score display
    pen = turtle.Turtle()
    pen.hideturtle()
    pen.penup()
    pen.goto(-380, 260)
    pen.write(f"Score: {score}", align="left", font=("Arial", 16, "normal"))

    # Movement functions
    def move_left():
        x = player.xcor()
        if x > -380:
            player.setx(x - player_speed)

    def move_right():
        x = player.xcor()
        if x < 380:
            player.setx(x + player_speed)

    # Keyboard bindings
    screen.listen()
    screen.onkeypress(move_left, "Left")
    screen.onkeypress(move_right, "Right")

    # Game loop
    last_spawn_time = time.time()
    
    while True:
        if not game_over:
            # Spawn enemies every 1 second
            if time.time() - last_spawn_time > 1.0:
                enemy = turtle.Turtle()
                enemy.shape("square")
                enemy.color(random.choice(enemy_colors))
                enemy.shapesize(stretch_wid=2, stretch_len=2)
                enemy.penup()
                enemy.goto(random.randint(-380, 380), 300)
                enemies.append(enemy)
                last_spawn_time = time.time()

            # Move enemies
            for enemy in enemies[:]:
                enemy.sety(enemy.ycor() - enemy_speed)

                # Collision detection
                if enemy.distance(player) < 30:
                    game_over = True

                # Remove off-screen enemies
                if enemy.ycor() < -300:
                    enemy.hideturtle()
                    enemies.remove(enemy)
                    score += 1
                    pen.clear()
                    pen.write(f"Score: {score}", align="left", font=("Arial", 16, "normal"))
                    # Increase difficulty
                    if score % 10 == 0:
                        enemy_speed += 0.5

        else:
            pen.goto(0, 0)
            pen.write("GAME OVER!", align="center", font=("Arial", 24, "bold"))
            pen.goto(0, -30)
            pen.write("Close window to exit", align="center", font=("Arial", 14, "normal"))
            # Turtle doesn't have a simple 'R' restart without complex state reset, 
            # so we'll just end the loop or wait for window close.
            screen.update()
            time.sleep(1)
            break

        screen.update()
        time.sleep(0.02) # Approx 50 FPS

    screen.mainloop()

if __name__ == "__main__":
    main()
