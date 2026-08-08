from collections import Counter
import json
from pathlib import Path

from doc_stats.analyzer import (
    analyze_document,
    extract_paragraphs,
    extract_words,
    find_documents,
    read_document,
)

from doc_stats.config import AppConfig


def find_duplicate_paragraphs(
    documents: list[Path],
) -> list[dict[str, object]]:
    """
    查找多个文件中重复出现的段落。
    """

    # key：
    #     段落内容
    #
    # value：
    #     这个段落出现在哪些文件中
    #
    # 例如：
    #
    # {
    #     "Python is useful.": [
    #         "a.txt",
    #         "b.txt",
    #     ]
    # }
    paragraph_locations: dict[
        str,
        list[str],
    ] = {}

    # 遍历每一个文档
    for document in documents:

        # 读取全文
        text = read_document(
            document
        )

        # 提取所有段落
        paragraphs = extract_paragraphs(
            text
        )

        # 遍历该文件中的每一个段落
        for paragraph in paragraphs:

            # setdefault：
            #
            # 如果 paragraph 不存在，
            # 创建：
            #
            # paragraph: []
            #
            # 然后返回这个列表。
            paragraph_locations.setdefault(
                paragraph,
                [],
            ).append(
                str(document)
            )

    duplicates = []

    # 遍历统计结果
    for (
        paragraph,
        locations,
    ) in paragraph_locations.items():

        # 出现在两个或以上位置，
        # 就视为重复段落。
        if len(locations) > 1:

            duplicates.append(
                {
                    "paragraph":
                        paragraph,

                    "count":
                        len(locations),

                    "files":
                        locations,
                }
            )

    return duplicates


def get_global_top_words(
    documents: list[Path],
    k: int,
) -> list[dict[str, object]]:
    """
    统计整个目录中出现次数最多的前 K 个单词。
    """

    # 创建一个空 Counter
    counter: Counter[str] = Counter()

    for document in documents:

        # 读取文件
        text = read_document(
            document
        )

        # 提取单词
        words = extract_words(text)

        # update 会累加计数
        #
        # 第一个文件：
        # python -> 2
        #
        # 第二个文件又出现一次：
        # python -> 3
        counter.update(words)

    # most_common(k)
    # 返回出现次数最多的前 k 项。
    #
    # 例如：
    # [
    #     ("python", 5),
    #     ("git", 3),
    # ]
    top_words = counter.most_common(k)

    # 转换为更适合 JSON 的结构。
    return [
        {
            "word": word,
            "count": count,
        }
        for word, count
        in top_words
    ]


def analyze_directory(
    config: AppConfig,
) -> dict[str, object]:
    """
    分析整个目录。
    """

    # 1. 找到所有需要分析的文件
    documents = find_documents(
        config
    )

    # 2. 对每个文件分别执行 analyze_document
    file_reports = [
        analyze_document(document)
        for document in documents
    ]

    # 3. 对每个文件的字符数求和
    total_characters = sum(
        int(report["characters"])
        for report in file_reports
    )

    # 4. 总单词数    sum(...for...)生成器表达式，循环产出一个个数字，sum把全部数字相加
    total_words = sum(
        int(report["words"])
        for report in file_reports
    )

    # 5. 总行数
    total_lines = sum(
        int(report["lines"])
        for report in file_reports
    )

    # 6. 总段落数
    total_paragraphs = sum(
        int(report["paragraphs"])
        for report in file_reports
    )

    # 返回整个目录的最终报告
    return {
        "summary": {
            "total_files":
                len(documents),

            "total_characters":
                total_characters,

            "total_words":
                total_words,

            "total_lines":
                total_lines,

            "total_paragraphs":
                total_paragraphs,
        },

        # 全局 Top-K 词频
        "top_words":
            get_global_top_words(
                documents,
                config.top_k,
            ),

        # 跨文件重复段落
        "duplicate_paragraphs":
            find_duplicate_paragraphs(
                documents
            ),

        # 每一个文件的详细统计
        "files":
            file_reports,
    }


def save_report(
    report: dict[str, object],
    output_file: Path,
) -> None:
    """
    将 Python 字典保存成 JSON 文件。
    """

    # 如果输出目录不存在，
    # 自动创建。
    #
    # parents=True：
    # 中间目录也一起创建。
    #
    # exist_ok=True：
    # 已存在时不要报错。
    output_file.parent.mkdir(
        parents=True,
        exist_ok=True,
    )

    # json.dumps：
    # Python dict -> JSON 字符串
    json_text = json.dumps(
        report,

        # 中文直接显示，
        # 不转成 \uXXXX
        ensure_ascii=False,

        # JSON 缩进，更容易阅读
        indent=2,
    )

    # 写入文件
    output_file.write_text(
        json_text,
        encoding="utf-8",
    )