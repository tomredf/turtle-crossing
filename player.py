from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.setheading(90)
        self.goto(STARTING_POSITION)

    def move_left(self):
        new_x = self.xcor() - MOVE_DISTANCE
        self.setpos(new_x, self.ycor())

    def move_right(self):
        new_x = self.xcor() + MOVE_DISTANCE
        self.setpos(new_x, self.ycor())

    def move_up(self):
        new_y = self.ycor() + MOVE_DISTANCE
        self.setpos(self.xcor(), new_y)

    def move_down(self):
        new_y = self.ycor() - MOVE_DISTANCE
        self.setpos(self.xcor(), new_y)