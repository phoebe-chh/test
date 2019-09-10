import time

from selenium import webdriver

# 加启动配置
option = webdriver.ChromeOptions()
option.add_argument('disable-infobars')
option.add_argument('disable-infobars')
# 打开chrome浏览器
driver = webdriver.Chrome(chrome_options=option)
driver.get("https://www.baidu.com/")
driver.set_window_size(1024, 700)
time.sleep(5)
driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
print(driver.title)