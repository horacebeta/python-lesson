#if语句判断是True，就把缩进的两行print语句执行了
#if添加一个else语句，意思是，如果if判断是False，不要执行if的内容，去把else执行了
#用elif做更细致的判断
age = 16
if age >= 18:
    print('adult')
elif age >= 6:
    print('teenager')
else:
    print('kid')
    
#if语句执行有个特点，它是从上往下判断，如果在某个判断上是True，把该判断对应的语句执行后，就忽略掉剩下的elif和else
age = 20
if age >= 6:
    print('teenager')
elif age >= 18:
    print('adult')
else:
    print('kid')
    
birth = int(input('birth: '))
if birth < 2000:
    print('00前')
else:
    print('00后')
    
#practice
#小明身高1.75，体重80.5kg。请根据BMI公式（体重除以身高的平方）帮小明计算他的BMI指数，并根据BMI指数：
#低于18.5：过轻
#18.5-25：正常
#25-28：过重
#28-32：肥胖
#高于32：严重肥胖

h = float(input('請輸入你的身高(米):'))
w = float(input('請輸入你的體重(KG):'))
BMI = w/(h ** 2)
s = '你的體重'
if BMI<18.5:
    print(f'你的BMI為{BMI:.1f}，過輕')
elif 18.5 <= BMI <= 25:
    print(f'你的BMI為{BMI:.1f}，正常')
elif 25 <= BMI <= 28:
    print(f'你的BMI為{BMI:.1f}，过重')
elif 28 <= BMI <= 32:
    print(f'你的BMI為{BMI:.1f}，肥胖')
else:
    print(f'你的BMI為{BMI:.1f}，严重肥胖')



