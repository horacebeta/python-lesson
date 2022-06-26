# 可变参数就是传入的参数个数是可变的，可以是1个、2个到任意个，还可以是0个
# 例子，给定一组数字a，b，c……，请计算a2 + b2 + c2 + ……
def calc(numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum

print(calc([1,2]))
print(calc(range(3)))
# print(calc()), fail

# 利用可变参数，调用函数的方式可以简化成这样
# *nums表示把nums这个list的所有元素作为可变参数传进去
def calcc(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum

print(calcc()) # 0個參數都work
print(calcc(1,2))
print(calcc(*range(3)))