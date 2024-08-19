import turtle
from turtle import Turtle, Screen

class Breakout_Game:

    def __init__(self):

        # Screen Settings
        self.screen = Screen()
        self.screen.setup(1000, 600)
        self.screen.tracer(0)
        self.screen.cv._rootwindow.resizable(False, False)

        # Paddle Settings
        self.paddle = Turtle()
        self.paddle.hideturtle()
        self.paddle.shapesize(1, 6)
        self.paddle.shape("square")
        self.paddle .penup()
        self.paddle.speed("fastest")
        self.paddle.setx(0)
        self.paddle.sety(-250)
        self.paddle.showturtle()

        # Activate tracking mouse pointer by paddle
        self.follow_mouse()


    def follow_mouse(self):
        x, y = self.screen._root.winfo_pointerx() - self.screen.window_width() // 1.29, self.screen._root.winfo_pointery() - self.screen.window_height() // 1.4
        if -470 < x < 470:
            self.paddle.setx(x)
        self.screen.update()
        self.screen.ontimer(self.follow_mouse, 10)

    def run_app(self):
        self.screen.mainloop()

if __name__ == "__main__":
    game = Breakout_Game()
    game.run_app()


# TODO 3: Create the ball
# TODO 4: Adjustment basic ball movement
# TODO 5: Make contact and change moving direction
