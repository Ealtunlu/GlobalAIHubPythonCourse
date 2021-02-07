# Create three classes named Animals, Dogs and Cats Add some features to these 
# classes Create some functions with these attributes. Don't forget! You have to do it using inheritance.
class Animal:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def is_mammel(self):
        return None

class Dogs(Animal):
    def __init__(self,name,age):
        super().__init__(name,age)
    def speak(self):
        return "Woof"
    def likes_walks(self):
        return True
    def is_good_boy(self):
        return True
    def is_mammel(self):
        return True

class Cats(Animal):
    def __init__(self,name,age):
        super().__init__(name,age)
    def speak(self):
        return "Meow!"
    def likes_sleeping(self):
        return True
    def is_mammel(self):
        return True

cliffard = Dogs("Cliffard",3)
leo = Cats("Leo",2)

print("*"*50)
print(f"Name is {cliffard.name} , Age is {cliffard.age}")
print(f"Cliffard says {cliffard.speak()}")
print(f"Cliffard likes walks : {cliffard.likes_walks()}")
print(f"Cliffard is a Mammel : {cliffard.is_mammel()}")
print("*"*50)
print(f"Name is {leo.name} , Age is {leo.age}")
print(f"Leo says {leo.speak()}")
print(f"Leo likes sleeping : {leo.likes_sleeping()}")
print(f"Leo is a Mammel : {leo.is_mammel()}")
print("*"*50)