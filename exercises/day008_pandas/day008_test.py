import pandas as pd


# =========================
# 0. 创建原始数据
# =========================

data = {
    "user_id": [
        "U001", "U002", "U003", "U003",
        "U005", "U006", "U007", "U008"
    ],
    "name": [
        " Alice ",
        "BOB",
        " charlie",
        "Charlie",
        None,
        "Eve ",
        "Frank",
        " Grace "
    ],
    "age": [
        "23",
        "31",
        "unknown",
        "27",
        "35",
        None,
        "29",
        "twenty"
    ],
    "city": [
        "Shanghai",
        "beijing ",
        "SHENZHEN",
        "Shenzhen",
        "Shanghai",
        None,
        " BEIJING",
        "Guangzhou"
    ],
    "score": [
        "88.5",
        "92",
        "bad",
        "76.5",
        None,
        "90.5",
        "81",
        "95"
    ]
}

df = pd.DataFrame(data)


# =========================
# 1. 原始数据体检
# =========================

print("===== 原始数据 =====")
print(df)

print("\n===== shape =====")
print(df.shape)

print("\n===== head =====")
print(df.head())

print("\n===== dtypes =====")
print(df.dtypes)

print("\n===== 缺失值 =====")
print(df.isna().sum())

duplicate_user_ids = (
    df.duplicated(subset=["user_id"]).sum()
)

print("\n重复 user_id 数量:")
print(duplicate_user_ids)


# =========================
# 2. 记录原始行数
# =========================

original_rows = len(df)


# =========================
# 3. 按 user_id 去重
# =========================

before_dedup = len(df)

df = df.drop_duplicates(
    subset=["user_id"],
    keep="first"
)

after_dedup = len(df)

removed_duplicates = (
    before_dedup - after_dedup
)


# =========================
# 4. 清洗 name
# =========================

df["name"] = (
    df["name"]
    .str.strip()
    .str.title()
)


# =========================
# 5. 删除 name 缺失
# =========================

before_drop_name = len(df)

df = df.dropna(
    subset=["name"]
)

after_drop_name = len(df)

removed_missing_name = (
    before_drop_name - after_drop_name
)


# =========================
# 6. 清洗 age
# 非法值转成 NaN
# 再转成可空整数 Int64
# =========================

df["age"] = pd.to_numeric(
    df["age"],
    errors="coerce"
)

df["age"] = (
    df["age"]
    .astype("Int64")
)


# =========================
# 7. 清洗 city
# =========================

df["city"] = (
    df["city"]
    .str.strip()
    .str.title()
    .fillna("Unknown")
)


# =========================
# 8. 清洗 score
# 非法值转 NaN
# =========================

df["score"] = pd.to_numeric(
    df["score"],
    errors="coerce"
)


# =========================
# 9. 重置索引
# =========================

df = df.reset_index(drop=True)


# =========================
# 10. 最终数据检查
# =========================

final_rows = len(df)

print("\n===== 清洗后的数据 =====")
print(df)

print("\n===== 最终 shape =====")
print(df.shape)

print("\n===== 最终 dtypes =====")
print(df.dtypes)

print("\n===== 最终缺失值 =====")
print(df.isna().sum())


# =========================
# 11. 清洗过程摘要
# =========================

print("\n===== Cleaning Summary =====")

print("原始行数:", original_rows)
print("删除重复记录:", removed_duplicates)
print("删除 name 缺失记录:", removed_missing_name)
print("最终行数:", final_rows)

print(
    "校验:",
    original_rows
    - removed_duplicates
    - removed_missing_name
    == final_rows
)


# =========================
# 12. 创建数据质量报告
# =========================

quality_report = pd.DataFrame({
    "column": df.columns,
    "dtype": df.dtypes.astype(str).values,
    "missing_count": (
        df.isna().sum().values
    ),
    "missing_rate": (
        df.isna().mean().values * 100
    ),
    "unique_count": [
        df[col].nunique(dropna=True)
        for col in df.columns
    ]
})

print("\n===== Data Quality Report =====")
print(quality_report)


# =========================
# 13. 保存最终结果
# =========================

df.to_parquet(
    "users_clean.parquet",
    index=False
)

quality_report.to_csv(
    "data_quality_report.csv",
    index=False
)

print("\n文件保存完成。")