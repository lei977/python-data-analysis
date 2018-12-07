K-近邻（KNN）算法练习

参考博客
https://cuijiahua.com/blog/2017/11/ml_1_knn.html

参考源码
https://github.com/Jack-Cherish/Machine-Learning/tree/master/kNN


k-近邻算法步骤如下：

计算已知类别数据集中的点与当前点之间的距离；
按照距离递增次序排序；
选取与当前点距离最小的k个点；
确定前k个点所在类别的出现频率；
返回前k个点所出现频率最高的类别作为当前点的预测分类。

源码中针对多维数据采用欧氏距离


test
准备数据集
test1
k-近邻算法
test2
k-近邻算法实战之约会网站配对效果判定