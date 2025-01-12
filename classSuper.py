# Create Animal class.
# Create a chile class called Fish
# create a method called Swim, if the sound is equal to None, print 'I am a fish, I do not have sound.' other wise print 'are you shure you are a fish?'
# create a second method called ocean, ask the fish which ocean they are from print off
# example Neau is the fish who lives in Pecific Ocean.
# create an object and call all four methods

class Animal():
    def __init__(self, name, pet, sound):
        self.name = name
        self.pet = pet
        self.sound = sound
    def speak(self):
        print(self.sound)
    def pet_info(self):
        print("My ", self.pet,", the name of ", self.name," and they make sound ", self.sound)
class Fish(Animal):
    def swim(self):
        if self.sound == None:
            print("You are a fish...")
        else:
            print("You must not a fish...")
    def ocean(self):
        region = input("Enter an ocean: ")
        print(self.name, " is a ", self.pet," who lives in ", region, "Ocean.")
        
nemo = Fish("Nemo","Fish",None)
nemo.speak()
nemo.pet_info()

nemo.swim()
nemo.ocean()

# We need a super class for vehicles. our constructor needs any car basic info: make, mode, price, year.
# Create a method to check if the name is 'Chevy' or 'Tesla' print 'Americal Made' else print 'Imported'
# Create a method that returns the vehicle model.
# Create a method that check if the car made year is greather than 2000 return '21st Century Car' other wise "Old Car"
# Create a method that accepts a new_price you are willing to pay. This method check if the car price is under your budget
# if yes return 'Within your budget' otherwise return 'Over budget'
# Create a child class for style. This class accept super class and slos has a parameter of its own for num_door
# Create a method if num_door is four return 'Family car' other wise return 'Sports Car'
# Create three objects 1- object using super class, call two methods. 
# The 2 other objects using the child class call, 3 or more method use the clild method and get_price method

class Superclass():
    def __init__(self, make, model, year, price):
        self.make = make
        self.model = model
        self.year = year
        self.price = price
    def get_make(self):
        if self.make =='Ford' or self.make =='Tesla' or self.make =='Chevy':
            return 'Americal Model'
        else:
            return 'Imported...'
    def get_model(self):
        return self.model
    
    def get_year(self):
        if self.year >=2000:
            return "21st Century Car"
        else:
            return "Old model car..."
    def get_price(self,maxprice):
        if self.price > maxprice:
            return "Good Bye, within your budget..."
        else:
            return "Over budget..."
class Style(Superclass):
    def __init__(self, make, model, year, price, num_door):
        super().__init__(make, model, year, price)
        self.num_door = num_door
    def get_door(self):
        if self.num_door == 4:
            return "Family Car"
        elif self.num_door == 2:
            return "Sports Car"
        else:
            return "Other category..."
truck = Superclass("Ford","Baleno",2010,9000)
print(truck.get_make())
print(truck.get_price(1500))

car = Style("Chevy","Classic",2001,9000,4)
print(car.get_door)

sportscar = Style("Lamborgini","Adventure",2022,35000,2)
print(sportscar.get_make())
print(sportscar.get_price(400000))
print(sportscar.get_make())

