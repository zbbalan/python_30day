f = open('./files/reading_file_example.txt')
print(f)
txt=f.read()
print(type(txt))
#print(txt)
#f.close()
f.seek(0) # 重置文件指针到文件开始位置
line=f.read(10)  ##打印前10个字符
print(line)
print(type(line))
#f.close()
f.seek(0)   
line1=f.readline()
print(line1) ###打印第一行
f.seek(0)
line2=f.readlines()   ##逐行读取并返回列表
print(line2)
#f.close()
f.seek(0)
line3=f.read().splitlines()    ###逐行读取并返回列表
print(line3)

with open('./files/reading_file_example.txt') as f:
    line4=f.readline()
try:
    with open('./files/reading_file_example.txt','a') as f:    ###a追加 append
        line5=f.write('hello world')
        line6=f.readlines()
        print(line6)
except IOError as e:
    print(f"文件操作失败:{e}")
except Exception as e:
    print(f"未知错误:{e}")

with open('./files/hello.txt', 'w') as f:   ####w如果不存在则创建
    f.write('hello world')