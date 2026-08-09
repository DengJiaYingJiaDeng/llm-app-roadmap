import pandas as pd

def build_order_features(
    orders:pd.DataFrame
)->pd.DataFrame:
    df = orders.copy()

    #1.时间转换
    df["order_time"] = pd.to_datetime(
        df["order_time"],
        errors="coerce"
    )

        # 2. 排序
    df = df.sort_values(
        ["user_id", "order_time"]
    )

        # 3. 用户基础订单统计
    order_stats = (
        df
        .groupby("user_id", as_index=False)
        .agg(
            order_count=("order_id", "count"),
            total_amount=("amount", "sum"),
            avg_amount=("amount", "mean"),
            max_amount=("amount", "max")
        )
    )

    # 4. 最近两笔平均金额
    df["rolling_2_avg"] = (
        df
        .groupby("user_id")["amount"]
        .transform(
            lambda s: s.rolling(
                2,
                min_periods=1
            ).mean()
        )
    )

        # 5. 每个用户最近一笔订单
    latest = (
        df
        .groupby("user_id")
        .tail(1)[
            [
                "user_id",
                "order_time",
                "amount",
                "rolling_2_avg"
            ]
        ]
        .rename(
            columns={
                "order_time": "last_order_time",
                "amount": "last_order_amount",
                "rolling_2_avg": "recent_2_order_avg"
            }
        )
    )

    # 6. 合并
    result = order_stats.merge(
        latest,
        on="user_id",
        how="left",
        validate="one_to_one"
    )

    return result

def build_event_features(
    events: pd.DataFrame
) -> pd.DataFrame:

    df = events.copy()

    # 1. 时间转换
    df["event_time"] = pd.to_datetime(
        df["event_time"],
        errors="coerce"
    )

    # 2. 排序
    df = df.sort_values(
        ["user_id", "event_time"]
    )

    # 3. 各类事件次数
    event_counts = df.pivot_table(
        index="user_id",
        columns="event_type",
        values="event_id",
        aggfunc="count",
        fill_value=0
    )

    event_counts.columns.name = None
    event_counts = event_counts.reset_index()

    # 4. 最近一次事件
    latest_event = (
        df
        .groupby("user_id")
        .tail(1)[
            [
                "user_id",
                "event_type",
                "event_time"
            ]
        ]
        .rename(
            columns={
                "event_type": "last_event_type",
                "event_time": "last_event_time"
            }
        )
        .reset_index(drop=True)
    )

    # 5. 合并
    result = event_counts.merge(
        latest_event,
        on="user_id",
        how="left",
        validate="one_to_one"
    )

    return result