# 关键字参数kw
# 扩展函数的功能; 调用者愿意提供更多的参数，我们也能收到。**kw接收的是一个dict
def person(name, age, **kw):
    print('name:', name, 'age:', age, 'other:', kw)
    
print(person('Bob', 35, city='Beijing'))

extra = {'city': 'Beijing', 'job': 'Engineer'} # 可把dict转换为关键字参数传进去
print( person('Jack', 24, city=extra['city'], job=extra['job']))
print(person('Jack', 24, **extra)) #簡化寫法

# 命名關鍵字參數
# person的kw可以傳入不受限制的關鍵字參數
# 如果要限制关键字参数的名字，就可以用命名关键字参数
# 和关键字参数**kw不同，命名关键字参数需要一个特殊分隔符*，*后面的参数被视为命名关键字参数。*前面的是位置參數
def personn(name, age, *, city, job):
    print(name, age, city, job)
    
print(personn('Jack', 24,job='B',city='A'))

#如果函数定义中已经有了一个可变参数，后面跟着的命名关键字参数就不再需要一个特殊分隔符*了：
def person(name, age, *args, city, job):
    print(name, age, args, city, job)




