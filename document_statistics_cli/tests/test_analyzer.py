from doc_stats.analyzer import (
    count_lines,
    count_paragraphs,
    count_words,
    extract_words,
)


def test_extract_words() -> None:
    """
    测试：
    大小写和标点是否能正确处理。
    """

    text = "Python, python! Git."

    result = extract_words(text)

    assert result == [
        "python",
        "python",
        "git",
    ]


def test_count_words() -> None:
    """
    测试单词统计。
    """

    text = "Python is useful."

    result = count_words(text)

    assert result == 3


def test_count_lines() -> None:
    """
    测试行数统计。
    """

    text = (
        "line1\n"
        "line2\n"
        "line3"
    )

    result = count_lines(text)

    assert result == 3


def test_count_paragraphs() -> None:
    """
    两个段落中间使用空行分隔。
    """

    text = (
        "First paragraph.\n\n"
        "Second paragraph."
    )

    result = count_paragraphs(
        text
    )

    assert result == 2