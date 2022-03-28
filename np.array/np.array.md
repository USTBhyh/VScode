[TOC]
***
#CSDN
>https://blog.csdn.net/gqixf/article/details/80195733?ops_request_misc=&request_id=&biz_id=102&spm=1018.2226.3001.4187
***
>https://blog.csdn.net/fu6543210/article/details/83240024?ops_request_misc=%257B%2522request%255Fid%2522%253A%2522164751111616782092919410%2522%252C%2522scm%2522%253A%252220140713.130102334..%2522%257D&request_id=164751111616782092919410&biz_id=0&spm=1018.2226.3001.4187
***
#与列表的区别
>标准Python的列表(list)中，元素本质是对象。如：L = [1, 2, 3]，需要3个指针和三个整数对象，对于数值运算比较浪费内存和CPU。因此，Numpy提供了ndarray(N-dimensional array object)对象：存储单一数据类型的多维数组。
***
#构造函数
```
np.array(1,2,3,4,5)#一维数组
np.array([1,2][3,4])#多维数组
```
***
#常用函数
###arand
>用法 ：np.arange(0,10)  // 生成[0,1,2,3,4,5,6,7,8,9] 左开右闭不包括10
###reshape
>用法:
np.arange(1,10).reshape((3,3)) 
 #从(3,4)改为(4,3)并不是对数组进行转置，而只是改变每个轴的大小，数组元素在内存中的位置并没有改变
reshape(-1,1) 任一行一列
###构造等差数列
> np.linspace(1, 10, 10)
 #构造等差数列 开始值，结束值，共几个数字 
  #包括终止值 [1,2,3,4,5,6,7,8,9,10]
  #可以通过选项配置其不包括终止值
  c=np.linspace(1, 10, 10, endpoint=False)
###构造等比数列
>np.logspace(1,4,4,base=2,endpoint=True)
 #参数：开始值(取log计算后的值)，结束值（取log运算后的值），base:log运算基数，等差数列公比
###随机数生成
>随机生成（4*4）个0-10的数的二维数组
  np.random.randint(a, b, size=(c, d))
  随机生成 0-1的10个数字
  np.random.rand 
