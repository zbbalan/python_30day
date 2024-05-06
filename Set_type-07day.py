st = {'item1', 'item2', 'item3', 'item4'}
fruits = {'banana', 'orange', 'mango', 'lemon'}
print(len(st), len(fruits))
print('item1' in st)  ##True
st.add('item5')  ###使用add添加元素
print(sorted(st))
st.update(['item6', 'item7', 'item8'])  ###使用update添加元素可添加list
print(st)
fruits2 = ('tomato', 'potato', 'cabbage', 'onion', 'carrot')
fruits.update(fruits2)
print(fruits)
fruits.remove('mango')
print(fruits)
# fruits.remove('mango')
# print(fruits)  ###使用remove删除元素，必须是存在在集合里的，否则删除错误
fruits.discard('mango')
print(fruits)  ###使用discard删除元素，key不存在不会报错
str1 = {'item1', 'item2', 'item3', 'item4'}
str2 = {'item1', 'item2'}
str3 = str1.difference(str2)  ##检查两个集合的差值
print(str3)
str3 = str1.intersection(str2)  ##检查两个集合的交集
print(str3)
print(str1.isdisjoint(str2))  ##检查两个集合是否没有交集 有返回true没有返回false
print(str1.issuperset(str2))  ##检查str1是否包含str2

###练习
num1 = {'AAA', 'BBB', 'CCC', 'DDD', 'EEE', 'FFF', 'GGG', 'HHH', 'III', 'JJJ', 'KKK', 'LLL', 'MMM', 'NNN', 'OOO', 'PPP',
        'QQQ', 'RRR', 'SSS', 'TTT', 'UUU', 'VVV', 'WWW', 'XXX', 'YYY', 'ZZZ', 'asadasda'}
print(len(num1))
num1.add('Twitter')
print(num1)
num2 = {'AAA', 'BBB', 'CCC', 'DDD', 'EEE', 'FFF', 'GGG', 'HHH', 'III', 'JJJ', 'KKK', 'LLL', 'MMM', 'NNN', 'OOO', 'PPP',
        'QQQ', 'RRR', 'SSS', 'TTT', 'UUU', 'VVV', 'WWW', 'XXX', 'YYY', 'ZZZ', '12121212'}
num3 = num1.union(num2)
print(num3)
num3.remove('AAA')
print(num3)
print(num1.intersection(num2))
print(num2.intersection(num1))
print(num1.isdisjoint(num2))
print(num1.difference(num2))
print(num1.symmetric_difference(num2))
