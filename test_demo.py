#/root/python3 python3
import pytest
import allure

@allure.feature("test_pytest")
class TestDemo:
    @allure.story("test1")
    @pytest.fixture(scope='class', autouse=True)
    def test_one(self):
        print('do test1')

    @allure.story("test2")
    def test_two(self):
        print('do test2')
