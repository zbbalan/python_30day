num3 = 0

while num3 < 10:
    print(num3)
    num3+=1

num4 = 1    
while num4 < 5:
    num4+=1
else:
    print(num4)

num1 = 0
while num1 <10:
    print('is',num1)
    num1+=1
    if num1 == 5:
        break   ###break 满足添加就退出

num2 =0  
while num2 < 10:
    if num2 == 5:
        num2 +=1
        continue  ###continue 满足添加就跳过
    print('this is',num2)
    num2 += 1

numbers = [0, 1, 2, 3, 4, 5]
for number in numbers:
    print(number) 

language = 'Python'
for letter in language:
    print(letter)
for i in range(len(language)):
    print(language[i])


person = {
    'first_name':'Asabeneh',
    'last_name':'Yetayeh',
    'age':250,
    'country':'Finland',
    'is_marred':True,
    'skills':['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address':{
        'street':'Space street',
        'zipcode':'02210'
    }
}

for key in person:
    print(key)
for key,value in person.items():
    print(key,value)
#range 范围
Au_num1 = list(range(11))
print(Au_num1) ##输出
for iterator in range(0, 11, 2):   ###范围（start、end、step）有三个参数 开始，结束，步长
    print(iterator)

person1 = {
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_marred': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
}
for key in person1:
    if key == 'address':
        for address in person1[key]:
            print(address)

for number in range(11):   
    print(number)
else:    ###如果我们想在循环结束时执行一些消息，我们使用else。
     print('The loop stops at', number)

###练习
num11 = list(range(0, 11))
for i in num11:
    print(i)
A = 0
while A<8:
    print('#' * A)
    A+=1

for i in range(7):
    for a in range(7):
        print('#', end='')
    print()

for i in range(0,7):
    for c in range(0,7):
        d = i * c
        print(i, 'x', c, '=', d)
    print()
for i in range(0,7):
    alan = i * i
    print(f"{i} x {i} = {alan}")

tabley =  ['Python', 'Numpy','Pandas','Django', 'Flask']

for i in tabley:
    print(i)

for i in range(0,100):
    if i % 2 == 0:
        print(i)
for i in range(0,100):
    if i % 2 != 0:
        print(i)
while i in range(0,100):
     i += A
     print(i + A)
     i+=1
sum = 0
for i in range(0,101):
    sum += i
print(sum)
sum = 0
sum1 = 0
for i in range(0,101):
    if i %2 == 0:
        sum+=i
    else:
        sum1+=i
print(sum)
print(sum1)
    

        

