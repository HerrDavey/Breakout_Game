import turtle
from turtle import Turtle, Screen

s = Screen()
s.setup(1000, 600)



t = Turtle()
t.hideturtle()
t.shape("square")
t.shapesize(1, 6)
t.penup()
t.speed("fastest")
t.setx(0)
t.sety(-250)
t.showturtle()

def dragging(x, y):
    t.ondrag(None)
    t.setheading(0)
    t.goto(x, -250)
    t.ondrag(dragging)

def main():
    turtle.listen()
    t.ondrag(dragging)
    s.mainloop()


main()



