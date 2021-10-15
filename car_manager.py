from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
NUM_CARS = 25


class CarManager():
    def __init__(self):
        self.cars = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def add_car(self):
        random_chance = random.randint(1, 6)
        if random_chance == 1:
            c = Turtle()
            c.color(random.choice(COLORS))
            c.shape("square")
            c.shapesize(1, 2)
            c.penup()
            rand_x = 300
            rand_y = random.randint(-250, 250)
            pos = (rand_x, rand_y)
            c.goto(pos)
            self.cars.append(c)

    def move_cars(self):
        for car in self.cars:
            car.backward(self.car_speed)

    def level_up(self):
        self.car_speed += MOVE_INCREMENT