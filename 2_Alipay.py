import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import random
import warnings
from selenium.common.exceptions import NoSuchElementException
import ctypes
import pyperclip
from selenium.webdriver.chrome.service import Service
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys

# 复制文本
def copy_text(text):
    pyperclip.copy(text)


# 设置控制台标题
def set_console_title(title):
    ctypes.windll.kernel32.SetConsoleTitleW(title)

set_console_title("𝓢𝓬𝓻𝓲𝓹𝓽 𝓑𝔂 𝓕𝓾𝔁𝓲𝓾")
warnings.filterwarnings('ignore')

# 随机生成IGN
def randomIGN(length=16, insert_char='_'):
    base_Str = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890'
    random_str = ''
    for i in range(length):
        if i >0 and i % 3 == 0:
           random_str += insert_char
        random_str += base_Str[random.randint(0, (len(base_Str) - 1))]
    return random_str


# Old Ramdom username
def randomUsername(length=16):
    base_Str = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890'
    random_str = ''
    for i in range(length):
        random_str += base_Str[random.randint(0, (len(base_Str) - 1))]
    return random_str

# Logo
print('''

   _____         ____                      _______           _     
  / ____|       |___ \                    |__   __|         | |    
 | (___    __ _   __) | _   _  _ __  __ _    | |  ___   ___ | |__  
  \___ \  / _` | |__ < | | | || '__|/ _` |   | | / _ \ / __|| '_ \ 
  ____) || (_| | ___) || |_| || |  | (_| | _ | ||  __/| (__ | | | |
 |_____/  \__,_||____/  \__,_||_|   \__,_|(_)|_| \___| \___||_| |_|
                                                                   
                                                                   

[+]一个简单的自动购买微软XGP 自动设置我的世界IGN 使用支付宝自动微软退款的Python脚本。
[Update Log]修复需要手动点击支付宝的bug
[Version]当前版本 V2 0620 Debug
''')

# 输入邮箱密码是否已经注册xbox
acc = input('Account:')
parts = acc.split("----")
Email = parts[0]
Password = parts[1]
Xbox = input("Xbox:")
Alipay_username = input('AlipayUsername:')
Alipay_password = input('AlipayPassword:')
Alipay_PayPassword = input('AlipayPayPassword:')
Xbox_User = 'Sa3ura' + randomUsername(5)
IGN = randomIGN(8)

# 设置 Chrome 浏览器驱动
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--incognito")  # 使用无痕模式
chrome_options.add_argument("--disable-browser-side-navigation")  # 禁用浏览器侧边导航
chrome_options.add_argument("--disable-gpu")  # 禁用 GPU 加速
chrome_options.add_argument("--disable-features=TranslateUI")  # 禁用翻译功能
chrome_options.add_argument("--disable-popup-blocking")  # 禁用弹出窗口阻止
chrome_options.add_argument("--disable-prompt-on-repost")  # 禁用重新提交时的提示
chrome_options.add_argument("--disable-blink-features=AutomationControlled") # 禁用 Chrome 浏览器中的自动化控制特性
chrome_options.add_argument('--no-sandbox') # 以最高权限运行
chrome_options.add_argument('blink-settings=imagesEnabled=false') # 不加载图片
# 添加excludeSwitches参数，禁用调试信息
chrome_options.add_experimental_option('excludeSwitches', ['enable-automation'])
chrome_options.add_experimental_option('useAutomationExtension', False)
# 创建Edge浏览器对象
service = Service('chromedriver.exe')
driver = webdriver.Chrome(service=service,options=chrome_options)
action_chains = ActionChains(driver)
# Selenium在打开任何页面之前，先运行这个Js文件。
# 读取文件
with open('stealth.min.js', 'r') as f:
    js = f.read()
driver.execute_cdp_cmd('Page.addScriptToEvaluateOnNewDocument', {'source': js})

# 打开购买界面
print('[Debugger]即将打开浏览器并自动购买......')
driver.get('https://www.xbox.com/zh-hk/games/store/pc-game-pass/cfq7ttc0kgq8/0002?rtc=1')
time.sleep(8)
join_button = driver.find_element(By.XPATH,'//button[@aria-label="加入 PC Game Pass。每月 HK$29.00"]').click()
time.sleep(6)
# 输入邮箱
print('[Debugger]即将自动输入邮箱密码登录......')
input_email = driver.find_element(By.NAME,'loginfmt').send_keys(Email)
# 点击下一步
next_button = driver.find_element(By.ID,'idSIButton9').click()
time.sleep(2)
# 输入密码
input_pwd = driver.find_element(By.NAME,'passwd').send_keys(Password)
# 点击登录
login_button = driver.find_element(By.ID,'idSIButton9').click()
time.sleep(2)
# 点击保持登录状态
try:
  keep_login_button = driver.find_element(By.ID,'idSIButton9').click()
  time.sleep(10)
except NoSuchElementException:
   skip_button = driver.find_element(By.ID,'iShowSkip').click()
   time.sleep(5)
   keep_login_button = driver.find_element(By.ID,'idSIButton9').click()
   time.sleep(5)
   cancel_button_1 = driver.find_element(By.ID,'iCancel').click()
   time.sleep(10)
# 输入Xbox用户名
if(Xbox == ''):
  print('[Debugger]即将自动设置Xbox用户名......')
  input_Xbox_username = driver.find_element(By.ID,'create-account-gamertag-input').send_keys(Xbox_User)
  time.sleep(3)
# 点击开始按钮
  start_button = driver.find_element(By.ID,'inline-continue-control').click()
  time.sleep(28)
  print('[Debugger]Xbox用户名为:'+Xbox_User)
# 点击下一步按钮
else:
  time.sleep(18)
next_button_2 = driver.find_element(By.XPATH,'//button[@aria-label="加入 PC Game Pass。每月 HK$29.00"]').click()
time.sleep(8)
# 添加付款方式
print('[Debugger]即将自动添加支付宝付款......')
driver.switch_to.frame('purchase-sdk-hosted-iframe')
add_payment_button = driver.find_element(By.XPATH, '//button[@class="primary--DXmYtnzQ base--kY64RzQE"]').click()
time.sleep(3)
# 选择PayPal或Alipay支付
eWallet_button = driver.find_element(By.ID,'displayId_ewallet').click()
time.sleep(1)
# 选择支付宝支付
Alipay_button = driver.find_element(By.ID,'displayId_ewallet_alipay_billing_agreement').click()
time.sleep(2)
# 点击下一步按钮
next_button_3 = driver.find_element(By.ID,'pidlddc-button-saveNextButton').click()
time.sleep(5)
# 登入支付宝
alipay_login_button = driver.find_element(By.ID,'pidlddc-hyperlink-alipayQrCodeChallengeRedirectionLink').click()
time.sleep(10)
# 找到并切换至支付宝框架
driver.switch_to.window(driver.window_handles[1])
alipay_iframe = driver.find_element(By.TAG_NAME,'iframe')
driver.switch_to.frame(alipay_iframe)
# 点击输入账号密码登录
online_login_button = driver.find_element(By.XPATH, '//a[@class="qrcode-target  qrcode-target-hide "]').click()

alipay_acc = driver.find_element(By.ID,'J-input-user')
action_chains.move_to_element(alipay_acc).click().perform()
Alipay_account = Alipay_username
for char in Alipay_account:
    alipay_acc.send_keys(char)
    time.sleep(0.2)


alipay_pwd = driver.find_element(By.ID,'password_rsainput')
action_chains.move_to_element(alipay_pwd).click().perform()
Alipay_pwd = Alipay_password
for char in Alipay_pwd:
    alipay_pwd.send_keys(char)
    time.sleep(0.2)
alipay_pwd.send_keys(Keys.ENTER)
time.sleep(5)
# 输入支付密码并提交
alipay_paypwd = driver.find_element(By.NAME,'payPassword_rsainput').send_keys(Alipay_PayPassword)
time.sleep(1)
alipay_pay_submit = driver.find_element(By.ID,'J_submit').click()
time.sleep(8)
driver.close()
# 点击继续
driver.switch_to.window(driver.window_handles[0])
driver.switch_to.frame('purchase-sdk-hosted-iframe')
continue_button = driver.find_element(By.ID,'pidlddc-button-alipayContinueButton').click()
time.sleep(3)
# 输入城市 & 地址
input_city = driver.find_element(By.ID,'city').send_keys('1')
input_address = driver.find_element(By.ID,'address_line1').send_keys('1')
# 点击储存按钮
save_button = driver.find_element(By.ID,'pidlddc-button-saveButton').click()
time.sleep(12)
# 点击订阅按钮
print('[Debugger]即将为您订阅Xbox Game Pass PC......')
subscription_button = driver.find_element(By.XPATH, '//button[@class="primary--DXmYtnzQ base--kY64RzQE"]').click()
driver.switch_to.default_content()
# 等待购买成功
time.sleep(20)
print('[Debugger]购买成功!')
# 打开官网设置ID
print('[Debugger]即将跳转官网为您自动设置ID.....')
driver.get('https://www.minecraft.net/en-us/msaprofile/mygames/editprofile')
time.sleep(10)
#点击登录按钮
home_login_button = driver.find_element(By.CSS_SELECTOR,"a[aria-label='Sign in with Microsoft account']").click()
time.sleep(15)
# 输入随机ID
input_ID = driver.find_element(By.CSS_SELECTOR,"input[name='profileName']").send_keys(IGN)
# 确认
set_ID_button = driver.find_element(By.CSS_SELECTOR,"button[aria-label='Set up your Profile Name']").click()
time.sleep(6)
print('[Debugger]ID设置成功! ID为:' + IGN)
# 打开微软退款
print('[Debugger]即将打开退款链接并自动退款......')
driver.get('https://account.microsoft.com/services/pcgamepass/cancel?fref=billing-cancel&lang=en-US')
time.sleep(8)
try:
  next_button_2 = driver.find_element(By.ID,'id__0').click()
  time.sleep(25)
  cancel_button = driver.find_element(By.CSS_SELECTOR,"button[aria-label='Cancel subscription']").click()
# 点击保持登录
except NoSuchElementException:
# 点击取消订阅按钮
  time.sleep(30)
  cancel_button = driver.find_element(By.CSS_SELECTOR,"button[aria-label='Cancel subscription']").click()
#选择立即退款按钮
refund_button = driver.find_element(By.CSS_SELECTOR,"input[aria-label='Cancel now and get refund']").click()
#点击取消订阅按钮
cancel_button = driver.find_element(By.ID,'cancel-select-cancel').click()
time.sleep(15)
print('[Debugger]已经成功退款！')
print('账号信息:' + Email + '----' + Password + '----' + IGN)
copy_text(Email + '----' + Password + '----' + IGN)
print('即将自动删除支付宝支付方式...')
driver.get('https://account.microsoft.com/billing/payments?fref=home.drawers.payment-options.manage-payment')
time.sleep(5)
remove_payment_btn = driver.find_element(By.CSS_SELECTOR,"button[aria-label='Remove Alipay']").click()
remove_payment_btn2 = driver.find_element(By.XPATH, '//button[@class="ms-Button ms-Button--primary root-290"]').click()
time.sleep(3)
close_btn = driver.find_element(By.XPATH, '//button[@class="ms-Button ms-Button--primary root-290"]')
time.sleep(3)
driver.quit()
input('按回车键退出脚本。')