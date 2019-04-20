from machpyMoudle import engine
import numpy as np

#定义表名
file = 'train'
#测试数据
data = np.array([55])

train = engine.QT(data=data)
pre = train.run(file, istrain='n')

print(pre)