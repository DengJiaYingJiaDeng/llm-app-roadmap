import json
from pathlib import Path

from doc_stats.config import AppConfig
from doc_stats.report import (
    analyze_directory,
    save_report,
)


def test_analyze_directory(
    tmp_path: Path,
) -> None:
    """
    测试整个目录分析流程。
    """

    # 在 pytest 临时目录中创建 docs
    input_dir = (
        tmp_path / "docs"
    )

    input_dir.mkdir()

    # 创建第一个测试文件
    (
        input_dir / "a.txt"
    ).write_text(
        "Python is useful.\n\n"
        "Same paragraph.",
        encoding="utf-8",
    )

    # 创建第二个测试文件
    (
        input_dir / "b.txt"
    ).write_text(
        "Git is useful.\n\n"
        "Same paragraph.",
        encoding="utf-8",
    )

    # 构造配置
    config = AppConfig(
        input_directory=input_dir,

        output_file=(
            tmp_path / "report.json"
        ),

        top_k=5,
    )

    # 执行目录分析
    report = analyze_directory(
        config
    )

    # 取 summary
    summary = report["summary"]

    # 应该分析到两个文件
    assert (
        summary["total_files"]
        == 2
    )

    # "Same paragraph."
    # 在两个文件中都出现，
    # 因此应该检测到一个重复段落。
    assert (
        len(
            report[
                "duplicate_paragraphs"
            ]
        )
        == 1
    )


def test_save_report(
    tmp_path: Path,
) -> None:
    """
    测试 JSON 是否真的能写入磁盘。
    """

    output = (
        tmp_path / "report.json"
    )

    # 构造一个最小测试报告
    report = {
        "summary": {
            "total_files": 1,
        }
    }

    # 保存
    save_report(
        report,
        output,
    )

    # 判断文件是否存在
    assert output.exists()

    # 再把 JSON 文件读取回来
    text = output.read_text(
        encoding="utf-8"
    )

    # JSON 字符串 -> Python dict
    data = json.loads(text)

    # 确认数据正确
    assert (
        data["summary"][
            "total_files"
        ]
        == 1
    )