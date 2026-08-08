import pandas as pd

data = {
    "user_id": [101, 102, 103, 103, 105, 106, 107],
    "name": [
        " Alice ",
        "Bob",
        "charlie",
        "charlie",
        None,
        "EVE ",
        " frank"
    ],
    "age": [
        "23",
        "31",
        "27",
        "27",
        None,
        "unknown",
        "29"
    ],
    "city": [
        "Shanghai",
        "beijing",
        "Shanghai ",
        "Shanghai ",
        "Shenzhen",
        None,
        "BEIJING"
    ],
    "score": [
        88.5,
        92.0,
        76.5,
        76.5,
        None,
        90.5,
        81.0
    ]
}

raw_df = pd.DataFrame(data)

print(raw_df)

raw_df.to_csv(
    "users_raw.csv",
    index = False
)

df = pd.read_csv("users_raw.csv")

print("\n===== 原始数据 =====")
print(df)

print("\n===== shape =====")
print(df.shape)

print("\n===== dtypes =====")
print(df.dtypes)

print("\n===== 缺失值 =====")
print(df.isna().sum())

print(df["age"].dtype)

original_rows = len(df)

print("原始行数:", original_rows)


print(
    df.duplicated(
        subset=["user_id"]
    )
)

print(
    "重复 user_id 数量:",
    df.duplicated(
        subset=["user_id"]
    ).sum()
)

before_dedup = len(df)

df = df.drop_duplicates(
    subset=["user_id"]
)

after_dedup = len(df)

removed_duplicates = (
    before_dedup - after_dedup
)

print("去重前:", before_dedup)
print("去重后:", after_dedup)
print("删除重复记录:", removed_duplicates)

df["name"] =(
    df["name"]
    .str.strip()
    .str.title()
)

print(df["name"])

df["city"] =(
    df["city"]
    .str.strip()
    .str.title()
)


df["city"] = (
    df["city"]
    .fillna("Unknown")
)

print(df["city"])

df["age"] = pd.to_numeric(
    df["age"],
    errors="coerce"
)

print(df["age"])

df["age"] = (
    df["age"]
    .astype("Int64")
)

print(df["age"])
print(df["age"].dtype)


before_drop_name = len(df)

df = df.dropna(
    subset=["name"]
)

after_drop_name = len(df)

removed_missing_name = (
    before_drop_name - after_drop_name
)

print("删除 name 缺失前:", before_drop_name)
print("删除 name 缺失后:", after_drop_name)
print(
    "删除 name 缺失记录:",
    removed_missing_name
)

print("\n===== 最终数据 =====")
print(df)

print("\n最终 shape:")
print(df.shape)

print("\n最终 dtypes:")
print(df.dtypes)

print("\n最终缺失值:")
print(df.isna().sum())

df.to_csv(
    "users_clean.csv",
    index=False
)

df.to_json(
    "users_clean.json",
    orient="records",
    force_ascii=False,
    indent=2
)

df.to_parquet(
    "users_clean.parquet",
    index=False
)

csv_df = pd.read_csv(
    "users_clean.csv"
)

json_df = pd.read_json(
    "users_clean.json"
)

parquet_df = pd.read_parquet(
    "users_clean.parquet"
)

print("\n===== CSV dtypes =====")
print(csv_df.dtypes)

print("\n===== JSON dtypes =====")
print(json_df.dtypes)

print("\n===== Parquet dtypes =====")
print(parquet_df.dtypes)

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

print(
    "\n===== Data Quality Report ====="
)

print(quality_report)


quality_report.to_csv(
    "data_quality_report.csv",
    index=False
)


print("\n===== Cleaning Summary =====")

print("原始行数:", original_rows)

print(
    "删除重复记录:",
    removed_duplicates
)

print(
    "删除 name 缺失记录:",
    removed_missing_name
)

print(
    "最终行数:",
    len(df)
)