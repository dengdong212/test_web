import unittest
from common.base import open_browser
from scripts.login_script import LoginScript
from common.operation_excel import OperationExcel
from common.base import Base
import ddt
# 准备测试数据
oper_excel = OperationExcel('./data/test_data.xlsx')
test_data = oper_excel.get_data_info()

@ddt.ddt
class TestLogin(unittest.TestCase):
    def setUp(self):
        """打开浏览器进入登录页面"""
        self.driver = open_browser()
        self.login = LoginScript(self.driver)
        self.base = Base(self.driver)
    @ddt.data(*test_data)
    def test_login(self,data):
        """登录不记住密码"""
        # 登录流程
        self.login.login_flow(data['username'],data['password'])
        # 验证登录是否成功
        result = self.login.is_login_success(data['username'])
        self.assertEqual(result,data['expect'])
    def tearDown(self):
        self.base.close_browser()




