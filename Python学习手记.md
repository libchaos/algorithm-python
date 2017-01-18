## 如何在列表，字典，集合中根据条件筛选数据


- 过滤掉列表
- 筛选字典
- 筛选集合


```
res = []
for i in data:
    if condition:
        res.append(i)
        
#列表解析 vs 函数式
from random import randint

data = [randint(-10, 10) for _ in xrange(10)]

filter?
timeit filter(lambda x: x>=0, data)

timeit [i for i in data if i >=0]


d = {x: randint(60, 100) for x in xranage(1, 20) }

#根据值过滤
{k : v for k, v in d.iteritems() if v > 90}

s = set(data)
{x for x in s if x% 3 ==0}

```


## 如何为元组中的每个元素命名，提高程序的可读性

```
student = ("li", 20, "male", "lic@qq.com")

#name
NAME = 0
student[NAME]
#age
AGE = 1
student[AGE]
#mail
...

from collections import nametuple
Student = nametuple('Student', ['name', 'age', 'sex', 'email'])

s = Student("li", 20, "male", "lic@qq.com)
s2 = Student(name="lib", age="23")

s2.name
s.name
s.age
s.male

```

## 序列中元素出现的频度


```
from random import randint
data = [randint(10, 20) for i in xrange(30)]
c = dict.fromkeys(data, 0)
for x in data:
    c[x] += 1
    
from collections import Councter
c2 = Counter(data)
c2[10]
c2.most_common(3)
#词频统计

import re
txt = open('CodingStyle').read()
txt = re.split('\W+', txt)
c3 = Counter(txt)
c3.most_common(10)
```

## 根据字典值的大小进行排序

- 解决方案
sorted

```
sorted([3, 1, 1])
from random import randint
d = {x: randint(60:100) for x in 'xyzabc'}
sorted(d) # 按键排序
list(iter(d)) 
d.keys()
d.values()
zip(d.itervalues(), d.iterkeys())
sorted(_)

d.items()
sorted(d.items(), keys=lambda x: x[1])

```

## 多个字典中的公共键

第一轮
{a: 1}{a: 2}{b: 2}
```

from random import randint, sample
sample1 = sample('abcdefg', randint(3, 6))

s1 = {x: randint(1, 4) for x in sample1}
s2 = {x: randint(1, 4) for x in sample1}
s3 = {x: randint(1, 4) for x in sample1}
# viewskeys
s1.viewkeys()&s2.viewkeys()&s3.viewkeys()

N轮呢？

map reduce
Map1 = map(dict.viewkeys, [s1, s2, s3])
reduce(lambda a, b: a&b, Map1)
```

## 字典有序
```
d = {}
d['Jim'] = (1, 35)
d['Leo'] = (2, 37)
d['sunny'] = (3, 39)
for k in d: print k
from collections import OrderedDict
d = OrderedDict()

from time import time

from random import randint
from collections import OrderedDict
d = OrderedDict()
players = list('ABCDEFG')
from time import time
start = time()

for i in xrange(8):
    raw_input()
    p = players.pop(randint(0, 7-i))
    end =time()
    print i+1, p, end-start,
    d[p] = (i+1, end-start)

print 
print '_' * 20
for k, v in d:
    print k, v
```



## 如何实现用户的历史记录功能


```
from random import randint
N = randint(0, 100)
history = deque([], 5)
def guess(K)：
    
    if K == N:
        print 'right'
        return True
    elif K < N:
        print 'less'
    else:
        print 'larger'
    return False

while True:
    line = raw_input("number K: ")
    if line.isdigit():
        k = int(line)
        history.append(k)
        if guess(k):
            break
        elif line = 'history' or line= 'h?':
        print list(history)
from collections import deque
q = deque([], 5)
q.append(1)

import pickle
q 
pickle.dump(q, open('histroy', w))
pickle.load(open('history'))


```

##  如何实现可迭代对象和迭代器对象

```
l = [1, 2, 3, 4]
s = 'abcde'
for x in l:
    print x
for x in s:
    print x
iter(l)
iter(s)
iter(5)

```

```
#coding: utf-8
import requests
from collections import Iterable, Iterator


class WeatherIterator(Iterator):

    def __init__(self, cities):
        self.cities = cities
        self.index = 0

    def getWether(self, city):
        r = requests.get(u'http://wthrcdn.etouch.cn/weather_mini?city=' + city)
  
        data = r.json()['data']['forecast'][0]

        result =  "%s, %s, %s" % (city,data['low'], data['high'])
        return result

    def next(self):
        if self.index == len(self.cities):
            raise StopIteration
        
        city = self.cities[self.index]

        self.index += 1

        return self.getWether(city)


class WeatherIterable(Iterable):

    def __init__(self, cities):
        self.cities = cities
    
    def __iter__(self):
        return WeatherIterator(self.cities)



for x in WeatherIterable([u"北京", u"上海"]):
    print x
```



### 利用生成器函数
```
def f():
    print "in f(), 1"
    yield 1

    print "2"
    yield 2
    print "3"
    yield 3


g = f()
g.next()
g.next()

for x in g:
    print x

g.__iter__() is g



class PrimeNumbers():

    def __init__(self, start, end):
        self.start = start
        self.end = end
    
    def isPrimeNum(self, k):
        if k < 2:
            return False
        for i in xrange(2, k):
            if k % i ==0:
                return False
        return True
    
    def __iter__(self):
        for k in xrange(self.start, self.end+1):
            if self.isPrimeNum(k):
                yield k


for x in PrimeNumbers(1, 100):
    print x
```


## 如何反向迭代

```

l = [1, 2, 3, 4, 5]
#l.reverse()

#l[::-1]

reversed(l)#反向迭代器
iter(l)#正向迭代器

class FloatRange:

    def __init__(self, start, end, step=0.1):
        self.start = start
        self.end = end
        self.step = step
    
    def __iter__(self):
        t = self.start
        while t <= self.end:
            yield t
            t += self.step
    
    def __reversed__(self):
        t = self.end
        while t >= self.start:
            yield t
            t -= self.step
    

FloatRange(1.0, 4.0, 0.5)
```


## 迭代器切片

```
from itertools import islice
f = open('text.txt')
islice(f, 100, 300)
```
**重新申请isclice对象**




## 如何在一个for语句中迭代多个可迭代对象
**并行**
```
#并行
from random import randint
math = [randint(60, 100) for _ in xrange(40)]
en = [randint(60, 100) for _ in xrange(40)]
ch = [randint(60, 100) for _ in xrange(40)]
for i in xrange(len(math)):
    ch[i] + math[i] +en[i]

# 生成器则不能用上述操作

zip([1, 2, 3, 5], ('a', 'b', 'c', 'd'), [7, 8, 9, 10])

#长度不一，取较短

total = []
for m, e, c in zip(math, en, ch):
    total.append(m + e +c)
```
**串行**
```
from itertools import chain
#串行

c1 = [randint(60, 100) for _ in xrange(40)]
c2 = [randint(60, 100) for _ in xrange(40)]
c3 = [randint(60, 100) for _ in xrange(40)]


count = 0

for s in chain(c1, c2, c3):
    if s > 90:
        count += 1

for x in chain([1, 2, 3, 4], ['a', 'b', 'c']):
    print x
```


## 如何拆分含有多种分隔符的字符串

 法1
```
#str.split()
s = "a;cd: fes,,sfdsaf | fsfsa\sfsa"
t = []
res = s.split(';')
map(lambda x: t.extend(x.split('|')), res)

res = t
t = []
map(lambda x: t.extend(x.split('\t')), res)



def mySplit(s, ds):
    res = [s]
    for d in ds:
        t = []
        map(lambda x: t.extend(x.split(d)), res)
        res = t
    #去空字符串
    return [for x in res if x] 
```

法2

```
import re

re.split?

re.split(r'[,;\t|]+', s)
```
## 字符开头结尾

```
import os, stat
os.listdir('.')
#['e.py', 'g.sh', 'a.java']
s = 'g.sh'
s.endswith('.sh')
s.endswith(('.sh', '.py')) #True

[x for name in os.listdir('.') if name.endswith(('.sh', '.py'))]
otc(os.stat('e.py').st_mode)

stat.S_IXUSER
os.chmod('e.py', os.stat('e.py').st_mode | stat.S_IXUSER)

```

## 如何调整字符串中文本的格式
```
log = open('/var/log/dpkg.log').read()

import re

re.sub('(?P<year>\d{4})-(?P<month>\d{2})-(?P<day>\d{2})', r'\2/\3/\1', log)

                                                     r'\g<month>/\g<day>/\g<year>'
```


## 字符串拼接
*浪费内存法*
```
s1 = "aba"
s2 = "fds"
s1 + s2
str.__add__
str.__add__(s1, s2)
s1 >　s2
pl = ['a', 'b', 'c']
s = ''
for p in pl:
    s += p
s

```
*str.join()*

```
';'.join(['abc', '123', 'xyz'])
```

*生成器表达式()*
```
''.join((str(x) for x in l))

```

#如何对字符串进行左中右对其

```
s = 'abc'
s.ljust?
s.ljust(20)
s.ljust(20, '=')
s.rjust(20)
s.rjust(20, '-')
s.center(20, '-')

#内置的format方法

format(s, '<20')
format(20, '>20')
format(s, '^20')


d = {'sfasf': 1, 'a': 2324}

d.keys()
w = max(map(len, d.keys()))
for k in d:
    print k.ljust(w), ":", d[k]

```

## 如何去掉字符串中不需要的字符

```
s = ' 2asfds sfs'
s.strip()
s.lstrip()
s.rstrip()
s = '---abac+++'
s.strip('-+')
s = 'abc:123'
s[:3] + s[4:] # 去掉：
s = '\tabc\t1231'
s.replace('\t', '')
s = '   \tsfdsa\r\sfdsf\t'
re.sub('[\t\r]', '', s)

str.translate?

unicode.translate?

s = 'abc1230323xyz'
import string
string.maketrans('abcxyz', 'xyzabc')
s.translate(string.maketrans('abcxyz', 'xyzabc'))
s = 'abc\regf\ndfa\t'
s.translate(None, '\r\t\n')
u.translate({0x0301: None})

```

##python2 和python3中文本文件的读写

```
s = u'你好'
s.encode('utf8')



open('py2.txt', 'w')
s = u'你好'
f.write(s.encode('utf8'))
f.close()
f = open('py2.txt', 'r')
t = f.read()
t  '\sxc'
t.decode('utf8')

#python3

open('py3.txt', 'wt', encoding='utf8')
f.write('你好，。。。')
f.close()
f = open('py3.txt', 'rt', encoding='utf8')
s = f.read()

print(s)
```
## 解析2进制数据
```
f = open('demo.wav', 'rb')
info = f.read(44)
info
import struct

struct.unpack('h', info[22, 24])
struct.unpack('i', info[24, 28])

import array

array.array('h', )
f.seek(0, 2)
f.tell()
n = (f.tell() - 44) / 2
buf = array('h', (0 for _ in xrange(n)))
f.seek(44)
f.readinto(buf)
buf[5]
buf[10]
for i in xrange(n):
    buf[i] /= 8

f2 = open('demo2.wav', 'wb')
f2.write(info)
buf.tofile(f2)
f2.close()
```

## 文件的缓冲设置
```
#4096
tail -f demo.txt
f = open('demo.txt', 'www')
f.write('abc')
f.write('+'*4093)
f.write('-')

f = open('demo2.txt', 'w', buffering=2048)
f = open('demo3.txt', 'w', buffering=1)

f.write('sfasf\n')

f = open('demo4.txt', buffering=0)


```

## 内存映射

```
dd if=/dev/zero of=demo.bin bs=1024 count=1024
od -x demo.bin

import mmap
mmap.mmap?

f = open('demo.bin', 'r+b')
f.fileno()
m=mmap.mmap(f.filenono(), 0, access=mmap.ACCESS_WRITE)
type(m)
m[0]
m[10:20]
m[0] = '\x88'
m[4:8] = '\xff' * 4

```

## 文件的状态

```
#ll
import os

os.stat?
os.stat('a.txt')
os.lstat('a.txt')
os.fstat('a.txt')
f = open('')
f.fileno

s = os.stat('a.txt')
s.st_mode
bin(s.st_mode)
import stat
stat.S_ISDIR(s.st_mode)
stat.S_ISREG(s.st_mode)
#权限

s.st_atime
s.st_mtime

import time
time.localtime(s.st_time)
os.path? 

os.path.isdir()
```
## 临时文件

```
from tempfile import TemporaryFile, NamedTemporaryFile

TemporaryFile?
f = TemporaryFile()
f.write('abacefa' * 100000)
f.seek(0)
f.read(100)

ntf = NamedTemporaryFile()
ntf.name
ls 

```


## 读些csv文件

```
from urllib import urlretrieve
urlretrieve('http://table.finance.yahoo.com/table.csv?=s=000001.sz', pingan.csv)
cat pingan.csv|less
import csv
csv.reader
csv.writer?
rf = open('pingan.csv', 'rb')
reader = csv.reader(rf)
reader.next()
wf = open('pingan_copy.csv', 'wb')
writer = csv.write(wf)

writer.writerow(['Date'..])
writer.writerow(reader.next())

import csv
with open('pingan.csv', 'rb') as rf:
    reader = csv.reader(rf)
    with open('pingan2.csv', 'wb') as wf:
        writer = csv.writer(wf)
        headers = reader.next()
        writer.writerow(headers)
        for row in reader:
            
            if row[0] < '2016-01-01':
                break
            if row[5] > 5 *　10 **7:
                writer.writerow(row)
```


## JSON

```
#coding: utf-8

import requests
import json

from record import Record
record = Record(channels=1)
audioData = record.record(2)

from secret import API_KEY, SECRET_KEY
authUrl = 'https://openapi.baidu.com/oauth/2.0/token?grant_type=client_cri...+ API_'

respones = requests.get(authUrl)
res = json.load(response.content)
token = res['access_token']

cuid = 'xxxxx'
srvUrl = ''
httpHeader = {
    'Content-Type': ''
}

response = requests.post(srvUrl)
res.loads()
text = res['result'][0]
```

```
import json

l = [1, 2, 'abc', {'age':123, name: 'bob'}]
json.dumps(l)

json.dumps(l, separators=[',', ':'])#紧凑格式


json.(d, sort_keys=True)
json.loads()

with open('demo.json', 'wb') as f:
    json.dump(l, f)

cat demo.json

json.load(f)

```


## XML 


```
from xml.etree.ElementTree import parse

f = open('demo.xml')
et = parse(f)
root = et.getroot()
root.tag
root.attrib
root.text
root.text.strip()
root.getchildren()
for child in root:
    print child.get('name')

root.find('country')
root.findall('country')
root.iterfind('country')
for e in root.iterfind('country')
list(root.iter())
root.iter('rank')

root.findall('.//rank')
root.findall('country/*')
root.findall(.//rank/..)
root.findall('country[@name]')
root.findall('country[@age]')
root.findall('country[rank=5]')  
##xpath 语法
```


## 构建xml


```
def csvToXml(fname):
    with open(fname, 'rb') as f:
        reader = csv.reader(f)
        headers = reader.next()
        root = Element('Data')
        for row in reader:
            eRow = Element('Row')
            root.append(eRow)
            for tag, text in zip(headers, row):
                e = Element(tag)
                e.text = text
                eRow.append(e)
    prett(root)
    return ElementTree(root)

def pretty(e, level=0):
    if len(e) >0:
        e.text  = '\n' + '\t' * (level+1)
        for child in e:
            pretty(child, level+1)
        child.tail = child.tail[:-1]
    e.tail = '\n' + '\t' * level

et = csvToXml('pingan.csv')
et.write('pingan.xml')
```



## 读写Excel文件

```
import xlrd

book = xlrd.open_workbook('demo.xlsx')
book.sheets()
sheet = book.sheet_by_index(0)
sheet.nrows
sheet.ncols
sheet.cell?
cell = sheet.cell(0, 0)
xlrd.XL_CELL_NUMBER
cell.ctype
cell.value
sheet.row(1)
sheet.row_values(1)
sheet.row_values(1, 1)
sheet.put()

import xlwt

wbook = xlwt.Workbook()
wbook.add_sheet('sheet1')


import xlrd, xlwt

rbook = xlrd.open_workbook('demo.xlsx')
rsheet = rbook.sheet_by_index(0)
nc = rsheet.ncols
rsheet.put_cell(0, nc, xlrd.XL_CELL_TEXT, u'总分', None)
for row in xrange(1, rsheet.nrows):
    t = sum(rsheet.row_values(row, 1))
    rsheet.put_cell(row, nc, xlrd.XL_CELL.NUMBER, t, None)

wbook = xlwt.Workbook()
wsheet = wbook.add_sheet(rsheet.name)
style = xlwt.easyxf('align: vertical center, horizontal center')
for r in xrange(rsheet.nrows):
    for c in xrange(rsheet.ncols):
        wsheet.write(r, c, rsheet.cell_value(r, c), style)

wbook.save('output.xlsx')
```



## 
# 如何派生内置不可变类型并修改其实例化行为

#列子： 我们想定义一种新类型的元祖，对于传入的可迭代对象，我们只保留
#其中int类型且值大于0的元素，intTuple([1, -1, 'abac']) => (1)
```
class IntTuple(tuple):
    def __new__(cls, iterable):
        g = (for x in iterable if isinstance(x, int) and x > 0)
        return super(IntTuple, cls).__new__(cls, g)

    def __init__(self, iterable):
        print self
        #before
        super(IntTuple, self).__init__(iterable)

        #after

```






## 创建大量实例节省内存
```
class Player(object):
    def __init__(self, uid, name, status=0,level=1):
        self.uid = uid
        self.name = name
        self.status = status
        self.level level


class Player2(object):
    __slots__ = ['uid', 'name','stat', 'level']
    
    def __init__(self, uid, name, status=0, level=1):
        self.uid = uid
        self.name = name
        self.stat = status
        self.level = level
        
p1 = Player('123', 'lsf')
p2 = Player2('212', 'fdf')


import sys

sys.getsizeof(p1.__dict__)        
```


## 如何让对象支持上下文管理
```

from telnetlib import Telnet
from sys import stdin, stdout
from collectoins import deque

class TelnetClient(object):
    def __init__(self, addr, port=23):
        self.addr = addr
        self.port = port
        self.tn = None

    def start(self):


        #User 
        t = self.th.read_utntil('Login:　')
        stdout.write(t)
        user = stdin.readline()
        self.tn.write(user)

        #password

        t = self.tn.read_until('Password: ')
        stdout.write(t)
        while True:
            uinput = stdin.readline()
            if not uinput:
                break
            self.history.append(uinput)
            self.tn.write(uinput)
            t = self.tn.read_until('$_')
            stdout.write(t[len(uinput) +1:])
    
    def cleanup(self):
        pass

    def __enter__(self):
        self.tn = Telnet(self.addr, self.port)
        self.history = deque()
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.tn.close()
        self.tn = None
        with open(self.addr+'_histroy.txt', 'w') as f:
            f.writelines(self.history)
        

client = TelnetClient('127.0.0.1')
print '\nstart ....'
client.start()
print '\nCleanup...'
```


## 如何创建可管理的对象属性
```
from math import pi

class Circle(object):
    def __init__(self, radius):
        self.radius = radius

    def getRadius(self):
        return self.radius

    def setRadius(self, value):
        if not isinstance(value, (int, long, float)):
            raise ValueError('wrong type.')
        self.radius = float(value)
    
    def getArea(self):
        return self.radius**2 * pi
    R = property(getRadius, setRadius)

c = Circle(3.2)
``
```
## 如何让类支持比较操作
```
from funtiontools import total_ordering
from abc import ABCMeta, abstractmethod

@total_ordering
class Shape(object):
    @abstractmethod
    def area(self):
        pass
    def __lt__(self, obj):
        print 'in__lt__'
        if not isinstance(obj, Shape):
            raise TypeError('obj is not the shape')
        return self.area() < obj.area()
    def __eq__(self, obj):
        if not isinstance(obj, Shape):
            raise TypeError('obj is not the shape')
        print 'in__lt__'
        return self.area() == obj.area()
    
##只要定义两个 < = 推测出其他比较操作 < or = 

class Rectangle:
    def __init__(sefl, w, h):

        self .w = w
        self.h = h
    
    def area(self):
        return self.w * self.h 
    
class Circle(Shape):
    def __init__(self, r):
        self.r = r
    def area(self):
        return self.r ** 2 * 3.14

rect1 = Rectangle(5, 3)
rect2 = Rectangle(4, 4)
c1 = Circle(8)
rect1 > rect2 #=> rect1.area() > react2.area() rect1.__gt__(react2)
c1 < react2
```


## 如何使用描述符对实例属性做类型检查
```
class Attr(object):
    def __init__(self, name, type_):

        self.name = name
        self.type_ = type_

    def __get__(self, instance, cls):
        print 'in __get__', instance, cls
        return instance.__dict__[self.name]
    
    def __set__(self, instance, value):
        print 'in_set_'
        if not isinstance(value, self.type_):
            raise TypeError('expected an %s' % self.type_)
        instance.__dict__[self.name] = value
    def __delete__(self, instance):
        print 'in__del__'
        del instance.__dict__[self.name]

class Person(object):
    name = Attr('name', str)
    age = Attr('age', int)
    height = Attr('height', float)

p = Person()
p.name = 'Bob'
p.age = 123.1
```


##如何通过实例方法名字的字符串调用方法
```
from lib1 import Circle
from lib2 import Triangle
from lib3 import Rectangle

def getArea(shape):
    for name in ('area', 'getArea', 'get_area'):
        f = getattr(shape, name)
        if f:
            return f()

shape1 = Circle(2)
shape2 = Triangle(3, 4, 5)
shape3 = Rectangle(6, 4)

shapes = [shape1, shape2, shape3]
print map(getArea, shape)

from operator import methodcaller

s ='abc2123abc123'
s.find('abc', 4)
methodcaller('find', 'abc', '4')(s)##如何通过实例方法名字的字符串调用方法
from lib1 import Circle
from lib2 import Triangle
from lib3 import Rectangle

def getArea(shape):
    for name in ('area', 'getArea', 'get_area'):
        f = getattr(shape, name)
        if f:
            return f()

shape1 = Circle(2)
shape2 = Triangle(3, 4, 5)
shape3 = Rectangle(6, 4)

shapes = [shape1, shape2, shape3]
print map(getArea, shape)

from operator import methodcaller

s ='abc2123abc123'
s.find('abc', 4)
methodcaller('find', 'abc', '4')(s)
```



## 如何使用多线程
```
import csv
from xml.etree.ElementTree import Element, ElementTree
import requests
from StringIO import StringIO
from xml_pretty import pretty
# from collections import deque
from Queue import Queue



class DownloadThread(Thread):
    def __init__(self, sid):
        Thread.__init__(self)
        self.sid = sid
        self.url = 'http://table.finace.yahoo.com/table.csv?=s%s.sz'
        self.url %= str(sid).rjust(6, '0')
        sef.queue = queue
            
    def download(self, url):
        response = requests.get(url, timeout=1)
        if response.ok:
            return StringIO(response.content)

    def run(self):
        #1
        self.download(self.url)
        #2. sid, data)
        # q.append((sid, data))
        self.queue.put((self.sid, data))
class ConvertThread(Thread):
    def __init__(self, queue, ):
        Thread.__init__(self)
        self.queue = queue
    def csvtoXml(self, scsv, fxml):
        reader = csv.reader(scsv)
        headers = reader.next()
        headers = map(lambda h: h.replace(' ', ''), headers)
        root = Element('Data')
        for row in reader:
            eRow = Element('Row')
            root.append(eRow)
            for tag, text in zip(headers, row):
                e = Element(tag)
                e.text = text
                eRow.append(e)
        prett(root)
        return ElementTree(root)
    
    def run(self):
        #1. sid, data 
        count = 0

        while True:
            sid, data = self.queue.get()
            print 'Convert sid: %s' % sid
            if sid == -1:
                self.cEvent.set()
                self.cEvent.clear()
                break
            if data:
                fname = str(sid).rjust(6, '0') + '.xml'
                with open(fname, 'wb') as wf:
                    self.csvtoXml(rf, wf)
                count += 1
                if count == 5:
                    self.cEvent.set()
                    self.tEvent.wait()

                    self.tEvent.clear()
                    count = 0
q = Queue()
dThreads = [DownloadThread(i, q) for i in xrange(1, 11)]
cThread = ConvertThread(q)

for t in dThreads:
    t.start()

cThread.start()

for t in dThreads:
    t.join()
q.put((-1, None))


# if __name__ == "__main__":
#     # url = url
#     # rf = download(url)
#     # if rf:
#     #     with open('00001.xml', 'wb') as wf:
#     #         csvtoXml(rf, wf)
    
#     for sid in xrange(1, 100):
def handle(sid):
    url = 'http://table.finace.yahoo.com/table.csv?=s%s.sz'
    url %= str(sid).rjust(6, '0')

    rf = download(url)
    if rf is None: continue
    fname = str(sid).rjust(6, '0')
    with open(fname, 'wb') as wf:
        csvtoXml(rf, wf)
from threading import Thread

# t = Thread(target=handle, args=(1,))
# t.start()
# print 'main thread'

class MyThread(Thread):
    def __init__(self, sid):
        Thread.__init__(self)
        self.sid = sid
    def run(self):
        handle(self.sid)
treads = []
for i in xrange(1, 11):    
    t = MyThread(i)
    threads.append(i)
    t.start()
# t.join()  #等待线程退出

for t in threads:
    t.join()
print "main thread"


# tar.py

import tarfile
import os

def tarXML(tfname):
    tf = tarfile.open(tfname, 'w:gz')
    for fname in os.listdir('.'):
        if fname.endswith('.xml'):
            tf.add(fname)
            os.remove(fname)
    tf.close()

    if not tf.members:
        os.remove(tfname)

tarXML('test.tgz')

class TarThread(Thread):
    def __init__(self, cEvent, tEvent):
        Thread.__init__(self)
        
        self.count = 0
        self.cEvent = cEvent
        self.tEvent = tEvent
        self.setDeamon(True)
    def tarXML(self, tfname):
        self.count += 1
        tfname = '%d.tgz' % self.count
        tf = tarfile.open(tfname, 'w:gz')
        for fname in os.listdir('.'):
            if fname.endswith('.xml'):
                tf.add(fname)
                os.remove(fname)
        tf.close()

        if not tf.members:
            os.remove(tfname)
        
    
    def run(self):

        while True:
            self.cEvent.wait()
            self.tarXML()
            self.cEvent.clear()
            self.tEvent.set()




from threading import Event, Thread

def f(e):
    print 'f 0'
    e.wait()
    print 'f 1'


e = Event()
t = Thread(target=f, args=(e, ))
t.start()
e.set()
e.clear()


cEvent = Event()
tEvent = Event()
tThread = TarThread(cEvent, tEvent)
```







