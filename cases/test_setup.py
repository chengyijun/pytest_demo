# -*- coding:utf-8 -*-
"""
@author: chengyijun
@contact: cyjmmy@foxmail.com
@file: test_setup.py
@time: 2020/8/11 9:40
@desc:
"""
import pytest


@pytest.mark.usefixtures('class_scope')
class TestNews:
    A = 10

    def setup_class(self):
        print('我是初始化方法')
        self.A = 20

    def teardown_class(self):
        print('我是析构方法')

    def test_abc(self):
        print('test_abc')
        assert self.A == 1

    def test_deg(self):
        print('test_deg')
        assert 1 == 1
