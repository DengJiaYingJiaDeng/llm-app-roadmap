import logging
from typing import Annotated

from fastapi import APIRouter, Header, HTTPException, status

from app.schemas import AiTaskRequest, AiTaskResponse


router = APIRouter(
    prefix="/ai/tasks",
    tags=["ai-tasks"],
)

logger = logging.getLogger("ai_tasks")


@router.post(
    "/mock",
    response_model=AiTaskResponse,
)
def run_mock_task(
    payload: AiTaskRequest,
    x_request_id: Annotated[str | None, Header()] = None,
):
    if not x_request_id:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail={
                "code": "MISSING_REQUEST_ID",
                "message": "X-Request-ID is required",
            },
        )

    logger.info(
        "request_id=%s service=python-ai "
        "event=task_received task_id=%s",
        x_request_id,
        payload.taskId,
    )

    result = f"mock result: {payload.prompt}"

    logger.info(
        "request_id=%s service=python-ai "
        "event=task_completed task_id=%s",
        x_request_id,
        payload.taskId,
    )

    return AiTaskResponse(
        requestId=x_request_id,
        taskId=payload.taskId,
        status="COMPLETED",
        result=result,
    )