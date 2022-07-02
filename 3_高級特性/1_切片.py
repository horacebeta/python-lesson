# 取指定索引范围的操作，Python提供了切片（Slice）操作符
L = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']

print(L[0:3]) #從索引0開始取，索引3為止，但不包括索引3
print(L[:])

M = list(range(101))
print(M[-10:])
print(M[:-10:2])

#字符串也可以切片
H = 'ABCDEFG'
print(H[:3])

# practice
# 利用切片操作，实现一个trim()函数，去除字符串首尾的空格，注意不要调用str的strip()方法：
def trim(x):
    if x[:1] == ' ':
        return trim(x[1:])
    elif x[-1:] == ' ':
        return trim(x[:-1])
    else:
        return x

print(trim('  Horace '))