import turtle

WIDTH = 500
HEIGHT = 500
DELAY = 20

def move_turtle():
    stamper.forward(1)
    stamper.right(1)
    screen.update()
    screen.ontimer(move_turtle, DELAY)

screen = turtle.Screen()
screen.setup(WIDTH, HEIGHT)
screen.title("Snake Game")
screen.bgcolor("cyan")
screen.tracer(0)

stamper = turtle.Turtle() # module = class # class within the module
stamper.shape('square')
stamper.color('red')
stamper.shapesize(50 / 20)
stamper.stamp()
stamper.penup()
stamper.shapesize(10 / 20)
stamper.goto(100, 100)
stamper.stamp()

move_turtle()

turtle.done()