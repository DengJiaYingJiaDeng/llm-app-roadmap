from app.service import get_document
from app.exceptions import AppException

def test_invalid_document():
    try:
        get_document(-1)

        assert False

    except AppException as e:

        assert e.code == "DOC_001"