package com.example.day012.dto;

public record ApiResponse<T>(
        boolean success,
        T data,
        String code,
        String message
) {

    public static <T> ApiResponse<T> success(
            T data
    ) {
        return new ApiResponse<>(
                true,
                data,
                "OK",
                "success"
        );
    }


    public static <T> ApiResponse<T> error(
            String code,
            String message
    ) {
        return new ApiResponse<>(
                false,
                null,
                code,
                message
        );
    }
}