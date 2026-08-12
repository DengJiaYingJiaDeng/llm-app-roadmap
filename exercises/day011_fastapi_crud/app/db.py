from collections.abc import Generator

import psycopg
from psycopg import Connection
from psycopg.rows import dict_row

from app.config import get_settings

def get_db() -> Generator[Connection,None,None]:
    settings = get_settings() #获取配置，包含database_url

    conn = psycopg.connect(   #用psycopg 建立真实的TCP链接
        settings.database_url,
        row_factory=dict_row, #关键点：让查询结果返回字典(列名：值)，而不是元组
    )

    try:
        yield conn # 把连接“抛”给调用方（比如 API 接口函数）
    finally:
        conn.close()