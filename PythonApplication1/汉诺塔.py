﻿#汉诺塔
#把a柱子移动到c柱子，附带输出

#初始值
num=0
towerA=[]
towerB=[]
towerC=[]
a=('A',towerA)
b=('B',towerB)
c=('C',towerC)


def babieta(n,a=('a',[0]),b=('b',[]),c=('c',[])):
    if n==1:
        print('#',a[0],'-->',c[0])
        c[1].append(a[1][-1])
        a[1].remove(c[1][-1])
        print(a,c)
    else:
        babieta(n-1,a,c,b)
        print('#',a[0],'-->',c[0])
        c[1].append(a[1][-1])
        a[1].remove(c[1][-1])
        print(a,c)
        babieta(n-1,b,a,c)
    pass
#输入变量和赋值
num=int(input('请输入汉诺塔的层数：'))
if num>=15:
    print('num is too big')
    exit(0)
towerA=list(range(num))
towerA.reverse()
towerB=[]
towerC=[]
a=('A',towerA)
b=('B',towerB)
c=('C',towerC)
#检查变量
print(a,b,c,'start program',sep='\n',end='\n')
babieta(num,a,b,c)
#print 结果
print('最终结果',a,b,c,sep='\n',end='\n')
