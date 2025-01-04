# Assignment 1: Design Your Own Class
class Smartphone:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price

    def make_call(self, number):
        return f"Dialing {number} from {self.brand} {self.model}..."

    def send_message(self, number, message):
        return f"Sending '{message}' to {number} from {self.brand} {self.model}."

class GamingSmartphone(Smartphone):
    def __init__(self, brand, model, price, gpu):
        super().__init__(brand, model, price)
        self.gpu = gpu

    def play_game(self, game):
        return f"Playing {game} on {self.brand} {self.model} with {self.gpu} GPU."

# Example usage:
phone = Smartphone("Apple", "iPhone 15", 999)
gaming_phone = GamingSmartphone("Asus", "ROG Phone 7", 1299, "Adreno 730")

print(phone.make_call("123-456-7890"))
print(gaming_phone.play_game("Genshin Impact"))

# Activity 2: Polymorphism Challenge
class Animal:
    def move(self):
        return "This animal moves in its own way."

class Bird(Animal):
    def move(self):
        return "Flying high in the sky! ✈️"

class Fish(Animal):
    def move(self):
        return "Swimming through the water! 🌊"

class Dog(Animal):
    def move(self):
        return "Running on the ground! 🐕"

# Example usage:
animals = [Bird(), Fish(), Dog()]
for animal in animals:
    print(animal.move())
