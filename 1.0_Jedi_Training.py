'''
1.0 Jedi Training (17pts)  Name:Jonathan Reischel

1. Define Forking (1pt): when someone makes a copy of a shared read only repository

2. Define Cloning (1pt): once a repository has been forked it can be cloned or (downloaded) onto a computer

3. Define Branching (1pt): a repository that has multiple types of code it can be grouped of into smaller chunks and
at any time it can be merged back into the master branch were all the code is located

4. Define Committing (1pt): it's like a checkpoint for a development in a project were you can record your changes

5. Define Merging (1pt): when someone has forked your piece of code they can make a pull request and if accepted will
merge into the original code

6. Define Pushing (1pt): a term used to describe uploading code to your forked remote

7. Define Pull Request (1pt): when a request is made it ask the owner of the project to pull or to take changes to there
code

8. TURTORIAL ART (10pts.)

Modify the starter code below to create your own cool drawing.
Make sure you keep the last two lines of code!!!!
Your first and last name must be written on your art.
The last line keeps the window open until you click to close.
Turtle Documentation: https://docs.python.org/3.3/library/turtle.html?highlight=turtle
'''
import turtle
from turtle import Turtle

tina = turtle.Turtle()

tina.color('red')
tina.shape('turtle')

tina.penup()
tina.goto(-150, 180)
tina.begin_fill()
tina.pendown()
tina.right(90)
tina.forward(300)
tina.goto(-80, -190)
tina.left(90)
tina.forward(60)
tina.left(90)
tina.forward(40)
tina.left(90)
tina.forward(40)
tina.goto(-90, -120)
tina.right(90)
tina.forward(300)
tina.left(90)
tina.forward(60)
tina.end_fill()
tina.pendown()

tommy = turtle.Turtle()
tommy.shape('turtle')
tommy.color('blue')

tommy.penup()
tommy.goto(150, 180)
tommy.begin_fill()
tommy.pendown()
tommy.right(90)
tommy.forward(300)
tommy.goto(80, -190)
tommy.right(90)
tommy.forward(60)
tommy.right(90)
tommy.forward(40)
tommy.right(90)
tommy.forward(40)
tommy.goto(90, -120)
tommy.left(90)
tommy.forward(300)
tommy.right(90)
tommy.forward(60)
tommy.end_fill()
tommy.pendown()
tommy.penup()
tommy.goto(-60, 180)
tommy.pendown()

tommy.write('Jonathan Reischel', font=("Arial", 16, "normal"))   # sign your name to your art
turtle.exitonclick()   # Keeps pycharm window open so we can see the drawing
