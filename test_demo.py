#/root/python3/bin python3
#coding:utf-8
import sys
sys.path.append('/root/python3/lib/python3.7/site-packages')

import pytest
import allure

@allure.feature("test_pytest")
class TestCase:
    @allure.story("test1")
    @pytest.fixture(scope='class', autouse=True)
    def test_one(self):
        assert 1 == 1
        print("do test1")

    @allure.story("test2")
    def test_two(self):
        assert 2 == 2
        print("do test2")

if __name__ == '__main__':
    pytest.main(['/root/python3/project/test_demo.py'])