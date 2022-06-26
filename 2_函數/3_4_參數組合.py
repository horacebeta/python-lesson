# 在Python中定义函数，可以用必选参数、默认参数、可变参数、关键字参数和命名关键字参数，这5种参数都可以组合使用。
# 但是请注意，参数定义的顺序必须是：必选参数、默认参数、可变参数、命名关键字参数和关键字参数。

from audioop import mul
from keyword import kwlist


def f1(a, b, c=0, *args, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'args =', args, 'kw =', kw)
      
print(f1(1,2))
print(f1(1,2,3))
print(f1(1,2,3,4,5))
print(f1(1,2,3,4,5,x=6))

def f2(a, b, c=0, *, d, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'd =', d, 'kw =', kw)
    
print(f2(1,2,d=3))
print(f2(1,2,d=3,e=4))
print(f2(1,2,c=77,d=3,e=4))

#practice
#可接收一个或多个数并计算乘积

def calcc(*numbers):
    if len(numbers) == 0:
        raise TypeError('不能不輸入參數')
    sum = 1
    for n in numbers:
        sum = sum * n
    return sum

print(calcc(3,4,5,5,5))

