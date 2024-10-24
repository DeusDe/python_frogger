from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("black")
        self.setheading(90)
        self.hideturtle()
        self.penup()
        self.goto(STARTING_POSITION)
        self.showturtle()


    def move(self):
        self.forward(10)


    def finish_line(self):
        if self.ycor() > FINISH_LINE_Y:
            print(self.ycor())
            return True
        return False
