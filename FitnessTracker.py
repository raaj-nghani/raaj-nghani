name = input('Enter Your Name: ')
weight = int(input('Enter Weight (in Kg.)'))
height = float(input('Enter height (in Mtr.)'))
bmi = weight / (height**2)
if bmi<18.5:
    status = 'Under Weight'
elif (bmi>18.5 and bmi < 24.9):
    status = 'Normal Weight'
elif(bmi>24.9 and bmi<29.9):
    status = 'Over Weight'
else:
    status = 'Obese'          
              
print('Hi', name, ', Your BMI is:', bmi, ', and you are',status)