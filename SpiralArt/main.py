# Spiral art

from turtle import *

# Adjust these variables

SIDES = 4           # Number of sides for the shape we use to spiral
ANGLE = 91          # Rotation after each shape
ITERATIONS = 200    # Number of iterations
GROWTH = 1          # Controls how much the shape grows per iteration

PEN_SIZE = 2
BACKGROUND = (0, 0, 0) # RGB Value
PEN_COLOUR = (255, 255, 255)

def draw_shape(t: Turtle, size: float) -> None:
    angle = 360 / SIDES

    for _ in range(SIDES):
        t.forward(size)
        t.right(angle)

def main() -> None:
    screen = Screen()
    screen.colormode(255)
    screen.bgcolor(BACKGROUND)

    t = Turtle()
    t.speed(0)
    t.pensize(PEN_SIZE)
    t.hideturtle()

    size = 50

    for i in range(ITERATIONS):

        t.pencolor(PEN_COLOUR)

        draw_shape(t, size)

        t.right(ANGLE)
        size += GROWTH

    done()

if __name__ == "__main__":
    main()