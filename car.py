from turtle import Turtle

import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]


class Car(Turtle):
    def __init__(self):
        super().__init__()
        random_y = random.randint(-300, 300)
        self.color(COLORS[random.randint(0, len(COLORS) - 1)])
        self.shape("square")
        self.shapesize(1, 3, 0)
        self.hideturtle()
        self.penup()
        self.goto(300, random_y)
        self.setheading(180)
        self.showturtle()
        self.move_speed = random.randint(750, 1250)/1000

    def forward(self, distance):
        distance *= self.move_speed
        super().forward(distance)

    def check_for_wall_hit(self):
        if self.xcor() < -350:
            random_y = random.randint(-300, 300)
            self.goto(350,random_y)