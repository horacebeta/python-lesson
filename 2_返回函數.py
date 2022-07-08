# 一个函数可以返回一个计算结果，也可以返回一个函数。
# 函数lazy_sum中又定义了函数sum，并且，内部函数sum可以引用外部函数lazy_sum的参数和局部变量，当lazy_sum返回函数sum时，相关参数和变量都保存在返回的函数中，这种称为“闭包（Closure）”的程序结构
def lazy_sum(*args):
    def sum():
        ax = 0
        for n in args:
            ax = ax + n
        return ax
    return sum

r = (1, 3, 5, 7, 9)
f = lazy_sum(r)
print(f)

# 閉包
# 如涉及