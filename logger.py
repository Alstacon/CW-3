import logging

logger = logging.getLogger('logger')
logger.setLevel(logging.INFO)
file_handler = logging.FileHandler('./logs/api.log.txt', encoding='utf-8')
formatter_log = logging.Formatter('%(asctime)s [%(levelname)s] %(message)s')
file_handler.setFormatter(formatter_log)
logger.addHandler(file_handler)