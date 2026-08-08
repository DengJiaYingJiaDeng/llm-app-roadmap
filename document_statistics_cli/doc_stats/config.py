from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class AppConfig:
    """
    应用配置对象。

    dataclass:
        用来快速定义“只保存数据”的类。

    frozen=True:
        表示对象创建后，字段不能被随意修改。
        这样配置更稳定。
    """

    # 输入目录，例如 sample_docs
    input_directory: Path

    # JSON 报告输出位置
    output_file: Path

    # 最多显示前多少个高频词
    top_k: int = 10

    # 当前支持分析的文件类型
    supported_suffixes: tuple[str, ...] = (
        ".txt",
        ".md",
    )