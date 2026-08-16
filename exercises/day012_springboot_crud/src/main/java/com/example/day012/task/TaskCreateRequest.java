package com.example.day012.task;

import jakarta.validation.constraints.NotBlank;

import jakarta.validation.constraints.Size;

public record TaskCreateRequest(

    @NotBlank
    @Size(max = 1000)
    String prompt
) {
} 