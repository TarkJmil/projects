class Car:
    def __init__(self, model, color, speed=0):
        """
        Initializes a new Car object.

        Args:
            model (str): The model of the car.
            color (str): The color of the car.
            speed (int, optional): The initial speed of the car. Defaults to 0.
        """
        self.model = model
        self.color = color
        self.speed = speed

    def accelerate(self, amount):
        """
        Increases the speed of the car by a certain amount.

        Args:
            amount (int): The amount to increase the speed by.
        """
        self.speed += amount

    def brake(self, amount):
        """
        Decreases the speed of the car by a certain amount.

        Args:
            amount (int): The amount to decrease the speed by.
        """
        if self.speed - amount >= 0:
            self.speed -= amount
        else:
            self.speed = 0

    def display_info(self):
        """
        Displays information about the car.
        """
        print(f"Model: {self.model}")
        print(f"Color: {self.color}")
        print(f"Speed: {self.speed} km/h")

# إنشاء instance من الفئة Car
my_car = Car("Toyota Camry", "Silver")

# تعديل instance الكائن my_car
my_car.accelerate(50)
my_car.brake(20)
my_car.display_info()