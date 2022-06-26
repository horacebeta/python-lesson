#x^n的函數
#power(x, n)函数有两个参数：x和n，这两个参数都是位置参数，调用函数时，传入的两个值按照位置顺序依次赋给参数x和n
def power(x,n):
    s = 1
    while n > 0:
        n = n-1
        s = s*x
    return s
    
print(power(5,2))

# 默認參數
# 把第二个参数n的默认值设定为2
# 必选参数在前，默认参数在后
# 变化大的参数放前面，变化小的参数放后面
def powerp(x,n=2):
    s = 1
    while n > 0:
        n = n-1
        s = s*x
    return s

print(powerp(6,3))

# 可以不按顺序提供部分默认参数。当不按顺序提供部分默认参数时，需要把参数名写上。
def enroll(name, gender, age=6, city='Beijing'):
    print('name:', name)
    print('gender:', gender)
    print('age:', age)
    print('city:', city)

print(enroll('Bob', 'M', 7))
print(enroll('Adam', 'M', city='Tianjin'))

# 默认参数必须指向不变对象
# 錯誤例子，[]是變量
def add_end(L=[]):
    L.append('END')
    return L
print(add_end())
print(add_end())
print(add_end())

# 糾正，None是不變量
def add_end(L=None):
    if L is None:
        L = []
    L.append('END')
    return L
print(add_end())
print(add_end())
print(add_end())