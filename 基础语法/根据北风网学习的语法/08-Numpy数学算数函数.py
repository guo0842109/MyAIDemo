import numpy as np

'''
绝对值
'''
a = np.random.randint(3,9,size = (2,3))
print(a)
print(np.abs(a))
b = np.fabs(a)
print(np.fabs(a))
'''
平方根
'''
print(np.sqrt(b))

'''
平方
'''
print(np.square(b))

'''
取正负号
'''
print(np.sign(b))

'''
e的次方
'''
print(np.exp(b))

'''
log
'''
print(np.log(b))