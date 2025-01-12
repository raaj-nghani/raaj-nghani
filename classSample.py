# create a class for animal with the parameter name, pet, sound.
# create a method called speak, print the sound of animal
# create a method called pet_info, print off the pet_info(propertie)
# create the object with different values
# call the method with your object

class Animal():
    def __init__(self, name, pet, sound):
        self.name = name
        self.pet = pet
        self.sound = sound
    
    def speak(self):
        print("Sound is ",self.sound)
    
    def pet_info(self):
        print("My ",self.pet," has the name ", self.pet, " making sound ", self.sound)

dog = Animal("Champ","Dog","Woof woof!")
cat = Animal("Tom","Cat","Meau!")

dog.speak()
cat.speak()

dog.pet_info()
cat.pet_info()
        
# We are wirking with NBA, we need a class called player.
# This class has three parameter, name, score and team.
# Team is initially set empty. Create a method called show_stats.
# This will print off the information about the player.
# Create a method called select_team this will ask for an input and set the value to team property
# Create an object for player. Call your methods. How can you show the updated player details
# after entering the team.
class Player():
    def __init__(self, name, score):
        self.name = name
        self.score = score
        self.team = None
    def show_stats(self):
        print("Player : ", self.name)
        print("Average Point : ", self.score)
        print("Team : ", self.team)
    def select_team(self):
        team = input("Enter your team name: ")
        self.team = team
player = Player("Raj","9")
player.show_stats()

player.select_team()
player.show_stats()

# We are building a class to find the perimeter and area of rectangle, what paarameter do we need to solve this?
# create a method to pring off basic information about the rectangle.
# create a method to calculate the perimeter(lenght + width) * 2 then return that value
# create a method to calculate the area (length * widht), then return the value.
# Create a method that wll shorten the length of rectangle, it will take one parameter and return the updated parameter.
# Gather the length and width through 2 inputs. Create an object giving the arguments we need.
# print off the basic infomation about the rectangle.
# print off the perimeter of the rectangle. print off the area of rectangle
# ask for an input to reduct the length of current rectangle.
# print off the updated rectangle perimeter.
class Rectangle():
    def __init__(self, length, width):
        self.length = length
        self.widht = width
    def print_info(self):
        print("Length: ", self.length)
        print("Width ", self.widht)
    def calc_perimeter(self):
        self.perimeter = (self.length + self.widht) * 2
        return self.perimeter
    def calc_area(self):
        self.area = self.length * self.widht
        return self.area
    def update(self, length):
        self.update = (self.length - length)* self.widht
        return self.update
l = int(input("Enter Length: "))
b = int(input("Enter Width "))

rect = Rectangle(l,b)
rect.print_info()
print("Perimeter ", rect.calc_perimeter())
print("Area : ", rect.calc_area())

c = int(input("Enter number to substract from length : "))
print("Updated area : ", rect.update(c))
