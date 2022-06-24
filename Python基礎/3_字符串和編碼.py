#求ACSII的十進制編碼
print(ord('A'))
print(ord('壕'))

##把ACSII的十進制編碼轉成對應的字符
print(chr(66))

#由于Python的字符串类型是str，在内存中以Unicode表示，一个字符对应若干个字节。如果要在网络上传输，或者保存到磁盘上，就需要把str变为以字节为单位的bytes
##Python对bytes类型的数据用带b前缀的单引号或双引号表示
###以Unicode表示的str通过encode()方法可以编码为指定的bytes
print('ABC'.encode('ascii'))
print('呂少壕'.encode('UTF-8')) #在bytes中，无法显示为ASCII字符的字节，用\x##显示

#把bytes变为str，就需要用decode()方法
print(b'ABC'.decode('ascii'))
print(b'\xe5\x91\x82\xe5\xb0\x91\xe5\xa3\x95'.decode('utf-8'))

#len()函数计算的是str的字符数，如果换成bytes，len()函数就计算字节数
print(len('呂少壕'))
print(len('呂少壕'.encode('UTF-8')))

#格式化#

# %运算符
## %就是用来格式化字符串的。在字符串内部，%s表示用字符串替换，%d表示用整数替换，%f表示用浮點數替換,有几个%?占位符，后面就跟几个变量或者值，顺序要对应好。如果只有一个%?，括号可以省略。
print('Hi, %s, Nice to meet you %s'  % ('bb', 'honestly'))
val = int(input('input a number:'))
print('growth rate: %d %%'% val)

#字符串的format()方法，它会用传入的参数依次替换字符串内的占位符{0}、{1}……
print('Hello, {0}, 成绩提升了 {1:.1f}%'.format('小明', 17.125))

#以f开头的字符串，称之为f-string，它和普通字符串不同之处在于，字符串如果包含{xxx}，就会以对应的变量替换
r = 1
s = 3.14 * r**2
print(f'The area of a circle with radius {r} is {s:.2f}')

#practice
s1= 72
s2 = 85
r = 100* (s2-s1)/s1
print('小明今年的成續比去年提升了%.1f%%' % r)
print('小明今年的成續比去年提升了{0:.1f}%'.format(r))
print(f'小明今年的成續比去年提升了{r:.1f}%')