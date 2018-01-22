import xlrd
import configparser
import os


class ExcleUtile(object):
    '''
    此类为excle读取数据并封装为列表加字典的格式返回，方便ddt数据驱动调用
    excle第一行为key，之后为key对应的value，每一个excle只能读取第一张sheet
    '''

    def __init__(self):
        '''
        初始化excle,传入exclepath和sheetname
        '''
        Config_path = os.path.abspath('..') + '\Config\config.ini'
        config = configparser.ConfigParser()
        config.read(Config_path, encoding='utf-8')
        exclename = config.get('Exlce', 'excleName')
        exclepath = os.path.abspath('..') + '\ExcleDdt\\' + exclename
        self.data = xlrd.open_workbook(exclepath, encoding_override='utf-8')
        self.table = self.data.sheet_by_index(0)
        # 获取第一行的值作为key
        self.keys = self.table.row_values(0)
        # 获取总行数
        self.rowNumber = self.table.nrows
        # 获取总列数
        self.colNumber = self.table.ncols

    def dict_data(self):
        '''
        获取excle表数据方法
        '''
        if self.rowNumber < 1:
            print('excle行数小于1行，请重新定义数据')
        else:
            s = []
            j = 1
            for i in range(self.rowNumber - 1):
                # 拿到第二行对应的values值
                dic = {}
                values = self.table.row_values(j)
                for k in range(self.colNumber):
                    dic[self.keys[k]] = values[k]
                    s.append(dic)
                j += 1
            return s


if __name__ == '__main__':
    ex = ExcleUtile()
    print(ex.dict_data())
