from data import (
    create_users,
    create_orders,
    create_events
)

from features import (
    build_order_features,
    build_event_features
)


def test_order_features_one_row_per_user():
    orders = create_orders()

    result = build_order_features(orders)

    assert result["user_id"].is_unique
    assert len(result) == 3


def test_user_101_order_stats():
    orders = create_orders()

    result = build_order_features(orders)

    user_101 = result[
        result["user_id"] == 101
    ].iloc[0]

    assert user_101["order_count"] == 3
    assert user_101["total_amount"] == 420
    assert user_101["max_amount"] == 200
    assert user_101["recent_2_order_avg"] == 160


def test_event_features_one_row_per_user():
    events = create_events()

    result = build_event_features(events)

    assert result["user_id"].is_unique
    assert len(result) == 4


def test_user_101_event_counts():
    events = create_events()

    result = build_event_features(events)

    user_101 = result[
        result["user_id"] == 101
    ].iloc[0]

    assert user_101["login"] == 1
    assert user_101["click"] == 1
    assert user_101["purchase"] == 1