import logging.config
import os
from time import sleep

log_path = './logs'
if not os.path.exists(log_path):
    os.makedirs(log_path)
CONF_LOG = "./log_conf"
logging.config.fileConfig(CONF_LOG);  # 采用配置文件
# print(logging.config.fileConfig(CONF_LOG))
logger = logging.getLogger('applog')

if __name__ == '__main__':
    while True:
        logger.info("Hello ！")
        logger.error("error！")
        sleep(2)