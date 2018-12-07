# -*- coding: UTF-8 -*-
from matplotlib.font_manager import FontProperties
import matplotlib.lines as mlines
import matplotlib.pyplot as plt
import numpy as np

"""
函数说明:打开并解析文件，对数据进行分类：1代表一类,2代表二类,3代表三类

Parameters:
    filename - 文件名
Returns:
    returnMat - 特征矩阵
    classLabelVector - 分类Label向量

特征数据集：
1-降落数值(s)
2-丙二醛(μmol/g)	
3-过氧化物酶(U/g)
4-脂肪酸值(mgKOH/100g)
5-发芽率(%)
6-电导率(μs/cm/g)
7-还原糖(%)

"""
def file2matrix(filename):
    #打开文件
    fr = open(filename)
    #读取文件所有内容
    arrayOLines = fr.readlines()
    #得到文件行数
    numberOfLines = len(arrayOLines)
    #返回的NumPy矩阵,解析完成的数据:numberOfLines行,3列
    returnMat = np.zeros((numberOfLines,7))
    #返回的分类标签向量
    classLabelVector = []
    #行的索引值
    index = 0
    for line in arrayOLines:
        #s.strip(rm)，当rm空时,默认删除空白符(包括'\n','\r','\t',' ')
        line = line.strip()
        #使用s.split(str="",num=string,cout(str))将字符串根据'\t'分隔符进行切片。
        listFromLine = line.split('\t')
        #将数据前三列提取出来,存放到returnMat的NumPy矩阵中,也就是特征矩阵
        returnMat[index,:] = listFromLine[0:7]
        #根据文本中标记的喜欢的程度进行分类,1代表一类,2代表二类,3代表三类
        if listFromLine[-1] == 'one':
            classLabelVector.append(1)
        elif listFromLine[-1] == 'two':
            classLabelVector.append(2)
        elif listFromLine[-1] == 'three':
            classLabelVector.append(3)
        index += 1
    return returnMat, classLabelVector

"""
函数说明:可视化数据

Parameters:
    datingDataMat - 特征矩阵
    datingLabels - 分类Label
Returns:
    无

"""
def showdatas(datingDataMat, datingLabels):
    #设置汉字格式
    font = FontProperties(fname=r"c:\windows\fonts\simsun.ttc", size=18)
    #将fig画布分隔成1行1列,不共享x轴和y轴,fig画布的大小为(13,9)
    #当nrow=2,nclos=2时,代表fig画布被分为四个区域,axs[0][0]表示第一行第一个区域
    fig, axs = plt.subplots(nrows=2, ncols=2,sharex=False, sharey=False, figsize=(13,9))

    numberOfLabels = len(datingLabels)
    LabelsColors = []
    for i in datingLabels:
        if i == 1:
            LabelsColors.append('black')
        if i == 2:
            LabelsColors.append('orange')
        if i == 3:
            LabelsColors.append('red')
    #画出散点图,以datingDataMat矩阵的第一列(降落数值(s))、第二列(丙二醛(μmol/g))数据画散点数据,散点大小为15,透明度为0.5
    axs[0][0].scatter(x=datingDataMat[:,0], y=datingDataMat[:,1], color=LabelsColors,s=15, alpha=.5)
    #设置标题,x轴label,y轴label
    axs0_title_text = axs[0][0].set_title(u'降落数值(s)与丙二醛(μmol/g)',FontProperties=font)
    axs0_xlabel_text = axs[0][0].set_xlabel(u'降落数值(s)',FontProperties=font)
    axs0_ylabel_text = axs[0][0].set_ylabel(u'丙二醛(μmol/g',FontProperties=font)
    plt.setp(axs0_title_text, size=12, weight='bold', color='red')
    plt.setp(axs0_xlabel_text, size=10, weight='bold', color='black')
    plt.setp(axs0_ylabel_text, size=10, weight='bold', color='black')

    #画出散点图,以datingDataMat矩阵的第一列(降落数值(s))、第三列(过氧化物酶(U/g))数据画散点数据,散点大小为15,透明度为0.5
    axs[0][1].scatter(x=datingDataMat[:,0], y=datingDataMat[:,2], color=LabelsColors,s=15, alpha=.5)
    #设置标题,x轴label,y轴label
    axs1_title_text = axs[0][1].set_title(u'降落数值(s)与过氧化物酶(U/g)',FontProperties=font)
    axs1_xlabel_text = axs[0][1].set_xlabel(u'降落数值(s)',FontProperties=font)
    axs1_ylabel_text = axs[0][1].set_ylabel(u'过氧化物酶(U/g)',FontProperties=font)
    plt.setp(axs1_title_text, size=12, weight='bold', color='red')
    plt.setp(axs1_xlabel_text, size=10, weight='bold', color='black')
    plt.setp(axs1_ylabel_text, size=10, weight='bold', color='black')

    #画出散点图,以datingDataMat矩阵的第二列(丙二醛(μmol/g))、第三列(过氧化物酶(U/g))数据画散点数据,散点大小为15,透明度为0.5
    axs[1][0].scatter(x=datingDataMat[:,1], y=datingDataMat[:,2], color=LabelsColors,s=15, alpha=.5)
    #设置标题,x轴label,y轴label
    axs2_title_text = axs[1][0].set_title(u'丙二醛(μmol/g)与过氧化物酶(U/g)',FontProperties=font)
    axs2_xlabel_text = axs[1][0].set_xlabel(u'丙二醛(μmol/g)',FontProperties=font)
    axs2_ylabel_text = axs[1][0].set_ylabel(u'过氧化物酶(U/g)',FontProperties=font)
    plt.setp(axs2_title_text, size=12, weight='bold', color='red')
    plt.setp(axs2_xlabel_text, size=10, weight='bold', color='black')
    plt.setp(axs2_ylabel_text, size=10, weight='bold', color='black')


    #设置图例
    didntLike = mlines.Line2D([], [], color='black', marker='.',
                      markersize=6, label='one')
    smallDoses = mlines.Line2D([], [], color='orange', marker='.',
                      markersize=6, label='two')
    largeDoses = mlines.Line2D([], [], color='red', marker='.',
                      markersize=6, label='three')


    #添加图例
    axs[0][0].legend(handles=[didntLike,smallDoses,largeDoses])
    axs[0][1].legend(handles=[didntLike,smallDoses,largeDoses])
    axs[1][0].legend(handles=[didntLike,smallDoses,largeDoses])
    #显示图片
    plt.show()


"""
函数说明:main函数

Parameters:
    无
Returns:
    无

"""
if __name__ == '__main__':
    #打开的文件名
    filename = "wheatSet.txt"
    #打开并处理数据
    datingDataMat, datingLabels = file2matrix(filename)
    showdatas(datingDataMat, datingLabels)