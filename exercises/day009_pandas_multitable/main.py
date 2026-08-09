from data import (
    create_users,
    create_orders,
    create_events
)
from features import (
    build_order_features,
    build_event_features
)


users = create_users()
orders = create_orders()
events = create_events()


print("===== USERS =====")
print(users)

print("\n===== ORDERS =====")
print(orders)

print("\n===== EVENTS =====")
print(events)

print("\n===== SHAPE =====")

print("users:", users.shape)
print("orders:", orders.shape)
print("events:", events.shape)

print("\n===== KEY CHECK =====")

print(
    "users.user_id unique:",
    users["user_id"].is_unique
)

print(
    "orders.order_id unique:",
    orders["order_id"].is_unique
)

print(
    "events.event_id unique:",
    events["event_id"].is_unique
)

order_features = build_order_features(orders)

print("\n===== ORDER FEATURES =====")
print(order_features)

event_features = build_event_features(events)

print("\n===== EVENT FEATURES =====")
print(event_features)

user_features = (
    users
    .merge(
        order_features,
        on="user_id",
        how="left",
        validate="one_to_one"
    )
    .merge(
        event_features,
        on="user_id",
        how="left",
        validate="one_to_one"
    )
)

user_features["order_count"] = (
    user_features["order_count"]
    .fillna(0)
    .astype("Int64")
)

user_features["total_amount"] = (
    user_features["total_amount"]
    .fillna(0)
)

print("\n===== USER FEATURES =====")
print(user_features)

print("\nshape:")
print(user_features.shape)

print("\nuser_id 是否唯一:")
print(user_features["user_id"].is_unique)

print("\n===== ROW COUNT CHECK =====")

print("users rows:", len(users))
print("order_features rows:", len(order_features))
print("event_features rows:", len(event_features))
print("user_features rows:", len(user_features))

assert len(user_features) == len(users)

assert user_features["user_id"].is_unique

bad_merge = orders.merge(
    events,
    on="user_id",
    how="inner"
)

print("\n===== BAD MERGE =====")
print("orders rows:", len(orders))
print("events rows:", len(events))
print("bad_merge rows:", len(bad_merge))

print(
    bad_merge[
        bad_merge["user_id"] == 101
    ]
)

real_total = (
    orders[
        orders["user_id"] == 101
    ]["amount"].sum()
)

wrong_total = (
    bad_merge[
        bad_merge["user_id"] == 101
    ]["amount"].sum()
)

print("真实订单总额:", real_total)
print("错误 merge 后统计:", wrong_total)

user_features.to_csv(
    "user_features.csv",
    index=False
)

user_features.to_parquet(
    "user_features.parquet",
    index=False
)

print("\n输出完成")