import turtle

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("white")

# Create a turtle object
heart = turtle.Turtle()
heart.color("red")
heart.speed(3)

# Function to draw a heart
def draw_heart():
    heart.begin_fill()
    heart.left(140)
    heart.forward(180)
    heart.circle(-90, 200)
    heart.left(120)
    heart.circle(-90, 200)
    heart.forward(180)
    heart.end_fill()

# Draw the heart
draw_heart()

# Hide the turtle
heart.hideturtle()

# Create another turtle object for writing text
text_turtle = turtle.Turtle()
text_turtle.color("black")
text_turtle.penup()
text_turtle.hideturtle()
text_turtle.goto(0, -50)
text_turtle.write("I Love You Payal", align="center", font=("Arial", 24, "normal"))

# Keep the window open
turtle.done()