import turtle
from turtle import Turtle, Screen

s = Screen()
s.setup(1000, 600)
s.tracer(0)
s.cv._rootwindow.resizable(False, False)



t = Turtle()
t.hideturtle()
t.shape("square")
t.shapesize(1, 6)
t.penup()
t.speed("fastest")
t.setx(0)
t.sety(-250)
t.showturtle()


def follow_mouse():
    x, y = s._root.winfo_pointerx() - s.window_width() // 1.29, s._root.winfo_pointery() - s.window_height() // 1.4
    if -470 < x < 470:
        t.setx(x)
    s.update()
    s.ontimer(follow_mouse, 10)

def main():
    follow_mouse()
    s.mainloop()

main()


# TODO 1: Paddle should follow the mouse pointer
# TODO 2: Make the paddle borders on Screen border
# TODO 3: Create the ball
# TODO 4: Adjustment basic ball movement
# TODO 5: Make contact and change moving direction
