def amount_calc(price, qty):
    amount = price * qty
    return amount

print('----- Prorame 1 -----')
price = float(input('Enter price: '))
quantity = int(input("Enter Quantity: "))
amt = amount_calc(price, quantity)
print(amt)

def deal(cost):
    if cost >= 50 and cost <150:
        responce = "This is a good deal!"
    elif cost >=150:
        responce = "Overpriced"
    else:
        responce = "Cheap, Byu now!"        
    return responce
print('----- Prorame 2 -----')
cost = int(input('Enter Cost: '))
res = deal(cost)
if res == "This is a good deal!":
    print("Buy tis before it's too late")    

def person_info(name, ae, nationality):
    print('Welcome: ', name)
    print('You are: ', ae )
    print('You are: ', nationality)

print('----- Prorame 3 -----')    
number = int(input("Count: "))
for i in range(number):
    name = input("Enter Name: ").capitalize()
    ae = input("Enter your ae: ")
    nationality = input("Enter your nationality: ").capitalize()  
    person_info(name, ae, nationality)  

print('----- Prorame 4 -----')        
def total_point(score):
    points = 0
    while score != 0:
        if score >= 5 and score <= 10:
            points += 2
        if score > 10 and score <= 20:
            points += 3
        score = int(input('Enter the game Score: '))
    return points    
score = int(input('Enter the game Score: '))
game_points = total_point(score)
print('Total Points: ', game_points)                 
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    