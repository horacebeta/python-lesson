# map()
# map函数接收两个参数，一个是函数，一个是Iterable，map将传入的函数依次作用到序列的每个元素，并把结果作为新的Iterator返回。
def f(x):
    return x*x

r = map(f,list(range(10)))
print(list(r))

w = map(str,list(range(10))) # map的函數可放任何抽象函數
print(list(w))

# reduce()
# reduce把一个函数作用在一个序列[x1, x2, x3, ...]上，这个函数必须接收两个参数，reduce把结果继续和序列的下一个元素做累积计算
# reduce(f, [x1, x2, x3, x4]) = f(f(f(x1, x2), x3), x4)
from functools import reduce
def fn(x,y):
    return x* 10 +y

print (reduce(fn,[1,3,5,7,9]))

# 組合map&reduce
# 假設沒有int()
def char2num(s):
    digits = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
    return digits[s]

print(reduce(fn,map(char2num,'31234')))

# 整理成一函數
digits = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
def str2int(s):
    def fn(x,y):
        return x*10+y
    def char2num(s):
        return digits[s]
    return reduce(fn,map(char2num,s))

print(str2int('123'))

# practice
# 利用map()函数，把用户输入的不规范的英文名字，变为首字母大写，其他小写的规范名字。
def normalize(name):
    return name[:1].upper()+name[1:].lower()

L = ['adam', 'LISA', 'barT']
print(list(map(normalize,L)))

# sum()函数可以接受一个list并求和，请编写一个prod()函数，可以接受一个list并利用reduce()求积
def prod(L):
    def ff(x,y):
        return x*y
    return reduce(ff,L)

print(prod([2,3,4]))

# 利用map和reduce编写一个str2float函数，把字符串'123.456'转换成浮点数123.456
digits = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
def str2float(s):
    def char2num(s):
        return digits[s]
    def fn(x,y):
        return x*10+y
    i = s.index('.')
    s = s.replace('.','')
    return reduce(fn,map(char2num,s)) / pow(10,len(s)-i)

print(str2float('123.223'))
