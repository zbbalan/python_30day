fruits = ['banana', 'orange', 'mango', 'lemon'] 
print(len(fruits)) #具有初始值的列表可以使用len()函数来获取长度
print(fruits[1]) #orange 正确使用索引获取列表中的元素
vegetables = ['Tomato', 'Potato', 'Cabbage','Onion', 'Carrot']    
animal_products = ['milk', 'meat', 'butter', 'yoghurt']            
web_techs = ['HTML', 'CSS', 'JS', 'React','Redux', 'Node', 'MongDB'] 
countries = ['Finland', 'Estonia', 'Denmark', 'Sweden', 'Norway']
lst = ['Asabeneh', 250, True, {'country':'Finland', 'city':'Helsinki'}] #列表可以包含不同数据类型的项
first_fruit, second_fruit, third_fruit, *rest = fruits
print(first_fruit)
print(second_fruit)
print(third_fruit)
print(rest)
#列表是一个可变的或可修改的有序项集合
fruits[0] = 'avocado'
print(fruits) #['avocado', 'orange', 'mango', 'lemon']
A_fruit = 'mango' in fruits
print(A_fruit) #True
fruits.append('apple')
lst = ['apple','aaaa']
lst.insert(2,'bbbb')
print(lst)  ##['apple', 'aaaa', 'bbbb'] inset插入
lst.remove('bbbb')
print(lst)  ##remove移除
lst.pop(1) #pop移除
print(lst)
del lst[0]
print(lst)  ##del删除
fruits_copy = fruits.copy()
print(fruits_copy)  ##copy复制
num1 = [1,2,3,4,5]
num2 = [6,7,8,1,10]
num3 = num1 + num2
print(num3)
num1.extend(num2) #extend合并
print(num1)
print(num1.count(1)) #count统计 1出现的次数
print(num1.index(6)) #index查找输出索引


##练习
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
ages.sort()
print(ages)
ages += ages[0],ages[-1]
ages.sort()
print(ages)
ages1 = ages[0]
ages2 = ages[-1]
print(ages1 + ages2 / 2)
new_ages = set(ages)
print(new_ages)
print(sum(new_ages)/len(new_ages))

