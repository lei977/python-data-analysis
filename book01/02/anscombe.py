
# 程序存在错误，尚未解决

# 导入
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib as mpl
from dautil import report
from dautil import plotting
import numpy as np
from tabulate import tabulate


# 定义以下函数来计算某一数据集中x和y的均值和方差、相关系数
# 以及斜率和每个数据集的线性拟合的截距
def aggregate():
    df = sns.load_dataset("anscombe")
    agg = df.groupby('dataset').agg([np.mean, np.var]).transpose()
    groups = df.groupby('dataset')

    corr = [g.corr()['x'][1] for _, g in groups]
    builder = report.DFBuilder(agg.columns)
    builder.row(corr)

    fits = [np.ployfit(g['x'], g['y'], 1) for _, g in groups]
    builder.row([f[0] for f in fits])
    builder.row([f[1] for f in fits])
    bottom = builder.build(['corr', 'slope', 'intercept'])

    return df, pd.concat((agg, bottom))


# 下面这个函数返回一个字符串，这个字符串有一部分是Markdown，有一部分是重组的文字，
# 有一部分是HTML，这主要是因为原生的Markdown不支持图表。
def generate(table):
    writer = report.RSTWriter()
    writer.h1('Anscombe Statistics')
    writer.add(tabulate(table, tablefmt='html', floatfmt='.3f'))

    return writer.rst


# 绘制数据并相应地与Seaborn的lmplot()函数线性拟合
def plot(df):
    sns.set(style="ticks")
    g = sns.lmplot(x="x", y="y", col="dataset", hue="dataset",
                   data=df, col_wrap=2, ci=None, palette="muted", size=4,
                   scatter_kws={"s": 50, "alpha": 1})

    plotting.embellish(g.fig.axes)


# 展示一个统计数据的表格如下：
df, table = aggregate()
from IPython.display import display_markdown

display_markdown(generate(table), raw=True)

# 以下几行代码绘制了数据集
# %matplotlib inline
plot(df)
