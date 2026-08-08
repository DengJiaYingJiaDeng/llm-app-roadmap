import argparse
from pathlib import Path

from doc_stats.config import AppConfig
from doc_stats.exceptions import (
    DocumentStatisticsError,
)
from doc_stats.logger import setup_logger
from doc_stats.report import (
    analyze_directory,
    save_report,
)


# 初始化日志对象
logger = setup_logger()


def parse_args() -> argparse.Namespace:
    """
    解析命令行参数。

    例如用户运行：

    python main.py \
        --input sample_docs \
        --output report.json \
        --top-k 10
    """

    # 创建命令行参数解析器
    parser = argparse.ArgumentParser(
        description=(
            "统计目录中的文本文件并生成 JSON 报告"
        )
    )

    # 必须传入的输入目录
    parser.add_argument(
        "--input",

        # required=True：
        # 用户不传就报错
        required=True,

        help="待分析的目录",
    )

    # 输出 JSON 文件位置
    parser.add_argument(
        "--output",

        # 用户不传时默认 report.json
        default="report.json",

        help="JSON 报告输出路径",
    )

    # Top-K
    parser.add_argument(
        "--top-k",

        # argparse 默认得到字符串，
        # type=int 自动转换成整数
        type=int,

        default=10,

        help="输出词频最高的前 K 个单词",
    )

    # 真正解析命令行
    return parser.parse_args()


def main() -> int:
    """
    程序主函数。

    返回：
        0：程序正常结束
        1：程序发生错误

    这是 Linux CLI 中常见的退出码习惯。
    """

    # 读取用户传入的命令行参数
    args = parse_args()

    # 先校验 top_k
    if args.top_k <= 0:

        logger.error(
            "--top-k 必须大于 0"
        )

        return 1

    # 将命令行参数转换成 AppConfig
    config = AppConfig(
        input_directory=Path(
            args.input
        ),

        output_file=Path(
            args.output
        ),

        top_k=args.top_k,
    )

    try:
        # 记录开始信息
        logger.info(
            "开始分析目录: %s",
            config.input_directory,
        )

        # 对整个目录执行分析
        report = analyze_directory(
            config
        )

        # 保存 JSON
        save_report(
            report,
            config.output_file,
        )

        logger.info(
            "分析完成，报告已保存: %s",
            config.output_file,
        )

        # report["summary"] 是一个 dict，
        # 再取其中的 total_files。
        logger.info(
            "共分析 %s 个文件",
            report["summary"][
                "total_files"
            ],
        )

        # 0 表示成功
        return 0

    except DocumentStatisticsError as exc:
        # 捕获我们自己定义的业务异常。
        #
        # 这样用户只看到清晰错误信息，
        # 而不是整页 traceback。
        logger.error(
            "程序执行失败: %s",
            exc,
        )

        return 1


# 只有直接运行 main.py 时，
# 才执行下面代码。
#
# 如果别人 import main，
# 则不会自动执行。
if __name__ == "__main__":

    # main() 返回 0 或 1，
    # SystemExit 把它转换成程序退出码。
    raise SystemExit(
        main()
    )