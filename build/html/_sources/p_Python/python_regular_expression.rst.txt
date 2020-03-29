=============================
Python正则表达式
=============================

内置模块re

坐井观天：本节知识点

理解正则表达式的概念
re模块

管中窥豹：延伸阅读
雨痕 《Python学习笔记》

正则表达式（Regular Expression）使用单个字符串来描述、匹配一系列符合某个句法规则的字符串。在很多文本编辑器里，正则表达式通常被用来检索、替换那些符合某个模式的文本。

正则表达式中特殊符号的作用
.^$*+?{}[]\|()


import re
dir(re)
re模块中的函数
re.compile # 生成一个匹配器实例，用来匹配，不用重复编译，优化代码执行时间
re.findall # 找到全部匹配字符串，以列表返回
re.finditer # 找到全部匹配实例对象，以迭代器返回
re.match # 匹配字符串开始位置
re.search # 扫描字符串，找到第一个位置
re.split # 根据规则切分字符串
re.sub # 查询替换字符串，返回替换结果
re.subn # 查询替换字符串，返回替换结果和替换次数


re.match、re.search、re.finditer返回匹配结果的实例对象，实例对象有如下方法
instance.group() # 返回匹配的完整字符串
instance.start() # 匹配的开始位置
instance.end() # 匹配的结束位置
instance.span() # 包含起始、结束位置的元组
instance.groups() # 返回分组信息
instance.groupdict() # 返回命名分组信息

import re

s = "12abc345ab"
m = re.match(r"\d+", s)
print(dir(m))
print(m.group())
print(m.span()) # 返回index

m = re.match(r"\d{3,}", s)
print(m is None)
m = re.search(r"\d{3,}", s)
print(m.group())
print(m.span())

m = re.search(r"\d+", s)
print(m.group())
print(m.span())

ms = re.findall(r"\d+", s)
print(ms)
ms = re.findall(r"\d{5}", s)
print(ms)

for m in re.finditer(r"\d+", s):
    print(m.group())
    print(m.span())

for m in re.finditer(r"\d{5}", s):
    print(m.group())
    print(m.span())

m = re.match(r"(\d+)(?P<letter>[abc]+)", s)
print(m.group())
print(m.start())
print(m.end())
print(m.span())
print(m.groups())
print(m.groupdict())
print(m.group(0))
print(m.group(1))
print(m.group(2))
print(m.group(1, 2))
print(m.group(0, 1, 2))
print(m.start(0), m.end(0))
print(m.start(1), m.end(1))
print(m.start(2), m.end(2))
print(m.span(0))
print(m.span(1))
print(m.span(2))

res = re.search("ch_", "proj_ch_dog")
res = re.search("d[aoes]g", "dog dag deg dsg")
res = re.search("d[a-zA-Z0-9]g", "dog dag deg dsg")

# \d 数字 [0-9]
# \w 字母或数字 a-z A-Z 0-9 _
# \s 空白字符 space
# \D \W \S 与小写相反
# . 任意字符
# | 或
# ^ 非，或者开始位置标记
# $ 结束位置标记
# \b 单词边界
# \B 非单词边界
匹配变长的字符
# ? 表示 0 - 1次 ab?c匹配abc或者ac
# + 表示1 - 无数次 ab+c匹配abc abbc abbbbbbc
# * 表示0 - 无数次 ab*c匹配ac abc abbbbbbc
# {m, n} 表示匹配m到n次 ab{2, 5}c匹配abbbc abbbbbbbc
# {m} 表示只匹配m次
# {m,} 表示匹配最少m次 
# {, n} 表示匹配最多n次 
res = re.search(r"a\wt", "adfaa_tfagdga")
res = re.search("1[357]\d{9}", "phone number: 13851709904")

# ()表达式编组，括号里面的表达式作为一个整体逻辑

res = re.search("SSNI-\d{3}\.avi", "this is budsfaf SSNI-518.avi dfaganiojfoas")
if res:
    print(res.group(), res.start(), res.end())
else:
    print("Not found!")

res = re.findall("[a-zA-Z]+\.html", sss)

(?P<name>)
(?=name)
(mov|exr)

match = re.search("(?P<id>\d+), Date: (?P<date>.+)", "ID: 021523, Date: Feb/12/2017")
print(match.group("id"))
print(match.group("date"))

res = re.search("\w+(?=.jpg)", "image.jpg")

(?=abc) 判断字符后面包含abc
(?!abc) 判断字符后面不包含abc
(?<=abc) 判断字符前面包含abc
(?<!abc) 判断字符前面不包含abc
(?#...) 注释

re.split(r"\W", "abc,123,x")
re.split(r"(\W)", "abc,123,x")
re.sub(r"[a-z]+", "abc,123,x")
re.sub(r"[a-z]+", "abc,123,x", 1)
re.subn(r"[a-z]+", "*", "abc,123,x")


编译标志(?iLmsux)
可以用re.I、re.M等参数，也可以直接在表达式中添加(?)

s	单行
i	忽略大小写
L	让\w匹配本地字符，对中文支持不好
m	多行
x	忽略多余的空白字符
u	unicode

(?i)忽略大小写

组操作，小括号即组，分组的概念
import re

s1 = “%123Abc%45xyz&”
re.findall(r”(\d+)(\w+)”, s1)
re.findall(r”(\d+(\w+))”, s1)

命名组 (?P<name>...)

for m in re.finditer(r”(?P<number>\d+)(?P<letter>[a-z]+)”, “%123Abc%45xyz&”, re.I):
    print(m.group())
    print(m.groupdict())

无捕获组(?:...)，作为匹配条件，匹配的对象在无名的组中，无需关心
import re

s1 = “%123Abc%45xyz&”
print(re.findall(r”(?:\d+)([a-z]+)”, s1))
print(re.findall(r”(?:\d+)([a-z]+)”, s1, re.I))


反向引用
\<number>或(?P=name)，引用前面的组
for m in re.finditer(r”<a>\w+</a>”, “%<a>123Abc</a>%<b>45xyz</b>&”):
    print(m.group())

for m in re.finditer(r”<\w>\w+</(\1)>”, “%<a>123Abc</a>%<b>45xyz</b>&”):
    print(m.group())

for m in re.finditer(r”<(?P<tag>\w)>\w+</(?P=tag)>”, “%<a>123Abc</a>%<b>45xyz</b>&”):
    print(m.group())

(?=...) # 组内容必须出现在右侧
(?!...) # 组内容不能出现在右侧
(?<=...) # 组内容必须出现在左侧
(?<!...) # 组内容不能出现在左侧


re.split用pattern做分隔符切割字符串，如果用(pattern)，分隔符也会返回
import re

s1 = “abc,123,x”
print(re.split(r”\W”, s1))
print(re.split(r”(\W)”, s1))


re.sub 替换查找到的字符串，返回新的字符串，可指定替换次数
import re

s1 = “abc,123,x”
print(re.sub(r”[a-z]+”, “*”, s1))
print(re.sub(r”[a-z]+”, “*”, s1, 1))

re.subn和re.sub用法一样，只是返回值不同，返回(新的字符串，被替换的次数)
import re

s1 = “abc,123,x”
print(re.subn(r”[a-z]+”, “*”, “abc,123,x”))
print(re.subn(r”[a-z]+”, “*”, “abc,123,x”, 1))

用来替换的参数repl可以接受自定义函数
import re

def repl(m):
    print(m.group())
    return “*” * len(m.group())

s1 = “abc,123,x”
print(re.sub(r”[a-z]+”, repl, s1))
print(re.sub(r”[a-z]+”, repl, s1, 1))
print(re.subn(r”[a-z]+”, repl, s1))
print(re.subn(r”[a-z]+”, repl, s1, 1))

结合匿名函数lambda可以更简洁
import re
s1 = “abc,123,x”
print(re.sub(r”[a-z]+”, lambda x: “*” * len(x.group()), s1))

import re
s1 = “magicFireNezhaSpirit”
re.sub(r”[A-Z]+”, lambda x: “_” + x.group().lower(), s1)

辅助组