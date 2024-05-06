mystrings = """hello world"""
print(mystrings)
#在Python中，字符串可以包含任何字符，包括空格、制表符、换行符等。
#多重行字符串可以使用三个双引号或三个单引号来表示。
one_name = 'the'
two_name = "is"
san_name = 'python'
full_name = one_name + two_name + san_name
print(full_name)
print(len(full_name))

print('look at %s %s %s'%(one_name,two_name,san_name))
#%s -字符串（或任何具有字符串表示的对象，如数字）
python_libraries = ['Django', 'Flask', 'NumPy', 'Matplotlib','Pandas']
formated_string = 'The following are python libraries:%s' %(python_libraries)
print(formated_string)

last_string = 'hello,python'
print(len(last_string))
print(last_string[-1]) #倒数第一个字符n
print(last_string[0]) #第一个字符h
print(last_string[0:2]) #he
print(last_string[0:]) #hello,python
print(last_string[::-1]) #[:: -1] 反转字符串
print(last_string.count('o')) ## count统计字符串中o出现的次数