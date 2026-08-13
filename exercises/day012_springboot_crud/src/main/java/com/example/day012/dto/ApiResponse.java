package com.example.day012.dto;

public record ApiResponse<T>(
        boolean success,
        T data,
        String message
) {

    public static <T> ApiResponse<T> success(T data) {
        return new ApiResponse<>(
                true,
                data,
                "success"
        );
    }

    public static <T> ApiResponse<T> error(String message) {
        return new ApiResponse<>(
                false,
                null,
                message
        );
    }
}
