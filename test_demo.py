# -*- coding: utf-8 -*-
# @Time    : 2021/12/14 15:55
# @Author  : Tom
# @Email   : 850156124@qq.com
# @File    : test_demo.py
# @Software: PyCharm
import pytest
import allure

@allure.feature("test1")
class TestDemo:
    @pytest.fixture(scope='class', autouse=True)
    def test_one(self):
        print('do test1')

    @allure.story("test2")
    def test_two(self):
        print('do test2')
