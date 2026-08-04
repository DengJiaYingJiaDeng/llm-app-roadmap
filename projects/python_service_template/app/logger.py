# Python 标准库日志模块,用来统一打印规范日志，代替零散的print
import logging

def get_logger(name:str):

    #创建/获取一个Logger日志对象
    logger = logging.getLogger(name)

    #设置日志级别：INFO，只输出等级大于等于INFO的日志
    logger.setLevel(
        logging.INFO
    )

    # StreamHandler() 日志输出到控制台终端
    handler = logging.StreamHandler()

    formatter = logging.Formatter(
        "%(asctime)s %(levelname)s %(message)s"
    )

    # 把格式模板绑定给处理器，让控制台按照上面的格式输出
    handler.setFormatter(
        formatter
    )

    # 将处理器挂在到logger对象
    logger.addHandler(handler)

    return logger