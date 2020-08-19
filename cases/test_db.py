import pytest


@pytest.fixture()
def db():
    print('数据库连接成功')

    yield

    print('数据库连接关闭')


def search_user(user_id):
    d = {
        '001': 'xiaoming'
    }
    return d[user_id]


def test_search(db):
    # db() # 不需要显式调用 会自动调用
    assert search_user('001') == 'xiaoming'
