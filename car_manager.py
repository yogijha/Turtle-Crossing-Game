from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
INCREASE_SPEED=10

class CarManager(Turtle):

    def __init__(self):
        super().__init__()
        self.all_cars=[]
        self.hideturtle()
        self.car_speed= STARTING_MOVE_DISTANCE


    def create_car(self):
        rand_int = random.randint(0, 6)
        if rand_int == 1:
            new_car = Turtle('square')
            new_car.penup()
            new_car.shape('square')
            new_car.shapesize(1,2)
            new_car.color(random.choice(COLORS))
            rand_y= random.randint(-250, 250)
            new_car.goto(300, rand_y)
            self.all_cars.append(new_car)

    def move_cars(self):
        for car in self.all_cars:
            car.backward(self.car_speed)

    def level_up(self):
        self.car_speed += INCREASE_SPEED