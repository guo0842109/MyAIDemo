
# np.reshape(a,newshape,order='C')
# https://cloud.tencent.com/developer/article/1351435
# np.random.random
# np.array()
# np.arange()
# np.linspace
# np.transpose
# np.random.rand()
# np.random.randn()
# np.random.randint()


# 1.np.random.random()函数参数
#
# np.random.random((1000, 20))
#
# 上面这个就代表一千个浮点数，从0-20中随机。
# 2.numpy.random.rand()函数用法
#
# numpy.random.rand(d0, d1, ..., dn)：
# 生成一个[0,1)之间的随机浮点数或N维浮点数组。
# 3.numpy.random.randn()函数用法：
#
# numpy.random.randn(d0, d1, ..., dn)：
# 生成一个浮点数或N维浮点数组，取数范围：正态分布的随机样本数。
# 4.numpy.random.standard_normal()函数用法
#
# numpy.random.standard_normal(size=None)：
# 生产一个浮点数或N维浮点数组，取数范围：标准正态分布随机样本
# 5.numpy.random.randint()函数用法：
#
# numpy.random.randint(low, high=None, size=None, dtype='l')：
# 生成一个整数或N维整数数组，取数范围：若high不为None时，取[low,high)之间随机整数，否则取值[0,low)之间随机整数。
# 6.numpy.random.random_integers()函数用法：
#
# numpy.random.random_integers(low, high=None, size=None)：
# 生成一个整数或一个N维整数数组，取值范围：若high不为None，则取[low,high]之间随机整数，否则取[1,low]之间随机整数。
# 7.numpy.random.random_sample()函数用法
#
# numpy.random.random_sample(size=None)：
# 生成一个[0,1)之间随机浮点数或N维浮点数组。
# 8.numpy.random.choice(）函数用法
#
# numpy.random.choice(a, size=None, replace=True, p=None)：
# 从序列中获取元素，若a为整数，元素取值为np.range(a)中随机数；若a为数组，取值为a数组元素中随机元素。
# 9.numpy.random.shuffle()函数用法
#
# numpy.random.shuffle(x)：
# 对X进行重排序，如果X为多维数组，只沿第一条轴洗牌，输出为None。
# 10.numpy.random.permutation()函数用法
#
# numpy.random.permutation(x)：
# 与numpy.random.shuffle(x)函数功能相同，两者区别：peumutation(x)不会修改X的顺序。