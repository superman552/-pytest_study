# -*- coding: GBK -*-
import logging.config
import os

log_path = '../logs'
if not os.path.exists(log_path):
    os.makedirs(log_path)
CONF_LOG = "../log.conf"
logging.config.fileConfig(CONF_LOG);  # 采用配置文件
# print(logging.config.fileConfig(CONF_LOG))
logger = logging.getLogger('applog')


if __name__ == '__main__':
    logger.info("Hello ！")
    logger.error("ss！")