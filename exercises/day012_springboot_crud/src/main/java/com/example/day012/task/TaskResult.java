package com.example.day012.task;

public record TaskResult(
        String requestId,
        String taskId,
        String status,
        String result
) {
}