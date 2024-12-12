import turtle

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("white")

# Create a turtle for drawing
pen = turtle.Turtle()
pen.speed(10)
pen.up()

# Colors for Google logo
colors = ["blue", "red", "yellow", "green", "blue"]

# Define the positions for each letter
font = ("Arial", 30, "bold")

# Letters and text to repeat
letters = "Google"

# Function to draw the text 'Google' with specific colors
def draw_google_logo():
    positions = [(-200, 0), (-100, 0), (0, 0), (100, 0), (200, 0)]
    for i in range(len(letters)):
        pen.goto(positions[i])
        pen.color(colors[i])
        pen.write(letters[i], font=font)

# Draw the Google logo multiple times
for _ in range(5):
    draw_google_logo()
    pen.setheading(90)  # Rotate the pen to draw vertically after each set
    pen.forward(50)  # Move downward for the next logo
    pen.setheading(0)  # Reset the pen to horizontal for the next line

# Hide the turtle
pen.hideturtle()

# Keep the window open until clicked
screen.exitonclick()
