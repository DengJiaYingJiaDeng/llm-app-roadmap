import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))

from app.user import User
from app.model import Document
from app.exceptions import AppException
from app.service import get_document
from app.config import settings

def main():

    user = User(
        "Alice",
        "Developer"
    )

    print(
        user.introduce()
    )

    doc = Document(
        1,
        "Python",
        "Python engineering"
    )

    print(doc)

    try:
        result = get_document(-1)

        print(result)

    except AppException as e:
        print(
            f"error:{e.code},{e.message}"
        )

    print(settings.app_name)
    print(settings.debug)
    print(settings.api_key)


if __name__ == "__main__":
    main()