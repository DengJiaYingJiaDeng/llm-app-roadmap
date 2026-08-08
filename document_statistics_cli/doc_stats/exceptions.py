class DocumentStatisticsError(Exception):
    """
    本项目所有自定义异常的父类。

    以后 main.py 只需要捕获这个父类，
    就能统一处理我们自己定义的业务异常。
    """


class InputDirectoryNotFoundError(
    DocumentStatisticsError
):
    """
    输入目录不存在，或者输入路径不是目录。
    """


class DocumentReadError(
    DocumentStatisticsError
):
    """
    文档读取失败。
    """