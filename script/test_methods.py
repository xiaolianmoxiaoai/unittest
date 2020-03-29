# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     test_methods
   Description :
   Author :       WWQ
   date：          2020/3/29
-------------------------------------------------
   Change Activity:
                   2020/3/29:
-------------------------------------------------
"""
__author__ = 'WWQ'
import unittest
from script.get_data import GetExcelDatas
from ddt import ddt, data

@ddt
class TestCase(unittest.TestCase):
    datas = GetExcelDatas(file="../testcase/测试用例.xlsx", sheet_name="乘法运算")
    data_lsit = datas()
    @data(*data_lsit)
    def test_multi(self, test_case):
    # test_case = data_named_tuple.pop(0)
        result = test_case.first_num * test_case.second_num
        try:
            self.assertEqual(test_case.expect, result, msg="测试{}失败".format(test_case.test_case))
        except Exception as e:
            print("测试{}失败{}".format(test_case.test_case, e))
            # datas.write_result(test_case.test_id, test_result=result, result="Failure")
        else:
            print("{}执行结果为{}".format(test_case.test_case, "PASSED"))
           #  datas.write_result(test_case.test_id, test_result=result, result="PASSED")

