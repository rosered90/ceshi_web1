# -*- coding:utf-8 -*-

def deco(func):
	def wrap():
		print("yufatang1")
		func()
		print("yufatang2")
	return wrap()

@deco
def myfun():
	print("myfun() called.")
	return 'ok'