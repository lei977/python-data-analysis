# 把箱线图、核密度图和小提琴图组合
import seaborn as sns
from dautil import data
import matplotlib.pyplot as plt

# 加载天气数据并计算标准分数
df = data.Weather.load()
zscores = (df - df.mean()) / df.std()

# 绘制标准分数的小提琴图
# %matplotlib inline
plt.figure()
plt.title('Weather Violin Plot')
sns.violinplot(zscores.resample('M'))
plt.ylabel('Z-scores')
