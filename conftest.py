import pytest
from py._xmlgen import html


def pytest_configure(config):
    # 添加接口地址与项目名称
    config._metadata["项目名称"] = "登特菲CTView V1.0.0"
    config._metadata['接口地址'] = 'http://dentafilm.cn/'
    # 删除Java_Home
    config._metadata.pop("JAVA_HOME")


@pytest.mark.optionalhook
def pytest_html_results_summary(prefix):
    prefix.extend([html.p("所属部门: 研发中心")])
    prefix.extend([html.p("测试人员: 程义军")])


@pytest.mark.hookwrapper
def pytest_runtest_makereport(item):
    outcome = yield
    report = outcome.get_result()
    getattr(report, 'extra', [])
    report.nodeid = report.nodeid.encode("utf-8").decode("unicode_escape")  # 解决乱码


@pytest.mark.optionalhook
def pytest_html_results_table_header(cells):
    cells.pop(-1)  # 删除link列


@pytest.mark.optionalhook
def pytest_html_results_table_row(report, cells):
    cells.pop(-1)  # 删除link列


@pytest.fixture(scope='function')
def func_scope():
    pass


@pytest.fixture(scope='module')
def mod_scope():
    pass


@pytest.fixture(scope='session')
def sess_scope():
    pass


@pytest.fixture(scope='class')
def class_scope():
    print('Connection successful')

    yield

    print('Connection closed')


def pytest_itemcollected(item):
    par = item.parent.obj
    node = item.obj
    pref = par.__doc__.strip() if par.__doc__ else par.__class__.__name__
    suf = node.__doc__.strip() if node.__doc__ else node.__name__
    if pref or suf:
        item._nodeid = ' '.join((pref, suf))


@pytest.fixture(scope='class')
def use_selenium():
    from selenium import webdriver
    chrome_driver = r'C:\Users\a\AppData\Local\Google\Chrome\Application\chromedriver.exe'  # chrome_driver 存放位置
    driver = webdriver.Chrome(executable_path=chrome_driver)
    print('创建浏览器')
    yield driver
    print('关闭浏览器')
    driver.close()
