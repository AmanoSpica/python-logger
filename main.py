from logger import Logger, child_logger

# parent logger
logger = Logger('main', level='DEBUG')

logger.debug('This is a debug message')
logger.info('This is an info message')
logger.warning('This is a warning message')
logger.error('This is an error message')
logger.critical('This is a critical message')

# child logger
child_logger = child_logger('main', 'child')
child_logger.debug('This is a debug message')
child_logger.info('This is an info message')
child_logger.warning('This is a warning message')
child_logger.error('This is an error message')
child_logger.critical('This is a critical message')