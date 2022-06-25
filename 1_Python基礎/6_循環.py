#range()函数，可以生成一个整数序列
W = list(range(101))
W.pop(0)
print(W)

#for x in ...循环就是把每个元素代入变量x，然后执行缩进块的语句
sum = 0
for x in W:
    sum = sum + x
print(sum)

#while循环，只要条件满足，就不断循环，条件不满足时退出循环
sum = 0
n = 100
while n > 0:
    sum = sum + n
    n = n -1
print(sum)

#practice
#利用循环依次对list中的每个名字打印出Hello, xxx!
L = ['Bart', 'Lisa', 'Adam']
for name in L:
    print(f'{name}')