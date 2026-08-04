# 专门用来读取环境变量 + .env配置文件
from pydantic_settings import BaseSettings,SettingsConfigDict

#定义配置类Setting，继承BaseSettings
class Settings(
    BaseSettings
):
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
    )
    app_name:str ="LLM App"

    debug:bool = False

    api_key:str = ""

    # #内部配置类config，告诉程序去根目录读取一个名叫.env的文件加载配置
    # class Config:
    #     env_file = ".env"


settings = Settings()