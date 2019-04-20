"""
写算法的模块
"""
from sklearn.model_selection import train_test_split
from sklearn import linear_model
from sklearn.externals import joblib
import os
from sklearn.metrics import mean_squared_error

class AlgorithmTrain(object):
    def __init__(self, datas):
        self._datas = datas
        self._trainX = None
        self._trainY = None
        self._testX = None
        self._testY = None
        self._result = None

    #用于写算法的过程
    def AI(self):
        #先划分数据集
        self.SplitTrainTest(0.1)
        ##########算法实现过程##########
        #数据集升维
        self._trainX = self._trainX.reshape(-1, 1)
        self._testX = self._testX.reshape(-1, 1)

        clf = linear_model.LinearRegression()
        clf.fit(self._trainX, self._trainY)

        #预测结果
        self._result = clf.predict(self._testX)
        ################################
        #保存模型参数
        self.save(model=clf, name='line.m')
        #测试性能
        self.performance(self._testY, self._result)
        return self._result

    #区分训练集和测试集
    def SplitTrainTest(self, scale):
        #scale用于划分训练集和测试集的比例
        self._trainX, self._testX, self._trainY, self._testY = train_test_split(
            self._datas[:, 0], self._datas[:, 1], test_size=scale, random_state=12
        )

    #保存模型中间参数
    def save(self, model, path='checkpoint', name=None):
        dirpath = os.path.join(path, name)
        joblib.dump(model, dirpath)

    #验证模型性能
    def performance(self, test, pre):
        mse = mean_squared_error(test, pre)
        print("MSE的值为：", mse)


#测试类
class AlgorithmTest(object):
    def __init__(self, path='checkpoint', name=None):
        #用于加载模型
        dirpath = os.path.join(path, name)
        self.clf = joblib.load(dirpath)

    def run(self, data):   #测试模型
        #改变数据维度
        data = data.reshape(-1, 1)
        pre_data = self.clf.predict(data)
        return pre_data