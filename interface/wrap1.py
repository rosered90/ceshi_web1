# _*_ coding:utf-8 _*_

def deco(func):
	def _deco(a,c):
		print("before called")
		ret = func(a,c)
		print("after called")
		return ret
	return _deco


@deco
def myfunc(a,c):
	print("qingwen%s,%s"%(a,c))
	return a+c

myfunc(2,50)