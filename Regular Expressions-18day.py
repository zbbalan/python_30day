import re
txt = "The rain in Spain hello python and java for a first programming language"
match = re.search('python',txt,re.I)  ### re.I 忽略大小写 <re.Match object; span=(24, 30), match='python'>
print(match)
span=match.span()  ###查找返回index
print(span) ### (24, 30)
matchs=re.findall('python',txt,re.I)  ###findall 查找返回列表
print(matchs) ### ['python']
Matchs=re.sub('python','javascript',txt,re.I)    ##sub 替换
print(Matchs)### The rain in Spain hello javascript and java for a first programming language
txt2 = '''%I a%m te%%a%%che%r% a%n%d %% I l%o%ve te%ach%ing. 
T%he%re i%s n%o%th%ing as r%ewarding a%s e%duc%at%i%ng a%n%d e%m%p%ow%er%ing p%e%o%ple.
I fo%und te%a%ching m%ore i%n%t%er%%es%ting t%h%an any other %jobs. 
D%o%es thi%s m%ot%iv%a%te %y%o%u to b%e a t%e%a%cher?'''
match2=re.sub('%',' ',txt2)
print(match2)

