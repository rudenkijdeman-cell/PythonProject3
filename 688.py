class Car:
    def __init__(self, make, year, model):
        self.make = make
        self.year = year
        self.model = model

    def get_info(self):
        return f"Марка: {self.make}, Модель: {self.model}, рік: {self.year}"

car1 = Car("Toyota", 2022, "Camry")
car2 = Car("BMW", 2021, "X5")
car3 = Car("Ford", 2023, "Mustang")

print("type model car")
user_car = input()

if user_car == "Toyota":
    print(car1.get_info())
elif user_car == "BMW":
    print(car2.get_info())
elif user_car == "Ford":
    print(car3.get_info())
else:
    print("we dont find this car try Toyota,BMW,Ford")

input()

