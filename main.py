from idlelib.configdialog import changes
from turtle import *
from random import randrange
from freegames import square, vector

# Three elements of the game
food = vector(0, 0)
snake = [vector(10, 0)]
aim = vector(0, -10)


# Defining change function
def change(x, y):
    aim.x = x  # aim.x represents the x-axis
    aim.y = y  # aim.y represents the y-axis


# Defining inside function
def inside(head):
    return -340 < head.x < 320 and -280 < head.y < 280  # This is the range of the square.
    # The snake must not go out of this range.


# Defining the move function
def move():
    # Snake's head will always move in the forward direction.
    # Therefore, we need to move the snake's head by -1.
    # -1 is considered as 1 unit in the forward direction.
    head = snake[-1].copy()
    head.move(aim)

    # Out conditions:
    # 1. If head of the snake touches the boundary.
    # 2. Or if head the snake touches itself.
    if not inside(head) or head in snake:
        square(head.x, head.y, 9, "red")  # If out, then head of the snake will be red.
        update()
        return

    snake.append(head)  # It will add button, if the above conditions are satisfied.

    # Conditions if the snake meets the food
    if head == food:
        print("Score: ", len(snake) - 1)  # This will return the Score when the snake eats the food on the output window

        # Coordinates of food
        food.x = randrange(-15, 15) * 10
        food.y = randrange(-15, 15) * 10

    else:
        snake.pop(0)

    clear()

    # Creating a for loop, to create the body of the snake
    for body in snake:
        square(body.x, body.y, 9, "green")

    # Creating Food
    square(food.x, food.y, 9, "red")
    update()
    ontimer(move, 100)


hideturtle()  # This will hide the turtle, who is drawing.
tracer(False)  # This will turn off the automatic screen updates
# This tracer will bring back the elements to its initial stage.

listen()  # Turtle Listen allows us to detect when the user has hit certain keys on the keyboard or moved/clicked the mouse.
# This listen will continually update the game every second.

# Setting the controls for the game.
onkey(lambda: change(10, 0), "Right")   # Here, 10 units is equal to 1 unit of the box.
onkey(lambda: change(-10, 0), "Left")
onkey(lambda: change(0, 10), "Up")
onkey(lambda: change(0, -10), "Down")

move()
done()
