import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import random
import warnings
from selenium.common.exceptions import NoSuchElementException
import ctypes
import pyperclip

# 复制文本
def copy_text(text):
    pyperclip.copy(text)


# 设置控制台标题
def set_console_title(title):
    ctypes.windll.kernel32.SetConsoleTitleW(title)

set_console_title("𝓢𝓬𝓻𝓲𝓹𝓽 𝓑𝔂 𝓕𝓾𝔁𝓲𝓾")
warnings.filterwarnings('ignore')

# 随机生成Xbox用户名 格式为'Sa3ura + Randomchar()'
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
                                                                   
                                                                   

[+]一个简单的自动购买微软XGP 自动设置我的世界IGN 使用支付宝自动微软退款的脚本。
[Update Log]优化速度减少支付出现问题
[Version]当前版本 B230524 DEBUG
''')

# 输入邮箱密码是否已经注册xbox
acc = input('Account:')
parts = acc.split("----")
Email = parts[0]
Password = parts[1]
Xbox = input("未注册Xbox请直接回车:")
Xbox_User = 'Sa3ura' + randomUsername(6)
IGN = randomUsername(10)

# 设置Edge浏览器驱动
edge_options = webdriver.EdgeOptions()
edge_options.use_chromium = False
edge_options.add_experimental_option('useAutomationExtension', False)
edge_options.add_argument('--inprivate')

# 添加excludeSwitches参数，禁用调试信息
edge_options.add_experimental_option('excludeSwitches', ['enable-automation', 'enable-logging'])


# 创建Edge浏览器对象
driver = webdriver.Edge('msedgedriver.exe',options=edge_options)

# 打开微软账户管理页面
print('[Debugger]即将打开浏览器并自动购买......')
driver.get('https://www.xbox.com/zh-HK/xbox-game-pass#join')
time.sleep(5)
# 在页面上查找29港币的PC Game pass
join_button = driver.find_element(By.CSS_SELECTOR, "a[data-bi-source='CFQ7TTC0KGQ8']").click()
time.sleep(5)
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
  time.sleep(8)
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
  time.sleep(25)
  print('[Debugger]Xbox用户名为:'+Xbox_User)
# 点击下一步按钮
else:
  time.sleep(15)
next_button_2 = driver.find_element(By.XPATH,'//button[@aria-label="下一步"]').click()
time.sleep(8)
# 添加付款方式
print('[Debugger]即将自动添加支付宝付款......')
driver.switch_to.frame('purchase-sdk-hosted-iframe')
add_payment_button = driver.find_element(By.XPATH, '//button[@class="primary--DXmYtnzQ base--kY64RzQE"]').click()
time.sleep(5)
# 选择PayPal或Alipay支付
eWallet_button = driver.find_element(By.ID,'displayId_ewallet').click()
time.sleep(1)
# 选择支付宝支付
Alipay_button = driver.find_element(By.ID,'displayId_ewallet_alipay_billing_agreement').click()
time.sleep(3)
# 点击下一步按钮
next_button_3 = driver.find_element(By.ID,'pidlddc-button-saveNextButton').click()
time.sleep(1)
# 等待扫码
print('[Debugger]等待支付宝扫码...')
time.sleep(25)
# 点击继续
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
time.sleep(18)
print('[Debugger]购买成功!')
# 打开官网设置ID
print('[Debugger]即将跳转官网为您自动设置ID.....')
driver.get('https://www.minecraft.net/en-us/msaprofile/mygames/editprofile')
time.sleep(10)
#点击登录按钮
home_login_button = driver.find_element(By.CSS_SELECTOR,"a[aria-label='Sign in with Microsoft account']").click()
time.sleep(13)
# 输入随机ID
input_ID = driver.find_element(By.CSS_SELECTOR,"input[name='profileName']").send_keys(IGN)
# 确认
set_ID_button = driver.find_element(By.CSS_SELECTOR,"button[aria-label='Set up your Profile Name']").click()
time.sleep(6)
print('[Debugger]ID设置成功! ID为:' + IGN)
# 打开微软退款
print('[Debugger]即将打开退款链接并自动退款......')
driver.get('https://account.microsoft.com/services/pcgamepass/cancel?fref=billing-cancel&lang=en-US')
time.sleep(20)
try:
  cancel_button = driver.find_element(By.CSS_SELECTOR,"button[aria-label='Cancel subscription']").click()
# 点击保持登录
except NoSuchElementException:
# 点击取消订阅按钮
  time.sleep(5)
  next_button_2 = driver.find_element(By.ID,'id__0').click()
  time.sleep(25)
  cancel_button = driver.find_element(By.CSS_SELECTOR,"button[aria-label='Cancel subscription']").click()
#选择立即退款按钮
refund_button = driver.find_element(By.CSS_SELECTOR,"input[aria-label='Cancel now and get refund']").click()
#点击取消订阅按钮
cancel_button = driver.find_element(By.ID,'cancel-select-cancel').click()
time.sleep(15)
print('[Debugger]已经成功退款！')
print('账号信息:' + Email + '----' + Password + '----' + IGN)
copy_text(Email + '----' + Password + '----' + IGN)
print('已经为您复制好。')
input('按回车键退出脚本。')