num = 3
if num > 0 :
    print('is ok')
else:
    print('is not ok')

num2 = 0
if num2 > 0 :
    print('is ok')
elif num2 < 0 :
    print('is okk')
else:
    print('is not ok')

num3 = 0
if num3 > 0 and num3 == 0:
    print('is ok')
elif num3 < 0 and num3 != 0:
    print('is okk')
else:
    print('is not ok')

num4 = 0
if num4 > 0 or num4 == 0:
    print('is ok')
elif num4 < 0 or num4 != 0:
    print('is okk')
else:
    print('is not ok')

age = input('Enter your age: ')
age = int(age)
if age > 18:
    print('is ok')
else:
    print('is not ok')

my_age = int(input('Enter your age: '))
your_age = int(input('Enter your age: '))
if my_age > your_age:
    print('my age is bigger')
elif your_age > my_age:
    print('your age is bigger')
elif my_age == your_age:
    print('we are the same age')

num5 = int(input('Enter number one:'))
num6 = int(input('Enter number two:'))
if num5 > num6:
    print('A')
elif num6 > num5:
    print('B')

num7 = int(input('输入分数'))
if num7 >80 and num7 <= 100:
    print('A')
elif num7 >60 and num7 <= 80:
    print('B')
elif num7 > 40 and num7 <= 60:
    print('C')
elif num7 > 20 and num7 <= 40:
    print('D')
elif num7 > 0 and num7 <= 20:
    print('E')
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits2 = ['banana', 'orange', 'mango', 'lemonc']
if fruits2 == fruits:
    print(fruits)

elif fruits2 != fruits:
   fruits2.extend(list(set(fruits).difference(set(fruits2))))
   print(fruits2)


    

