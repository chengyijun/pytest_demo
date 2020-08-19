# -*- coding:utf-8 -*-
"""
@author: chengyijun
@contact: cyjmmy@foxmail.com
@file: test_selenium.py
@time: 2020/8/11 14:13
@desc:
"""
import time

import pytest
from selenium.webdriver.common.by import By


@pytest.mark.usefixtures('use_selenium')
class TestSelenium:

    # def setup_class(self):
    #     from selenium import webdriver
    #     chrome_driver = r'C:\Users\a\AppData\Local\Google\Chrome\Application\chromedriver.exe'  # chrome_driver 存放位置
    #     self.driver = webdriver.Chrome(executable_path=chrome_driver)

    def test_selenium(self, use_selenium):
        self.driver = use_selenium  # fixture是不需要显式调用的
        self.driver.get("https://www.baidu.com/")
        self.driver.find_element(By.ID, "kw").send_keys("demo")
        self.driver.find_element(By.ID, "su").click()
        time.sleep(3)

    def test_another(self, use_selenium):
        self.driver = use_selenium
        self.driver.get("https://www.sohu.com/")
        time.sleep(3)
        assert True
    # def teardown_class(self):
    #     self.driver.quit()
