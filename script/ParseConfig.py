# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     ParseConfig
   Description :
   Author :       WWQ
   date：          2020/4/4
-------------------------------------------------
   Change Activity:
                   2020/4/4:
-------------------------------------------------
"""
__author__ = 'WWQ'
from configparser import ConfigParser

class HandleConf(ConfigParser):
    '''
    继承configParser类，添加一些方法
    '''
    def __init__(self):
        super().__init__()
        self.file = "../config/testinfo.conf"
        self.read(self.file, encoding="utf-8")

    def __call__(self, Section="DEFAULT", Option=None, is_eval=False, is_bool=False):
        '''
        :param Section:区域名，不传值时默认获取DEFAULT区域下所有信息，返回字典
        :param Option: 操作名, 为空时默认获取改区域下所有信息，返回字典
        :param is_eval: 是否使用eval()方法来解析值的类型，默认不使用
        :param is_bool: 是否将值解析为布尔类型，默认不使用
        :return:
        '''
        if Option is None:
            return dict(self[Section])
        if isinstance(is_bool, bool):
            if is_bool:
                return self.getboolean(section=Section, option=Option)
        else:
            raise ValueError("The variable is_bool must be a bool !")
        data = self.get(section=Section, option=Option)
        if data.isdigit():  # 判断data是否为整数
            return int(data)
        try:
            return float(data)
        except ValueError:
            pass
        if isinstance(is_eval, bool):
            if is_eval:
                return eval(data)
        else:
            raise ValueError("The variable is_eval must be a bool !")
        return data


if __name__ == '__main__':
    conf = HandleConf()
    print(conf())
    print(conf(Section="TestInfo"))
    print(conf(Section="Excel", Option="is_list"))
    print(conf(Section="Excel", Option="is_list", is_eval=True))
    print(conf(Option="more_info", is_bool=True))

