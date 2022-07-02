# for 循環可以遍歷list或 tuple，這種遍歷稱為迭代
# dict可迭代
d = {'a':1,'b':2,'c':3}
print(d)

#默認情況下，dict迭代的是key
for bb in d:
    print(bb)
    
for cc in d.values():
    print (cc)
    
for dd in d.items():
    print(dd)

# 字符串可迭代   
T = 'Horace'
for ee in T:
    print(ee)
    
L = ['A','B','C']
for i,value in enumerate(L):
    print(i,value)
    
M = [4,67,7,8,9,55]
print (max(M))

def findMinAndMax(L):
    if len(L) == 0:
        return(None,None)
    min = max = L[0]
    for i in L:
        if i<min:
            min = i
    for i in L:
        if i>max:
            max = i
    return (min,max)

print(findMinAndMax(M))