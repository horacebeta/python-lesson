# def语句，依次写出函数名、括号、括号中的参数和冒号:
# 然后，在缩进块中编写函数体，函数的返回值用return语句返回
# 一旦执行到return时，函数就执行完毕，并将结果返回
# 函数执行完毕也没有return语句时，自动return None

def my_abs(x):
    if x >= 0:
        return x
    else:
        return -x

print(my_abs(-99))

#空函數
def nop():
    pass

#参数检查
#当传入了不恰当的参数时，内置函数abs会检查出参数错误，而我们定义的my_abs没有参数检查
#修改一下my_abs的定义，对参数类型做检查，只允许整数和浮点数类型的参数。数据类型检查可以用内置函数isinstance()实现：
def my_abs(x):
    if not isinstance(x, (int, float)):
        raise TypeError('bad operand type')
    if x >= 0:
        return x
    else:
        return -x
#print(my_abs('A'))

#返回多个值
import math

def move(x, y, step, angle=0):
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return nx, ny

x, y = move(100, 100, 60, math.pi / 6)
print(x, y)

#Python的函数返回多值其实就是返回一个tuple
r = move(100, 100, 60, math.pi / 6)
print(r)

#practice
#定义一个函数quadratic(a, b, c)，接收3个参数，返回一元二次方程 ax^2+bx+c=0的兩個解

def quadratic(a,b,c):
    if a==0:
        print("a不能等於0")
    elif b*b - 4*a*c<0:
        print('無解')
    else:
        x1=(-b+math.sqrt(b*b-4*a*c))/(2*a)
        x2=(-b-math.sqrt(b*b-4*a*c))/(2*a)
        return x1, x2

print(quadratic(1,3,1))
        