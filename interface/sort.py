# _*_ coding:utf-8 _*_

# 冒泡排序
def bubbleSort(alist):
    for passnum in range(len(alist)-1,0,-1):
        #print alist,passnum
        for i in range(passnum):
            if alist[i]>alist[i+1]:
                temp = alist[i]
                alist[i] = alist[i+1]
                alist[i+1] = temp
    return alist

a = bubbleSort([2,8,3,5,1])
print a

for j in range(1,5):
	print j