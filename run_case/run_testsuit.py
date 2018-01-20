import unittest
import os, time
import HTMLTestRunner

case_path = os.path.join(os.path.abspath('..'), 'test_suit')
report_path = os.path.join(os.path.abspath('..'), 'objectreport')


def add_case():
    '''
    加载所有用例使用descover方法
    '''
    descover = unittest.defaultTestLoader.discover(case_path,
                                                   pattern='test*.py',
                                                   top_level_dir=None)
    return descover


def runner_all(descover, report_path):
    '''
    执行所有用例，传入descover和测试报告存储的路径，测试报告使用第三方插件
    '''
    now = time.strftime('%Y%m%d.%H.%M.%S') + '.html'  # 建立一个时间戳保证报告名字不会重复
    report_name = os.path.join(report_path, now)
    '''
    创建一个文件传入文件名，使用第三方插件做成报告执行descover
    '''
    with open(report_name, 'wb') as fb:
        runner = HTMLTestRunner.HTMLTestRunner(stream=fb,
                                               title='自动化测试报告结果如下：',
                                               description='用例执行情况：')
        runner.run(descover)


if __name__ == '__main__':
    discover = add_case()
    runner_all(discover, report_path)
