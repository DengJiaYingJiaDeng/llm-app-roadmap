package com.example.day012.exception;

import com.example.day012.dto.ApiResponse;
import com.example.day012.task.AiServiceException;

import org.springframework.dao.DataIntegrityViolationException;
import org.springframework.http.HttpStatus;
import org.springframework.web.bind.MethodArgumentNotValidException;
import org.springframework.web.bind.annotation.ExceptionHandler;
import org.springframework.web.bind.annotation.ResponseStatus;
import org.springframework.web.bind.annotation.RestControllerAdvice;


@RestControllerAdvice
public class GlobalExceptionHandler {

    // 1. 查询的数据不存在 → 404
    @ExceptionHandler(ResourceNotFoundException.class)
    @ResponseStatus(HttpStatus.NOT_FOUND)
    public ApiResponse<Void> handleNotFound(
            ResourceNotFoundException exception
    ) {
        return ApiResponse.error(
                "NOT_FOUND",
                exception.getMessage()
        );
    }


    // 2. DTO 参数校验失败 → 400
    @ExceptionHandler(MethodArgumentNotValidException.class)
    @ResponseStatus(HttpStatus.BAD_REQUEST)
    public ApiResponse<Void> handleValidation(
            MethodArgumentNotValidException exception
    ) {

        String message = exception
                .getBindingResult()
                .getFieldErrors()
                .stream()
                .findFirst()
                .map(error ->
                        error.getField()
                                + ": "
                                + error.getDefaultMessage()
                )
                .orElse("invalid request");

        return ApiResponse.error(
                "INVALID_REQUEST",
                message
        );
    }


    // 3. 重复文档 → 409
    @ExceptionHandler(DuplicateDocumentException.class)
    @ResponseStatus(HttpStatus.CONFLICT)
    public ApiResponse<Void> handleDuplicate(
            DuplicateDocumentException exception
    ) {
        return ApiResponse.error(
                "DUPLICATE_DOCUMENT",
                exception.getMessage()
        );
    }


    // 4. 数据库约束错误 → 400
    @ExceptionHandler(DataIntegrityViolationException.class)
    @ResponseStatus(HttpStatus.BAD_REQUEST)
    public ApiResponse<Void> handleDatabaseConstraint(
            DataIntegrityViolationException exception
    ) {
        return ApiResponse.error(
                "DB_CONSTRAINT",
                "invalid data: database constraint violation"
        );
    }


    // 5. Python AI 服务调用失败 → 502
    @ExceptionHandler(AiServiceException.class)
    @ResponseStatus(HttpStatus.BAD_GATEWAY)
    public ApiResponse<Void> handleAiService(
            AiServiceException exception
    ) {
        return ApiResponse.error(
                "AI_SERVICE_ERROR",
                exception.getMessage()
        );
    }
}