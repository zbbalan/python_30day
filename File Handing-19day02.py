###删除文件
import os
import json
import csv
import xlrd
import xml.etree.ElementTree as ET
if os.path.exists('test.txt'):
    os.remove('test.txt')
else:
    print('文件不存在')
###将j'son数据转换为python字典
person_json = '''{
    "name": "Asabeneh",
    "country": "Finland",
    "city": "Helsinki",
    "skills": ["JavaScrip", "React", "Python"]
}'''
person_json = json.loads(person_json)
print(person_json)
print(person_json['name'])

person_json_class =json.dumps(person_json,indent=1)  ###indent=1表示缩进
print(person_json_class)

with open('./files/hello.json','w',encoding='utf-8') as f:
    json.dump(person_json,f,ensure_ascii=False, indent=4)


'''with open('./files/csv_example.csv','w') as f:
    csv_reader = csv.reader(f, delimiter=',') # w use, reader method to read csv
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'Column names are :{", ".join(row)}')
            line_count += 1
        else:
            print(
                f'\t{row[0]} is a teachers. He lives in {row[1]}, {row[2]}.')
            line_count += 1
    print(f'Number of lines:  {line_count}')'''
try:
    excel_book = xlrd.open_workbook('./files/sample.xls','rb')
    print(excel_book.nsheets)   ##获取工作表数量
    print(excel_book.sheet_names())  ##获取工作表名称
except FileNotFoundError:
    print('文件不存在')
except xlrd.XLRDError:
    print('文件格式错误')
except Exception as e:
    print(f"未知错误: {str(e)}")

tree = ET.parse('./files/xml_example.xml')
root = tree.getroot()
print('Root tag:', root.tag)
print('Attribute:', root.attrib)
for child in root:
    print('field: ', child.tag)