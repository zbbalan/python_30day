print(type(float(10))) # <class 'float'>
print(len('helloword'))# 9
print(str(10))
print(min(20,30,40,50)) # 20 min内置函数取最小值
print(max(20,30,40,50)) # 50 max内置函数取最大值
print(sum([1,2,3,4,5])) # 15 sum内置函数求和

first_name, last_name, country, age, is_married = 'Asabeneh', 'Yetayeh', 'Helsink', 250, True
###多个变量可赋予多个值
print(first_name, last_name, country, age, is_married)
print('First name:', first_name)
print('Last name: ', last_name)
print('Country: ', country)
print('Age: ', age)
print('Married: ', is_married)

fast_age = input('why you so fast：')
print(type(fast_age))  ##所有通过input输入的都是字符串

init_Age = 20.1
print(int(init_Age))
print(type(int(init_Age)))
init_Age1 = '21'
print(int(init_Age1))
print(type(int(init_Age1)))
init_Age2 = 'helloword'
print(list(init_Age2))
print(type(list(init_Age2)))
init_Age3 = 22
print(float(init_Age3))
print(type(float(init_Age3)))
print(str(init_Age3))
print(type(str(init_Age3)))
