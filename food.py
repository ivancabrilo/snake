from turtle import Turtle
import random
colors = ["red", "orange", "yellow", "blue","green","purple"]
class Food(Turtle):
    

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.color(random.choice(colors))
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.speed("fastest")
        self.refresh()
        

    def refresh(self):
        self.color(random.choice(colors))
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.goto(random_x, random_y)

