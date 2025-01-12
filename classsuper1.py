# create classes for our agents James Bond & Ethan Hunt
# create a super class that take nmae health and car 
# create a superclass metod that print off agent infomration.
# create a child class call spy, this inherits everything from the parent class
# add three additional parameters Agency, Location and killed (killed set to False)
# {Ethan Hunt will be bad guy}
# create a method to attack/assassinate the other agent, this take one parameter (on object)
# If the enemy's health is greater than 0, subtract 20 from health print off who has last 20 health and print off their updated health level
# if the enemy's health is less then or equal to 0, the killed property become true, print off {Enemy Name} is dead....
# create two instances of the spy class for James Bond and Etha Hunt
# call the method to print of agents information then weit 5 seconds while Ethan Hunt health greater than 0, both objects
# call assassinate method to attack.
# after every attack program should weit 2 seconds before the next. 
from time import *
class Agent():
    def __init__(self,name,health,car):
        self.name = name
        self.health = health
        self.car = car
    def agent_info(self):
        print("Welcome ", self.name)
        print("Health ", self.health)
        print("Car Choice ", self.car)
class Spy(Agent):
    def __init__(self, name, health, car, agency, location):
        super().__init__(name, health, car)
        self.agency = agency
        self.location = location
        self.killed = False
    def assassinate(self, bad_guy):
        if bad_guy.health > 0:
            bad_guy.health -= 20
            print(bad_guy.name, "has lossed 20 from their health...")
            print(bad_guy.name, "has health level ", bad_guy.health)
            if bad_guy.health == 0:
                self.killed = True
                print(bad_guy.name," is dead....", self.killed)
                
james_bond = Spy("James Bond",100,"Jaguar","MI6","London")
ethan_hunt = Spy("Ehtan Hunt",40,"Ferrari","FBI","New York")
james_bond.agent_info()
ethan_hunt.agent_info()
sleep(5)

while ethan_hunt.health > 0:
    james_bond.assassinate(ethan_hunt)
    ethan_hunt.assassinate(james_bond)
    sleep(2)