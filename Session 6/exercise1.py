'''
underweight = <18.5
normalweight = 18.5-24.9
overweight = 25-29.9
obesity = BMI of 30 or greater
'''
USA_BMI = 703 * (weight / height**2)
Metric_BMI = (weight / height**2)

while input == 'metric':
    height = float('Please enter your hight input meters(decimals): ')
    weight = int(input('Please enter your weight input kg: '))
    BMI = weight / (height*height)

if BMI < 18.5:
    print('Your BMI is', bmi, 'which means you are underweight.')
elif BMI > 18.5 and BMI < 24.9:
        print('Your BMI is', bmi, 'which means you are normal weight.')
elif BMI > 25 and BMI < 29.9:
        print('Your BMI is', bmi, 'which means you are overweight.')
elif BMI > 30:
    print('Your BMI is', bmi, 'which means you are obese.')
 else:
    print('There is an error with your input')
    print('Please check you have entered whole numbers\n'
              'and decimals were asked.')   

USA_BMI = 20
