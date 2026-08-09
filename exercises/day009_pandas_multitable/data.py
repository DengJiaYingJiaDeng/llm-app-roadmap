import pandas as pd


def create_users() -> pd.DataFrame:
    return pd.DataFrame({
        "user_id": [101, 102, 103, 104],
        "name": [
            "Alice",
            "Bob",
            "Charlie",
            "David"
        ],
        "city": [
            "Shanghai",
            "Beijing",
            "Shenzhen",
            "Shanghai"
        ]
    })


def create_orders() -> pd.DataFrame:
    return pd.DataFrame({
        "order_id": [
            "O001",
            "O002",
            "O003",
            "O004",
            "O005",
            "O006"
        ],
        "user_id": [
            101,
            101,
            102,
            103,
            101,
            103
        ],
        "amount": [
            100,
            200,
            150,
            80,
            120,
            160
        ],
        "order_time": [
            "2026-08-01 10:00:00",
            "2026-08-03 09:30:00",
            "2026-08-02 14:00:00",
            "2026-08-01 16:30:00",
            "2026-08-05 18:00:00",
            "2026-08-04 11:00:00"
        ]
    })


def create_events() -> pd.DataFrame:
    return pd.DataFrame({
        "event_id": [
            "E001",
            "E002",
            "E003",
            "E004",
            "E005",
            "E006",
            "E007",
            "E008"
        ],
        "user_id": [
            101,
            101,
            101,
            102,
            102,
            103,
            103,
            104
        ],
        "event_type": [
            "login",
            "click",
            "purchase",
            "login",
            "click",
            "login",
            "purchase",
            "login"
        ],
        "event_time": [
            "2026-08-01 08:00:00",
            "2026-08-01 09:00:00",
            "2026-08-03 09:20:00",
            "2026-08-02 09:00:00",
            "2026-08-02 10:00:00",
            "2026-08-01 15:00:00",
            "2026-08-04 10:30:00",
            "2026-08-03 12:00:00"
        ]
    })