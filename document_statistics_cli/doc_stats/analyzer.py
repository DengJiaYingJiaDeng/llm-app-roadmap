from collections import Counter
from pathlib import Path
import re

from doc_stats.config import AppConfig
from doc_stats.exceptions import (
    DocumentReadError,
    InputDirectoryNotFoundError,
)


def find_documents(
    config: AppConfig,
) -> list[Path]:
    """
    在配置指定的目录中查找所有支持的文档。

    返回：
        list[Path]

    例如：
        [
            Path("sample_docs/a.txt"),
            Path("sample_docs/b.md"),
        ]
    """

    # 取出配置中的输入目录
    directory = config.input_directory

    # exists()：判断路径是否存在
    if not directory.exists():
        raise InputDirectoryNotFoundError(
            f"目录不存在: {directory}"
        )

    # is_dir()：判断它是否真的是目录
    if not directory.is_dir():
        raise InputDirectoryNotFoundError(
            f"输入路径不是目录: {directory}"
        )

    # rglob("*")：
    # 递归查找目录中的所有内容。
    #
    # 例如：
    # sample_docs/a.txt
    # sample_docs/sub/b.md
    #
    # 都能找到。
    files = [
        path
        for path in directory.rglob("*")
        if (
            # 只保留文件，不要目录
            path.is_file()

            # suffix 表示扩展名，例如 ".txt"
            and path.suffix.lower()
            in config.supported_suffixes
        )
    ]

    # 排序后返回，方便每次运行结果稳定
    return sorted(files)


def read_document(
    path: Path,
) -> str:
    """
    使用 UTF-8 编码读取文件。

    如果文件无法读取，
    转换成我们自己的 DocumentReadError。
    """

    try:
        return path.read_text(
            encoding="utf-8"
        )

    except (
        OSError,
        UnicodeDecodeError,
    ) as exc:
        # from exc：
        # 保留原始异常原因，
        # 调试时可以看到真正底层错误。
        raise DocumentReadError(
            f"读取文件失败: {path}"
        ) from exc


def extract_words(
    text: str,
) -> list[str]:
    """
    从文本中提取英文单词。

    当前这个项目先做简单英文词频统计，
    暂时不做真正的中文分词。
    """

    # lower()：
    # 全部转成小写。
    #
    # Python / PYTHON / python
    # 都会统计为 python。
    text = text.lower()

    # 正则表达式：
    # [A-Za-z0-9']+
    #
    # 表示匹配：
    # 英文字母、数字、单引号
    #
    # + 表示至少出现一次。
    words = re.findall(
        r"[A-Za-z0-9']+",
        text,
    )

    return words


def extract_paragraphs(
    text: str,
) -> list[str]:
    """
    按空行切分文本中的段落。
    """

    # 如果文件只有空格或为空，
    # 直接返回空列表。
    if not text.strip():
        return []

    # text.strip()
    # 去掉文本开头和结尾多余空白。
    #
    # re.split(r"\n\s*\n", ...)
    # 表示遇到“空行”时进行切分。
    raw_paragraphs = re.split(
        r"\n\s*\n",
        text.strip(),
    )

    # 清除每个段落前后的空白，
    # 同时过滤空段落。
    paragraphs = [
        paragraph.strip()
        for paragraph in raw_paragraphs
        if paragraph.strip()
    ]

    return paragraphs


def count_characters(
    text: str,
) -> int:
    """
    统计所有字符数量。

    包括：
    - 字母
    - 数字
    - 空格
    - 换行
    - 标点
    """

    return len(text)


def count_non_whitespace_characters(
    text: str,
) -> int:
    """
    统计非空白字符数量。

    空白包括：
    - 空格
    - 换行
    - tab
    """

    return sum(
        1
        for char in text
        if not char.isspace()
    )


def count_words(
    text: str,
) -> int:
    """
    统计单词数量。
    """

    words = extract_words(text)

    return len(words)


def count_lines(
    text: str,
) -> int:
    """
    统计文本行数。
    """

    # 空字符串没有行
    if not text:
        return 0

    # splitlines() 会按换行符拆分
    return len(
        text.splitlines()
    )


def count_paragraphs(
    text: str,
) -> int:
    """
    统计段落数量。
    """

    paragraphs = extract_paragraphs(
        text
    )

    return len(paragraphs)


def word_frequency(
    text: str,
) -> Counter[str]:
    """
    统计每个单词出现多少次。

    Counter 是 collections 模块里的计数工具。
    """

    words = extract_words(text)

    return Counter(words)


def analyze_document(
    path: Path,
) -> dict[str, object]:
    """
    对单个文件进行完整分析。

    最后返回一个 dict，
    后面可以直接转换为 JSON。
    """

    # 先读取文件
    text = read_document(path)

    # 统计词频
    frequency = word_frequency(text)

    # 把所有分析结果组合成字典
    return {
        "file": str(path),

        "characters":
            count_characters(text),

        "non_whitespace_characters":
            count_non_whitespace_characters(
                text
            ),

        "lines":
            count_lines(text),

        "words":
            count_words(text),

        "paragraphs":
            count_paragraphs(text),

        # Counter 不是最基础的 JSON 类型，
        # 所以转换成普通 dict。
        "word_frequency":
            dict(frequency),
    }