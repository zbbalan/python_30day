tpl = ('item1', 'item2','item3')
fruits = ('banana', 'orange', 'mango', 'lemon')
print(len(tpl))
print(len(fruits))
all_items = tpl[0:2]
print(all_items)  # ('item1', 'item2') 正指数范围
print(tpl[-2:]) # ('item3',) 负数范围
 #我们可以把元组变成列表，也可以把列表变成元组。元组是不可变的，如果我们想修改一个元组，我们应该把它变成一个列表。
tpl2 = ('item1', 'item2', 'item3','item4')
lst = list(tpl2)
print(lst) 
lst[0] = 'apple'
print(lst) 
#我们可以使用in检查一个元组中是否存在一个元素，它返回一个布尔值。
print('apple' in lst) #True
tpl3 = tpl2 + tpl
print(tpl3)
#不可能删除元组中的单个项，但可以使用del删除元组本身。
del tpl3
