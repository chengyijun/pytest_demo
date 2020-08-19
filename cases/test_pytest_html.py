import time

import pytest


def login(username, password):
    """模拟登录"""
    user = "linux超"
    pwd = "linux超哥"
    if user == username and pwd == password:
        return {"code": 1001, "msg": "登录成功", "data": None}
    else:
        return {"code": 1000, "msg": "用户名或密码错误", "data": None}


test_data = [
    # 测试数据
    {
        "case": "用户名正确, 密码正确",
        "user": "linux超",
        "pwd": "linux超哥",
        "expected": {"code": 1001, "msg": "登录成功", "data": None}
    },
    {
        "case": "用户名正确, 密码为空",
        "user": "linux超",
        "pwd": "",
        "expected": {"code": 1000, "msg": "用户名或密码错误", "data": None}
    },
    {
        "case": "用户名为空, 密码正确",
        "user": "",
        "pwd": "linux超哥",
        "expected": {"code": 1000, "msg": "用户名或密码错误", "data": None}
    },
    {
        "case": "用户名错误, 密码错误",
        "user": "linux",
        "pwd": "linux",
        "expected": {"code": 1000, "msg": "用户名或密码错误222", "data": None}
    }
]

# 改变输出结果
ids = [
    "测试：{}->[用户名:{}-密码:{}-预期:{}]".
        format(data["case"], data["user"], data["pwd"], data["expected"]) for data in test_data
]


@pytest.mark.usefixtures('class_scope')
class TestLogin(object):

    @pytest.mark.parametrize("data", test_data, ids=ids)
    def test_login(self, data):
        result = login(data["user"], data["pwd"])
        assert result == data["expected"]

    @pytest.mark.skip(reason='api已经废弃')
    def test_unfinished(self):
        assert 1 == 1

    def connect(self, a, b):
        print('这是log信息')
        raise Exception('类型错误哦')

    def test_raises(self):
        with pytest.raises(TypeError) as e:
            self.connect('localhost', '6379')
        exec_msg = e.value.args[0]
        assert exec_msg == 'port type must be int'

    @pytest.mark.parametrize('student', ['abel', 'rox', 'tank'])
    def test_name(self, student):
        time.sleep(1)
        assert student == 'tank'
