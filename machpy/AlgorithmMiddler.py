"""
定义预处理中间件和插值中间件
"""
import numpy as np

#预处理中间件
class ProcessMiddler(object):
    def __init__(self, datas=None):
        self._datas = datas

    def process(self):
        print(111)
        self._datas -= 1

    def backData(self):
        return self._datas


#插值中间件
class CZMiddler(object):
    def __init__(self, datas=None):
        self._datas = datas

    def process(self):
        print(222)
        self._datas += 1

    def backData(self):
        return self._datas