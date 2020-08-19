# import time
# from selenium import webdriver
# from selenium.webdriver.common.by import By
#
# chrome_driver = r'C:\Users\a\AppData\Local\Google\Chrome\Application\chromedriver.exe'  # chrome_driver 存放位置
# driver = webdriver.Chrome(executable_path=chrome_driver)
# driver.get("https://www.baidu.com/")
# driver.find_element(By.ID, "kw").send_keys("demo")
# driver.find_element(By.ID, "su").click()
# time.sleep(3)
# driver.quit()

# with open('./icsap.json', 'r', encoding='utf-8') as f:
#     json_str = f.read()
#
# rep = re.compile(r'{{Host}}')
# sss = re.sub(rep, '127.0.0.1', json_str)
#
# with open('./icsap_replaced.json', 'w', encoding='utf-8') as f:
#     f.write(sss)
#
# print(sss)
import re

s1 = '就立12即立333即"hello abel"'

search = re.search(r'(?P<nums>\d+).*?(?P<co>\d+)', s1)
print(search.group('nums'))
print(search.group('co'))
print(search.group())

s2 = re.sub(r'(?P<nums>\d+).*?(?P<co>\d+)', r'\g<nums>', s1)
print(s2)
