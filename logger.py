import datetime
import logging
import logging.handlers

import colorlog


def namer_app(name):
    parts = name.rsplit('/', 1).rsplit('\\', 1)
    date_str = parts[1].split('.')[-1]
    date = datetime.datetime.strptime(date_str, '%Y-%m-%d').strftime('%Y%m%d')
    archive_file_name = f"{parts[0]}/app_{date}.log"
    return archive_file_name

def namer_error(name):
    parts = name.rsplit('/', 1).rsplit('\\', 1)
    date_str = parts[1].split('.')[-1]
    date = datetime.datetime.strptime(date_str, '%Y-%m-%d').strftime('%Y%m%d')
    archive_file_name = f"{parts[0]}/error_{date}.log"
    return archive_file_name



def Logger(root_logger_name: str, level: str = 'INFO') -> logging.Logger:
    logger = logging.getLogger(root_logger_name)
    logger.setLevel(level)

    # StreamHandler
    stdout_handler = logging.StreamHandler()
    stdout_formatter = colorlog.ColoredFormatter(
        '\033[30m%(asctime)s\033[0m  \033[35m %(threadName)10s / %(name)10s\033[0m%(log_color)s%(levelname)9s%(reset)s  %(message)s    [%(filename)s:%(lineno)d]',
        datefmt='%Y-%m-%d %H:%M:%S',
        log_colors={
            'DEBUG': 'cyan',
            'INFO': 'green',
            'WARNING': 'yellow',
            'ERROR': 'red',
            'CRITICAL': 'bold_red',
        }
    )
    stdout_handler.setFormatter(stdout_formatter)
    logger.addHandler(stdout_handler)


    file_format = '%(asctime)s [ %(name)10s / %(threadName)10s ] %(levelname)8s  %(message)s   [%(filename)s:%(lineno)d]'

    # ErrorHandler
    stderr_file_handler = logging.handlers.TimedRotatingFileHandler(
        filename='logs/error.log',
        when='midnight',
        interval=1,
        encoding='utf-8',
        backupCount=0
    )
    stderr_file_handler.setLevel(logging.ERROR)
    stderr_file_handler.setFormatter(logging.Formatter(file_format, datefmt='%Y-%m-%d %H:%M:%S'))
    stderr_file_handler.namer = namer_error
    logger.addHandler(stderr_file_handler)

    # FileHandler
    file_handler = logging.handlers.TimedRotatingFileHandler(
        filename='logs/app.log',
        when='midnight',
        interval=1,
        encoding='utf-8',
        backupCount=0
    )
    file_handler.setFormatter(logging.Formatter(file_format, datefmt='%Y-%m-%d %H:%M:%S'))
    file_handler.namer = namer_app
    logger.addHandler(file_handler)

    return logger


def child_logger(root_logger_name: str, child_name: str) -> logging.Logger:
    logger = logging.getLogger(root_logger_name).getChild(child_name)
    return logger
