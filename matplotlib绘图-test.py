import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['SimHei']#显示中文
#matplotlib默认没有安装中文，需要在matplotlib的ttf目录中添加中文字体
#~/.local/lib/python3.5/site-packages/matplotlib/mpl-data/fonts/ttf/simhei.ttf
#~/.cache/matplotlib$ rm -rf *.*  #清除matplotlib缓冲，重置后启动
plt.rcParams['axes.unicode_minus'] = False#显示负数

x = np.arange(0,4,0.01)
y = np.sin(2*np.pi*x)#曲线函数
plt.figure(figsize=(10,6))#改变图片大小
plt.plot(x,y,'g--',alpha=0.5,linewidth=3,)#绘制线状图;alpha为透明度，g--绿色虚线图
plt.xlim(0,4)#改变x轴的显示区域
plt.ylim(-1,1)#改变y轴的显示区域
plt.grid()#显示网格
plt.xlabel('时间(s)',fontsize=12)#x轴的标签
plt.ylabel('电压(V)',fontsize=12)#y轴的标签
plt.title('电压变化趋势图',fontsize=15)#标题
plt.text(1.5,0.25,'y=sin(2*pi*x)',fontsize=12)#插入文本
plt.text(1,0.75,'学个锤子',fontsize=30)#插入文本
plt.savefig('/home/jason/zelin/数据分析/ChuiziDianya.png',dpi=400,bbox_inches='tight')#保存 在show前保存
plt.show()#显示图片 show（）之后为空白页
