from turtle import Turtle
import random as ran
COLORS = ["green", "blue", "red", "yellow", "lightblue", "purple", "orange"]

class Food(Turtle):
    
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_wid=0.7, stretch_len=0.7)  # 20 * 0.5 = 10
        self.speed("fastest")
        self.refresh_location()

    def refresh_location(self):
        x_random = ran.randint(-280, 280)
        y_random = ran.randint(-230, 230)
        self.color(ran.choice(COLORS))
        self.goto(x_random, y_random)
