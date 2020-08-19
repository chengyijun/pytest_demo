# -*- coding:utf-8 -*-

import pytest


def main():
    pytest.main('cases --html=测试报告.html --self-contained-html'.split())


if __name__ == '__main__':
    main()
