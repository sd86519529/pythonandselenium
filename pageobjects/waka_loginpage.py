from Framework.base_page import BasePage


class WakaLoginPage(BasePage):
    '''
    此类为页面类，通过每个页面封装成类来进行元素的定位器和流程写函数和变量
    在实际工作中根据不同的业务逻辑进行参考变换，不要一成不变的使用POM思想
    '''
    # 定位器，定位页面的元素内容
    username_locator = ('id', 'username')  # 输入账号框
    password_locator = ('id', 'password')  # 输入密码框
    submit_locator = ('id', 'div_login_btn')  # 登录按钮框
    registration_locator = ('css selector', '#lose_password > span:nth-child(2)')  # 用户注册框
    Forget_locator = ('css selector', '#a_to_register > span:nth-child(2)')  # 忘记密码框
    locator_text = ('link text', '退出')

    def Login(self, username, password):
        '''
        登录流程
        :param username:
        :param password:
        :return:
        '''
        self.send_keys(self.username_locator, username)
        self.send_keys(self.password_locator, password)
        self.click(self.submit_locator)
