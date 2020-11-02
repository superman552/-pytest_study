import logging
import os
import datetime
import time
from logging import handlers

class Log():
    lever_relations = {
        'debug':logging.DEBUG,
        'info':logging.INFO,
        'warning':logging.WARNING,
        'error': logging.ERROR,
        'crit':logging.CRITICAL
    }#日志级别映射


    def __init__(self,filenameall,filenameerr,level='info',when='midnight',backCount=3,fmt='%(asctime)s - %(pathname)s[line:%(lineno)d]'
                                                                            ' - %(levelname)s: %(message)s'):
        self.logger = logging.getLogger()#初始化 logger
        format_str = logging.Formatter(fmt)#设置日志格式
        self.logger.setLevel(self.lever_relations.get(level))#设置日志级别
        sh = logging.StreamHandler()#创建handler，将日志输出到屏幕
        sh.setLevel(logging.INFO)
        sh.setFormatter(format_str)#为handler屏幕指定输出格式
        th_all = handlers.TimedRotatingFileHandler(filename=filenameall, when=when, backupCount=backCount, encoding='utf-8')
        th_all.setLevel(logging.INFO)
        #将日志输出到文件
        # 实例化TimedRotatingFileHandler
        # interval是时间间隔，backupCount是保留文件的个数，如果超过这个个数，就会自动删除，when是间隔的时间单位，单位有以下几种：
        # S 秒 # M 分 # H 小时、 # D 天、 # W 每星期（interval==0时代表星期一） # midnight 每天凌晨
        th_all.setFormatter(format_str)#设置文件日志写入格式
        th_err = handlers.TimedRotatingFileHandler(filename=filenameerr, when=when, backupCount=backCount, encoding='utf-8')
        th_err.setLevel(logging.ERROR)
        self.logger.addHandler(sh) #把对象加到logger里
        self.logger.addHandler(th_all)
        self.logger.addHandler(th_err)

#创建log实例
# day = datetime.datetime.now().strftime('%Y-%m-%d')
log_path = './logs'
if not os.path.exists(log_path):
    os.makedirs(log_path)
filename_all = os.path.join(log_path, 'all.log')
filename_error = os.path.join(log_path, 'error.log')
# filename_all = os.path.join(log_path, '{}all.log'.format(day))
# filename_error = os.path.join(log_path, '{}error.log'.format(day))
log = Log(filename_all,filename_error)



if __name__ == '__main__':

    # while True:
    #     log_all.logger.debug('debug')
    #     log_all.logger.info('info')
    #     log_all.logger.warning('警告')
    #     log_all.logger.error('报错')
    #     log_all.logger.critical('严重')
    #     log_err.logger.info('ces ')
    #     log_err.logger.error('报错')
    #     log_err.logger.critical('严重')
    #     time.sleep(10)
    log.logger.info('info')
    log.logger.error('报错')