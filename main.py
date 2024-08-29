from turtle import Turtle, Screen
import time

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

        # Create game ball
        self.ball = Turtle()
        self.ball.shape("circle")
        self.ball.penup()
        self.ball.shapesize(0.75)
        self.ball.setx(0)
        self.ball.sety(0)

    def follow_mouse(self):
        x, y = self.screen._root.winfo_pointerx() - self.screen.window_width() // 1.29, self.screen._root.winfo_pointery() - self.screen.window_height() // 1.4
        if -470 < x < 470:
            self.paddle.setx(x)
        self.screen.update()
        self.screen.ontimer(self.follow_mouse, 10)


    def ball_movement(self):
        change_x = 0.1
        change_y = 0.1
        while True:
            self.screen.update()
            self.ball.setx(self.ball.xcor() + change_x)
            self.ball.sety(self.ball.ycor() + change_y)

            if self.ball.xcor() >= 485 or self.ball.xcor() <= -490:
                change_x *= -1

            if self.ball.ycor() >= 290:
                change_y *= -1

            if self.ball.ycor() <= -285 and (self.ball.xcor() - 60 < self.ball.xcor() < self.ball.xcor() + 60):
                change_y *= -1

            # TODO 6: Change impact only in one point in paddle to all paddle size
            if int(self.ball.xcor()) == int(self.paddle.xcor()) and int(self.ball.ycor()) == int(self.paddle.ycor()):
                change_x *= -1
                change_y *= -1


    def run_app(self):
        self.follow_mouse()
        self.ball_movement()
        self.screen.mainloop()


if __name__ == "__main__":
    game = Breakout_Game()
    game.run_app()
