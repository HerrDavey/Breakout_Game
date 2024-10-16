import tkinter
from turtle import Turtle, Screen
from tkinter import messagebox
import random
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
        self.paddle.penup()
        self.paddle.speed("fastest")
        self.paddle.setx(0)
        self.paddle.sety(-250)
        self.paddle.showturtle()
        self.paddle.color("navy")

        # Create game ball
        self.ball = Turtle()
        self.ball.shape("circle")
        self.ball.penup()
        self.ball.shapesize(0.9)
        self.ball.setx(0)
        self.ball.sety(0)
        self.ball.speed(20)

    def follow_mouse(self):
        x, y = self.screen._root.winfo_pointerx() - self.screen.window_width() // 1.29, self.screen._root.winfo_pointery() - self.screen.window_height() // 1.4
        if -470 < x < 470:
            self.paddle.setx(x)
        self.screen.update()
        self.screen.ontimer(self.follow_mouse, 10)

    def create_blocks(self):
        random_color = ["#" + ''.join([random.choice('0123456789ABCDEF') for j in range(6)])
                        for i in range(20)]
        self.blocks = []
        start_x = -452
        start_y = 260

        for _ in range(50):
            block = Turtle()
            block.hideturtle()
            block.color(random.choice(random_color))
            block.shapesize(1, 4.3)
            block.shape("square")
            block.penup()
            block.speed("fastest")
            block.goto(start_x, start_y)
            block.showturtle()

            self.blocks.append(block)
            start_x += 100

            if start_x > 452:
                start_x = -452
                start_y -= 25




    def block_impact(self, *args):
        for block in self.blocks:
            if abs(self.ball.xcor() - block.xcor()) < 50 and abs(self.ball.ycor() - block.ycor()) < 12.5:
                block.hideturtle()
                self.blocks.remove(block)
                return True
        return False


    def ball_movement(self):
        change_x = 6
        change_y = 6
        frame_duration = 0.01

        while len(self.blocks) > 0:
            start_time = time.time()  # Początek pętli

            self.ball.setx(self.ball.xcor() + change_x)
            self.ball.sety(self.ball.ycor() + change_y)
            self.screen.update()

            if self.ball.xcor() >= 485 or self.ball.xcor() <= -490:
                change_x *= -1

            if self.ball.ycor() >= 290:

                change_y *= -1

            if self.block_impact():
                change_y *= -1

            if self.ball.ycor() <= -285:
                break

            if self.paddle.ycor() - 12 <= self.ball.ycor() <= self.paddle.ycor() + 12:
                if self.paddle.xcor() - 60 < self.ball.xcor() < self.paddle.xcor() + 60:
                    change_y *= -1

                    if abs(self.ball.xcor() - self.paddle.xcor()) >= 20:
                        change_x *= -1

            end_time = time.time()
            elapsed_time = end_time - start_time

            if elapsed_time < frame_duration:
                time.sleep(frame_duration - elapsed_time)

        if len(self.blocks) > 0:
            messagebox.showinfo("DEFEAT!", "The ball fall under the paddle! \n\nGAME OVER!")
            self.screen.exitonclick()
        else:
            messagebox.showinfo("YOU WON!")



    def run_app(self):
        self.follow_mouse()
        self.create_blocks()
        self.ball_movement()
        self.screen.mainloop()

if __name__ == "__main__":
    game = Breakout_Game()
    game.run_app()
