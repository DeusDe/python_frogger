from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()

        self.level = 0
        self.hideturtle()
        self.color("black")
        self.update_level()

    def update_level(self):  #
        self.level += 1
        self.show_level()

    def show_level(self):
        self.teleport(-280, 260)
        self.write(f"Level: {self.level}", font=FONT)
