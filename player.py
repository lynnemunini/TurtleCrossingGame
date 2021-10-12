from turtle import Turtle
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280
UP = 90

# Create a  turtle player that starts out at the bottom of the screen and listen for the "Up" keypress to move the
# turtle north


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("seaGreen")
        self.left(90)
        self.penup()
        self.go_to_start()

    def go_up(self):
        if self.heading() == UP:
            new_y = self.ycor() + MOVE_DISTANCE
            self.goto(self.xcor(), y=new_y)

    def go_to_start(self):
        self.goto(STARTING_POSITION)

    def is_at_finish_line(self):
        if self.ycor() > FINISH_LINE_Y:
            return True
        else:
            return False
