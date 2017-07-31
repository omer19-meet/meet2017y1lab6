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
    return("you pressed Up")

def left():
    global direction
    global UP
    global LEFT
    global 
    direction = LEFT
    print(direction)
    return("you pressed Left")


turtle.mainloop()

