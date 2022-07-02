# 函数内部，可以调用其他函数。如果一个函数在内部调用自身本身，这个函数就是递归函数
# 理论上，所有的递归函数都可以写成循环的方式，但循环的逻辑不如递归清晰。
# n!
def fact(n):
    if n ==1:
        return 1
    return n * fact(n-1)

print(fact(3))

# 使用递归函数需要注意防止栈溢出。递归调用的次数过多，会导致栈溢出。
# 解决递归调用栈溢出的方法是通过尾递归优化
# 尾递归是指，在函数返回的时候，调用自身本身，并且，return语句不能包含表达式。
def factt(n):
    return fact_iter(n, 1)

def fact_iter(num, product):
    if num == 1:
        return product
    return fact_iter(num - 1, num * product)

# print(factt(1000)) #都系栈溢出WO !!

#汉诺塔的移动
def move(n,a,b,c):
    if n == 1:
        print(a,'-->',c)
    else:
        move(n-1,a,c,b)
        move(1,a,b,c)
        move(n-1,b,a,c)

print(move(2,'A','B','C'))
