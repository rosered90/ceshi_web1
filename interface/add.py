# _*_ coding:utf-8 _*_

def deco(func):
	def _deco(*args, **kwargs):
		print("before called")
		ret = func(*args, **kwargs)
		print("after called")
		return ret
	return _deco


@deco
def myfunc1(a,c):
	print("qingwen%s,%s"%(a,c))
	return a+c

@deco
def myfunc2(a,c,b):
	print("qingwen%s,%s"%(a,c))
	return a+c

myfunc1(2,50)
myfunc2(1,2,3)


