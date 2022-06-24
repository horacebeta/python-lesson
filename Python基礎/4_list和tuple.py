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

#list里面的元素的数据类型也可以不同; list可以多維
L = ['python', 'java', ['asp', 1233], True]
print(L[2][1])