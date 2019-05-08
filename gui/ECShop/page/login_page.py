"""
1.学习目标
    掌握page类的封装方法
2.操作步骤
    2.1 page.py文件继承Base类
    2.2 封装表现层
    2.3 封装操作层
    
3.需求
    对ECShop登录页面进行封装
4. 总结
    
"""
from common.base import Base
from common.base import open_browser

login_url = "http://ecshop.itsoso.cn/user.php"
class LoginPage(Base):
    """
    封装表现层__制作定位器
    """
    username_loc = ("name","username")# 用户名输入框
    password_loc = ("name","password")# 密码输入框
    remember_loc = ("id","remember")# 记住密码
    submit_loc = ("name","submit") # 立即登录按钮
    password_question_loc = ("link text","密码问题")# 找回密码--密码问题链接
    email_loc = ("link text","邮件")# 找回密码--邮件链接
    message_loc = ("link text","短信验证")# 找回密码--短信验证链接
    register_loc = ("css selector","a>img")# 立即注册按钮
    home_page_loc = ("link text","首页")# 首页链接

    """
    封装操作层:每一个元素的操作方法都写成一个方法
    """
    def input_username(self,username):
        """输入用户名"""
        self.send_keys(self.username_loc,username)
    def input_password(self,password):
        """输入密码"""
        self.send_keys(self.password_loc,password)
    def click_submit(self):
        """点击登录"""
        self.click(self.submit_loc)
    def click_remeber(self):
        """点击记住密码"""
        self.click(self.remember_loc)

if __name__ == '__main__':
    driver = open_browser()
    login = LoginPage(driver)
    login.open_url(login_url)
    login.input_username("1234596")
    login.input_password("123456")
    login.close_browser()
