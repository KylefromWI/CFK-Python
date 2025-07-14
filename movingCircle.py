import turtle #requires tkinter, run in VS Code
import time

# Screen setup
screen = turtle.Screen()
screen.setup(width=700, height=700)
screen.bgcolor("white")
screen.title("Moving Circle")

# Turtle setup
pen = turtle.Turtle()
pen.speed(0)  # Set to fastest speed
pen.hideturtle()
pen.penup()
pen.color("blue")
pen.shape("circle")

# Initial circle parameters
radius = 50
x, y = 0, -100
pen.goto(x, y)
pen.pendown()
pen.pensize(3)

# Animation parameters
angle = 0
speed = 2

# Animation loop
while True:
    angle += speed
    x = radius * 2 * turtle.getscreen().window_width()/700 * (2 * (angle/360) - (angle//360)) # calculate x position based on angle
    y = radius * turtle.getscreen().window_height()/700 * (0.8*turtle.sin(angle * (3.14159/180))) # calculate y position based on angle
    pen.goto(x, y) # move to new position

    if x > screen.window_width()/2 - radius or x < -screen.window_width()/2 + radius:
       speed = -speed # Reverse direction when hitting screen edge

    time.sleep(0.01) # Adjust animation speed

screen.mainloop()
