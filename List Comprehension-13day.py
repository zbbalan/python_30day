#如果你想把一个字符串变成一个字符列表。你可以使用几种方法
langger = 'Python'
print(list(langger))

##示例1
lst = [i for i in langger]
print(lst)

##示例2
#如果你想生成一个数字列表，
nubers = [ i for i in range(10)] 
print (nubers)
##也可以制作一个元组列表
numbers = [(i,i *i) for i in range(10) ]
print(numbers)

###列表解析可以与if表达式结合使用
events = [i for i in range(10) if i % 2 ==0 ]
print(events) ##生成0 --10  的偶数列

evens = [ i for i in range(10) if i %2 != 0]
print(evens) ##生成0 --10  的奇数列
