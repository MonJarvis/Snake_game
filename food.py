from turtle import Turtle
from snake import random_color
import random
prime_numbers = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
class Food(Turtle):
    def __init__(self,prime):
        super().__init__()
        self.prime = prime
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color(random_color())
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        randomx = random.randint(-280, 280)
        randomy = random.randint(-280, 280)
        self.goto(randomx, randomy)
        if self.prime == True:
            number = random.choice(prime_numbers)
        else:
            number = random.randint(1, 100)
            if number in prime_numbers:
                number += 1  # Ensure it's not prime by adding 1 (simple way)
        self.fillcolor("")  # Set the circle's color
        self.pencolor(random_color())  # Set the pen color to black for the text
        self.write(f"{number}", align="center", font=("Arial", 12, "bold"))  # Add text inside the circle
        self.fillcolor(random_color())  # Restore the fill color

    def remove_text(self):
        self.clear()