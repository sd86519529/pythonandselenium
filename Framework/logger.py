import logging
import os.path
import time

'''
此类是日志打印类，封装日志打印工具提供其他类的调用 obj为其他类名
'''


class Logger(object):
    '''
    日志信息类创建后class logger（object），在初始化方法中完成保存日志的路径，日志的级别，调用的文件
    将日志储存到指定文件中等工作内容
    :param obj:
    :return:
    '''

    def __init__(self, obj):
        self.logger = logging.getLogger(obj)  # 使用logging.getLogger传入其他类名称来创建一个logger
        self.logger.setLevel(logging.DEBUG)  # 通过setLeverl方法来设置日志的等级

        '''
        创建好logger后编辑log的储存路径，文件名以时间的形式避免重复
        '''
        log_file = time.strftime('%Y%m%d.%H.%M.%S') + '.log'
        log_name = os.path.abspath('..') + '\logs\\' + log_file

        # 创建一个handler，用于输出到指定文件,并设置其日志等级
        fi = logging.FileHandler(log_name,encoding='utf-8')
        fi.setLevel(logging.INFO)
        # 创建一个handler,用于输出到控制台，并设置其日志等级
        st = logging.StreamHandler()
        st.setLevel(logging .INFO)
        #定义handler的输出格式
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        fi.setFormatter(formatter)
        st.setFormatter(formatter)
        #给日志添加handler
        self.logger.addHandler(fi)
        self.logger.addHandler(st)

    def getlog(self):
        '''
        :return: logger
        '''
        return self.logger






