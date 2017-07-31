import turtle

##turtle.shape('turtle')
##square = turtle.clone()
##square.shape('square')
##square.goto(0,100)
##square.stamp()
##square.goto(100,100)
##square.stamp()
##square.goto(100,0)
##square.stemp()
##square.goto(0,0)


##triangle = turtle.clone()
##triangle.shape('triangle')
##triangle.pendown()
##triangle.goto(100, 0)
##
##triangle.goto(50,100)
##triangle.goto(0,0)
turtle.pendown()

UP_ARROW = "Up"
LEFT_ARROW = "Left"
DOWN_ARROW = "Down"
RIGHT_ARROW = "Right"
SPACEBAR = "space"


UP = 0
LEFT = 1
DOWN = 2
RIGHT = 3

direction = UP

def up():
    global direction
    direction = UP
    print(direction)
    return("you pressed Up")

def left():
    global direction
    direction = LEFT
    print(direction)
    return("you pressed Left")

def down():
    global direction
    direction = DOWN
    print(direction)
    return("you pressed Down")
           
def right():
    global direction
    direction = RIGHT
    print(direction)
    return("you pressed Right")

turtle.onkeypress(up, UP_ARROW)
turtle.onkeypress(down, DOWN_ARROW)
turtle.onkeypress(left, LEFT_ARROW)
turtle.onkeypress(right, RIGHT_ARROW)

turtle.listen()
print("Alexander the GREAT")
turtle.mainloop()

