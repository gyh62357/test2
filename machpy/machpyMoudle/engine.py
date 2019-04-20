import read_data
import setting
import importlib
import numpy as np
import algorithm

class QT(object):
    def __init__(self, data=None):
        self._data = data   #用于测试的数据
        self._result = None
    def run(self, file, istrain='y'):
        #执行数据读取模块
        conn = read_data.ReadData()
        datas = conn.read(file)
        conn.close()
        datas = np.array(datas)

        #读取中间件
        #判断某个属性是否存在
        isMiddlers = None
        try:
            middlers = setting.middlers
            isMiddlers = True
        except AttributeError as e:
            isMiddlers = False
        if isMiddlers:
            rank = sorted(middlers.values())
            for r in rank:
                for key, value in middlers.items():
                    if r == value:
                        m_root, m_sub = key.split('.')
                        model = importlib.import_module(m_root)
                        obj = getattr(model, m_sub)(datas)    #反射机制，实例化类
                        obj.process()
                        datas = obj.backData()

        #调用算法阶段
        if istrain == 'y':
            self._result = self.train(datas)
        elif istrain == 'n':
            self._result = self.test_(self._data)
        else:
            print("请输入正确的指示")

        return self._result

    #定义训练阶段
    def train(self, datas):
        alg = algorithm.AlgorithmTrain(datas)
        pre_data = alg.AI()
        return pre_data

    #定义测试阶段
    def test_(self, data):
        alg = algorithm.AlgorithmTest(name='line.m')
        pre_data = alg.run(data)
        return pre_data