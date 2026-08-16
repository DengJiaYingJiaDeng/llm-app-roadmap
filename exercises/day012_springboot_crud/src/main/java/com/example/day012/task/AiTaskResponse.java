package com.example.day012.task;

public record AiTaskResponse(
        String requestId,
        String taskId,
        String status,
        String result
) {
}