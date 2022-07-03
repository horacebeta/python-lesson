# 不必创建完整的list，从而节省大量的空间。在Python中，这种一边循环一边计算的机制，称为生成器：generator
# 第一种方法很简单，只要把一个列表生成式的[]改成()
L = [x*x for x in range(10)]
print(L)

# 一个一个打印出来，可以通过next()函数获得generator的下一个返回值
g = (x*x for x in range(10))
print(g)
print(next(g))
print(next(g))
print(next(g))

# generator也是可迭代对象，可使用for循环
m = (x*x for x in range(10))
for n in m:
    print(n)
    
# 斐波拉契数列（Fibonacci）：1, 1, 2, 3, 5, 8, 13, 21, 34, ...
def Fib(max):
    n,a,b = 0,0,1
    while n < max:
        print(b)
        a,b = b, a+b
        n = n +1
    return 'done'
print(Fib(20))

# Fib函数实际上是定义了斐波拉契数列的推算规则，可以从第一个元素开始，推算出后续任意的元素，这种逻辑其实非常类似generator。
# 要把fib函数变成generator函数，只需要把print(b)改为yield b就可以了：
def Fibb(max):
    n,a,b = 0,0,1
    while n < max:
        yield b
        a,b = b, a+b
        n = n +1
    return 'done'

for n in Fibb(10):
    print(n)
    
# odd不是普通函数，而是generator函数，在执行过程中，遇到yield就中断，下次又继续执行。
def odd():
    print('step 1')
    yield 1
    print('step 2')
    yield(3)
    print('step 3')
    yield(5)
    
g = odd()
print(next(g))
print(next(g))
print(next(g))

# practice
# 杨辉三角
#          1
#         / \
#        1   1
#       / \ / \
#      1   2   1
#     / \ / \ / \
#    1   3   3   1
#   / \ / \ / \ / \
#  1   4   6   4   1
# / \ / \ / \ / \ / \
#1   5   10  10  5   1

def tri(max):
    L = [1]
    n = 0
    while n < max:
        yield L
        L = [1] + [L[n] + L[n+1] for n in range(len(L)-1)] + [1]
        n = n+1
    return 'done'

for n in tri(10):
    print(n)
