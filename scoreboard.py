from turtle import Turtle


class Score (Turtle):

    def __init__(self):
        super().__init__()
        
        self.penup()
        self.score = 0
        self.color("white")
        self.goto(0, 275)
        self.write(f"Score: {self.score}", align="center", font=("Courier", 20, "normal"))
        self.hideturtle()

    def update(self):
        self.clear()
        self.score += 1
        self.write(f"Score: {self.score}", align="center", font=("Courier", 20, "normal"))
       
        

        
    def game_over(self):
        self.goto(0,0)
        self.color("White")
        self.write("GAME OVER", align="center", font=("Courier", 30, "normal"))