# Hit the Target Game
import turtle
import math
#Initialise Turtle
wn = turtle.Screen()
turtle.Turtle()
turtle.color("green")
turtle.shape("turtle")
# Named constants
SCREEN_WIDTH = 600 # Screen width
SCREEN_HEIGHT = 600 # Screen height
TARGET_LLEFT_X = 100 # Target's lower-left X
TARGET_LLEFT_Y = 250 # Target's lower-left Y
TARGET_WIDTH = 25 # Width of the target
FORCE_FACTOR = 30 # Arbitrary force factor
PROJECTILE_SPEED = 1 # Projectile's animation speed
NORTH = 90 # Angle of north direction
SOUTH = 270 # Angle of south direction
EAST = 0 # Angle of east direction
WEST = 180 # Angle of west direction
# Setup the window.
turtle.setup(SCREEN_WIDTH, SCREEN_HEIGHT)
# Draw the target.
turtle.hideturtle()
turtle.speed(0)
turtle.penup()
turtle.goto(TARGET_LLEFT_X, TARGET_LLEFT_Y)
turtle.pendown()
turtle.setheading(EAST)
turtle.forward(TARGET_WIDTH)
turtle.setheading(NORTH)
turtle.forward(TARGET_WIDTH)
turtle.setheading(WEST)
turtle.forward(TARGET_WIDTH)
turtle.setheading(SOUTH)
turtle.forward(TARGET_WIDTH)
turtle.penup()
# Center the turtle.
turtle.goto(0, 0)
turtle.setheading(EAST)
turtle.showturtle()
turtle.speed(PROJECTILE_SPEED)
# Get the angle and force from the user.
angle = float(input("Enter the projectile's angle: "))
force = float(input("Enter the launch force (1−10): "))
# Calculate the distance.
distance = force * FORCE_FACTOR
# Set the heading.
turtle.setheading(angle)
# Launch the projectile.
turtle.pendown()
turtle.forward(distance)
# Did it hit the target?
if (turtle.xcor() >= TARGET_LLEFT_X and
    turtle.xcor() <= (TARGET_LLEFT_X + TARGET_WIDTH) and
    turtle.ycor() >= TARGET_LLEFT_Y and
    turtle.ycor() <= (TARGET_LLEFT_Y + TARGET_WIDTH)):
        print('  Target hit, you won the game!')
else:
        print('  You missed the target.')

        #Calculate Angle and Distance to box using Trigonometry
        TRIANGLE_WIDTH = TARGET_LLEFT_X + TARGET_WIDTH/2
        TRIANGLE_HEIGHT = TARGET_LLEFT_Y + TARGET_WIDTH/2

        #Use Pythagoras to find distance from starting point center of box
        CORRECT_DISTANCE = math.sqrt(TRIANGLE_WIDTH**2 + TRIANGLE_HEIGHT**2)

        #Use asin to find angle from starting point to center of box
        CORRECT_ANGLE = math.asin(TRIANGLE_HEIGHT / CORRECT_DISTANCE) * 180/math.pi

        #Display to the user if they need more/less angle/force (with leniency of 3)
        if (angle < CORRECT_ANGLE - 3):
            print('Use a greator angle')
        else:
            if (angle > CORRECT_ANGLE + 3):
                print('Use a lessor angle')

        if (distance < CORRECT_DISTANCE - 3):
            print('Use more force')
        else:
            if (distance > CORRECT_DISTANCE + 3):
                print('Use less force')
turtle.done()
