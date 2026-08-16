package com.example.day012.task;

public record AiTaskRequest(
    String taskId,
    String prompt
) {
}