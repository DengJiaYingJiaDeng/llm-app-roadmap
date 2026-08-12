from typing import Annotated

import psycopg
from fastapi import APIRouter, Depends, HTTPException, Response, status
from psycopg.errors import ForeignKeyViolation

from app.db import get_db
from app.schemas import DocumentCreate, DocumentOut, DocumentUpdate

# APIRouter：把文档相关的接口统一挂载到 /documents 路径下
router = APIRouter(
    prefix="/documents",
    tags=["documents"],
)

"""
FastAPI 依赖注入的“快捷写法”。Annotated 告诉 FastAPI：“这个参数需要一个数据库连接，请调用 get_db() 函数帮我拿到它”。这样在每个函数里直接声明 conn: DbConn，就能拿到连接，省去了重复写 Depends(get_db) 的冗余。
"""
DbConn = Annotated[
    psycopg.Connection,
    Depends(get_db),
]

@router.post(
    "",
    response_model=DocumentOut,
    status_code=status.HTTP_201_CREATED,
)
def create_document(
    payload:DocumentCreate,
    conn:DbConn,
):
    try:
        with conn.cursor() as cur:
            cur.execute(
                """
                INSERT INTO documents (
                    user_id,
                    title,
                    content
                )
                VALUES (%s, %s, %s)
                RETURNING
                    id,
                    user_id,
                    title,
                    content,
                    created_at
                """,
                (
                    payload.user_id,
                    payload.title,
                    payload.content,
                ),
            )

            document = cur.fetchone()

        conn.commit()

        return document

    except ForeignKeyViolation:
        conn.rollback()

        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="user_id does not exist",
        )
       
@router.get(
    "",
    response_model=list[DocumentOut],
)
def list_documents(
    conn: DbConn,
):
    with conn.cursor() as cur:
        cur.execute(
            """
            SELECT
                id,
                user_id,
                title,
                content,
                created_at
            FROM documents
            ORDER BY id
            """
        )

        return cur.fetchall()


@router.get(
    "/{document_id}",
    response_model=DocumentOut,
)
def get_document(
    document_id: int,
    conn: DbConn,
):
    with conn.cursor() as cur:
        cur.execute(
            """
            SELECT
                id,
                user_id,
                title,
                content,
                created_at
            FROM documents
            WHERE id = %s
            """,
            (document_id,),
        )

        document = cur.fetchone()

    if document is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="document not found",
        )

    return document


@router.put(
    "/{document_id}",
    response_model=DocumentOut,
)
def update_document(
    document_id: int,
    payload: DocumentUpdate,
    conn: DbConn,
):
    with conn.cursor() as cur:
        cur.execute(
            """
            UPDATE documents
            SET
                title = %s,
                content = %s
            WHERE id = %s
            RETURNING
                id,
                user_id,
                title,
                content,
                created_at
            """,
            (
                payload.title,
                payload.content,
                document_id,
            ),
        )

        document = cur.fetchone()

    if document is None:
        conn.rollback()

        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="document not found",
        )

    conn.commit()

    return document


@router.delete(
    "/{document_id}",
    status_code=status.HTTP_204_NO_CONTENT,
)
def delete_document(
    document_id: int,
    conn: DbConn,
):
    with conn.cursor() as cur:
        cur.execute(
            """
            DELETE FROM documents
            WHERE id = %s
            RETURNING id
            """,
            (document_id,),
        )

        deleted = cur.fetchone()

    if deleted is None:
        conn.rollback()

        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="document not found",
        )

    conn.commit()

    return Response(
        status_code=status.HTTP_204_NO_CONTENT,
    )