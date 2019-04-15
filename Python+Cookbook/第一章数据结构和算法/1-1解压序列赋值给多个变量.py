"""
现在有一个包含 N 个元素的元组或者是序列，怎样将它里面的值解压后同时赋值
给 N 个变量？
"""
"""
任何的序列（或者是可迭代对象）可以通过一个简单的赋值语句解压并赋值给多
个变量。唯一的前提就是变量的数量必须跟序列元素的数量是一样的。

"""

def fun(a,argsL = None):
	if argsL is None:
		argsL = []
	argsL.append(a )
	return argsL
for i in range(10):
	r = fun(i)
	print(r)