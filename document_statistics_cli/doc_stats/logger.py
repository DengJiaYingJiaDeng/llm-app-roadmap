import logging


def setup_logger() -> logging.Logger:
    """
    创建并返回项目使用的 logger。

    logger 可以理解为比 print 更工程化的输出方式。

    它可以区分：
    - INFO：普通运行信息
    - WARNING：警告
    - ERROR：错误
    """

    # 获取一个名字叫 document_statistics_cli 的 logger
    logger = logging.getLogger(
        "document_statistics_cli"
    )

    # 如果 logger 已经有 handler，
    # 说明已经初始化过了，直接返回。
    #
    # 这样可以避免重复调用 setup_logger()
    # 后一条日志被打印多次。
    if logger.handlers:
        return logger

    # 设置最低日志等级。
    # INFO 表示 INFO / WARNING / ERROR 都会显示。
    logger.setLevel(logging.INFO)

    # StreamHandler 默认把日志输出到终端。
    handler = logging.StreamHandler()

    # 定义日志显示格式。
    formatter = logging.Formatter(
        "%(asctime)s | %(levelname)s | %(message)s"
    )

    # 把格式应用到 handler
    handler.setFormatter(formatter)

    # 再把 handler 添加到 logger
    logger.addHandler(handler)

    return logger