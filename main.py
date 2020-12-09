from turtle import Turtle, Screen

# Initialise Turtle object references
timmy = Turtle()
screen = Screen()

# Initialise Turtle setup
screen.listen()


# Movement functions
def move_forwards():    timmy.forward(10)
def move_backward():    timmy.back(10)
def turn_left():        timmy.left(10)
def turn_right():       timmy.right(10)
def clear_screen():     screen.reset()

# Add actionlisteners and link movement functions
screen.onkey(key="w", fun=move_forwards)
screen.onkey(key="a", fun=turn_left)
screen.onkey(key="s", fun=move_backward)
screen.onkey(key="d", fun=turn_right)
screen.onkey(key="c", fun=clear_screen)

# A
screen.exitonclick()
