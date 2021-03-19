import logging
import logging.handlers

def logger_init(name='', log_path='../log/index.log'):
  logger = logging.getLogger(name)
  logger.setLevel(logging.DEBUG)
  rotation_handler = logging.handlers.RotatingFileHandler(
      log_path, encoding='utf-8',
      maxBytes=50*1000,
      backupCount=10,
    )
  rotation_handler.setLevel(logging.DEBUG)
  formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(filename)s - %(name)s - %(funcName)s - %(message)s')
  rotation_handler.setFormatter(formatter)
  logger.addHandler(rotation_handler)
  return logger
