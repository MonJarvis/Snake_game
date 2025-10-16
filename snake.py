from turtle import Turtle
import random
MOVE_DISTANCE = 20
class Snake:
    def __init__(self):
        self.segments = []
        self.segments_count = 3
        self.create_snake()

    def create_snake(self):
        """Create the Snake."""
        positions = [(0, 0), (-20, 0), (-40, 0)]
        for _ in range(self.segments_count):
            snake = Turtle()
            snake.shape("square")
            snake.color("white")
            snake.penup()
            snake.goto(positions[_])
            self.segments.append(snake)

    def create_segment(self, position):
        new_segment = Turtle("square")
        new_segment.color(random_color())
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)
        self.segments_count += 1
        return new_segment

    def move(self):
        for segments in range (len(self.segments)-1,0,-1):
            self.segments[segments].color(random_color())
            new_x = self.segments[segments - 1].xcor()
            new_y = self.segments[segments - 1].ycor()
            self.segments[segments].goto(new_x, new_y)
        self.segments[0].forward(MOVE_DISTANCE)

    def move_up(self):
        for segment in self.segments:
            if segment.heading() != 270:
                self.segments[0].setheading(90)
        
    def move_down(self):
        for segment in self.segments:
            if segment.heading() != 90:
                self.segments[0].setheading(270)

    def move_left(self):
        for segment in self.segments:
            if segment.heading() != 0:
                self.segments[0].setheading(180)

    def move_right(self):
        for segment in self.segments:
            if segment.heading() != 180:
                self.segments[0].setheading(0)
def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color