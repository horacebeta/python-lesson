# range
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(list(range(1,11)))

# [1x1, 2x2, 3x3, ..., 10x10]
# method 1
L = []
for x in range(1,11):
    L.append(x*x)

print(L)

# method 2
print(list(x*x for x in range(1,11)))

print(list(x*x for x in range(1,11)if x % 2 == 0) ) #加篩選條件

# 兩層循環，生成全排列
print(list(m + n for m in 'ABC' for n in 'DEF'))

# 實例：列出当前目录下的所有文件和目录名
import os
print(list(d for d in os.listdir('.')))

# 兩個變量
d = {'x':'A','y':'B','z':'C'}

for k,v in d.items():
    print(k, '=',v)

print(list(k + '=' + v for k,v in d.items()))

# 套函數
L = ['HORace', 'Bb']
print(list(f.lower() for f in L))

# for前面的if ... else是表达式，而for后面的if是过滤条件，不能带else。
print(list(x*x for x in range(1,11)if x % 2 == 0) ) #加篩選條件
print(list(x*x if x % 2 == 0 else 0 for x in range(1,11)))

# isinstance() 判斷對象是否是一個已知的類型
x = 'abc'
y = 123
print(isinstance(x,str))
print(isinstance(y,int))

# practice
# shows ['hello', 'world', 'apple']
L1 = ['Hello', 'World', 18, 'Apple', None]
print(list(x.lower() for x in L1 if isinstance(x,str) == True))