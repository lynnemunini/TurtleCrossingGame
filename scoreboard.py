from turtle import Turtle
FONT = ('Courier', 10, 'bold')
ALIGNMENT = 'center'


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.color("black")
        self.hideturtle()
        self.penup()
        self.goto(x=-150, y=260)
        self.write(f"Level: {self.level}", move=False, align=ALIGNMENT, font=FONT)

    def increase_level(self):
        self.level += 1
        self.clear()
        self.write(f"Level: {self.level}", move=False, align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(x=0, y=0)
        self.write("YOU DIED!", move=False, align=ALIGNMENT, font=FONT)
