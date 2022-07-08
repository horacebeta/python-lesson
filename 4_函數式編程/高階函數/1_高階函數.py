# 函數本身可賦值給變量
print(abs(-1))
f = abs
print(f(-29))

# 變量可以指向函数，函数的参数能接收变量，那么一个函数就可以接收另一个函数作为参数，这种函数就称之为高阶函数
def abc(x,y,f):
    return f(x)+f(y)

print(abc(-6,-11,abs))