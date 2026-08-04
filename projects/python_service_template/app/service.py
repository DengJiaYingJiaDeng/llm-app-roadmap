from app.exceptions import AppException
from app.logger import get_logger

logger = get_logger(__name__)


def get_document(doc_id:int):

    logger.info(
        f"request document id={doc_id}"
    )

    if doc_id <= 0:

        logger.error(
            "invalid document id"
        )

        raise AppException(
            "invalid id",
            "DOC_001"
        )

    return{
        "id":doc_id,
        "title":"test document"
    }