
class Pet:
    def __init__(self, name, type, age, gender):
        self.name = name
        self.type = type
        self.age = age
        self.gender = gender

    def get_info(self):
        return self.name, self.type, self.age, self.gender

class Dog(Pet):
    def __init__(self, name, type, age, gender):
        super().__init__(name, type, age, gender)
    def woof(self):
        return "Гав"

class Cat(Pet):
    def __init__(self, name, type, age, gender):
        super().__init__(name, type, age, gender)
    def meow(self):
        return "Мяу"

dog  = Dog("dogee", "dog", 1, "male")
cat  = Cat("cette", "cat", 5, "female")

print(dog.get_info())
print(dog.woof())

print(cat.get_info())
print(cat.meow())