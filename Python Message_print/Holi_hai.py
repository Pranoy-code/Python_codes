import turtle
import random

# Setup screen
screen = turtle.Screen()
screen.bgcolor("Sky Blue")  # Navy Blue Background
screen.title("Happy Holi!")

# Turtle for text
text_turtle = turtle.Turtle()
text_turtle.speed(0)
text_turtle.hideturtle()

# Turtle for splashes
splash_turtle = turtle.Turtle()
splash_turtle.speed(0)
splash_turtle.hideturtle()
splash_turtle.width(10)  # Thicker splashes

# List of bright Holi colors
colors = ["red", "yellow", "green", "purple", "orange", "pink", "cyan"]
Letter_colors = ["red", "yellow", "green",  "orange", ]
# Define the safe zone where text will appear
safe_x_min, safe_x_max = -200, 200
safe_y_min, safe_y_max = -110, 110

# Function to draw a thick splash
def draw_splash(x, y, size):
    splash_turtle.penup()
    splash_turtle.goto(x, y)
    splash_turtle.pendown()
    
    splash_turtle.color(random.choice(colors))
    splash_turtle.pensize(8)  # Make the strokes thicker
    
    for _ in range(12):  # More lines for a fuller splash
        splash_turtle.forward(size)
        splash_turtle.backward(size)
        splash_turtle.left(30)

# Draw multiple splashes randomly but outside the text area
for _ in range(25):
    while True:
        x = random.randint(-300, 300)
        y = random.randint(-200, 200)
        
        # Ensure the splash is outside the safe text area
        if not (safe_x_min < x < safe_x_max and safe_y_min < y < safe_y_max):
            break  # Valid position found

    size = random.randint(20, 60)
    draw_splash(x, y, size)

# Function to display "Happy Holi"
def display_text():
    text_turtle.penup()
    text_turtle.goto(-120, 0)
    text_turtle.pendown()
    
    for letter in "Happy Holi!":
        text_turtle.color(random.choice(Letter_colors))
        text_turtle.write(letter, font=("Arial", 36, "bold"))
        text_turtle.forward(30)

# Display text with colors
display_text()

# Keep the window open
turtle.done()
