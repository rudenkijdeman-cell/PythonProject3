#class Car:
#    def __init__(self, make, year, model):
#        self.make = make
#        self.year = year
#        self.model = model

#    def get_info(self):
#        return f"Марка: {self.make}, Модель: {self.model}, рік: {self.year}"

#car1 = Car("Toyota", 2022, "Camry")
#car2 = Car("BMW", 2021, "X5")
#car3 = Car("Ford", 2023, "Mustang")

#print("type model car")
#user_car = input()

#if user_car == "Toyota":
    #print(car1.get_info())
#elif user_car == "BMW":
    #print(car2.get_info())
#elif user_car == "Ford":
    #print(car3.get_info())
#else:
    #print("we dont find this car try Toyota,BMW,Ford")

#input()

#class Animal:
    #satiety = 60
    #energy = 50
    #mood = 50

#class Cat(Animal):
    #mood = 80
    #def action(self):
        #if self.satiety < 30:
            #print("Котик голодний, йде їсти!")
            #self.satiety += 40
        #else:
            #print("Котик ситий і грається!")
            #self.energy -= 20

#class Dog(Animal):
    #energy = 90

#barsik = Cat()
#tapok = Dog()

#print(barsik.satiety)
#print(tapok.satiety)

#class people:
    #happiness = 100
    #health = 100
    #love = 100

#class birthday_girl(people):
    #satiety = 100
    #dreams = "здійснюються"
    #mood = "найкраще "

#inka = birthday_girl()

#print("З Днем народження, Інко!")
#print("Рівень щастя:", inka.happiness)
#print("Рівень здоров'я:", inka.health)
#print("Настрій сьогодні:", inka.mood)
import random

class Encryptor:
    def __init__(self, a, b):
        self.__a = a
        self.__b = b

    def __secret_math(self):
        op = random.randint(1, 3)
        if op == 1:
            return self.__a + self.__b
        if op == 2:
            return self.__a - self.__b
        if op == 3:
            return self.__a * self.__b

    def __str__(self):
        return str(self.__secret_math())

# Введення даних з клавіатури
num1 = int(input("Введіть перше число: "))
num2 = int(input("Введіть друге число: "))

obj = Encryptor(num1, num2)
print("Результат:", obj)

#print(obj.__a)#тут є захист програми
