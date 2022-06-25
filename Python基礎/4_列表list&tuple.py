#list
Fruit = ['apple','orange','watermelon']
print(len(Fruit))

#list索引
print(Fruit)
print(Fruit[0])
print(Fruit[1])
print(Fruit[-2])

#list增加
Fruit.append('strawberry')
print(Fruit)

#list插入
Fruit.insert(2,'123')
print(Fruit)

#list刪除
Fruit.pop()
print(Fruit)
Fruit.pop(2)
print(Fruit)

#list替換
Fruit[0] = 'Horace'
print(Fruit)

#list排序
a = ['c', 'b', 'a','b']
a.sort()
print(a)

#list里面的元素的数据类型也可以不同; list可以多維
L = ['python', 'java', ['asp', 1233], True]
print(len(L))
print(L[2][1])

################################################################

#tuple
##tuple和list非常类似，但是tuple一旦初始化就不能修改
Fruit = ('apple','orange','watermelon')
print(Fruit)

#可修改的tuple
t = ('a', 'b', ['A', 'B'])
t[2][1] = 'A'
print(t)

#practice
L = [
    ['Apple', 'Google', 'Microsoft'],
    ['Java', 'Python', 'Ruby', 'PHP'],
    ['Adam', 'Bart', 'Lisa']
]
print(L)

# 打印Apple:
print(L[0][0])
# 打印Python:
print(L[1][1])
# 打印Lisa:
print(L[2][2])
