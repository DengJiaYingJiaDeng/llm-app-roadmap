package com.example.day012.dto;

import jakarta.validation.constraints.NotBlank;
import jakarta.validation.constraints.NotNull;
import jakarta.validation.constraints.Positive;
import jakarta.validation.constraints.Size;

public record DocumentCreateRequest(

        @NotNull
        @Positive
        Long userId,

        @NotBlank
        @Size(max = 200)
        String title,

        String content

) {
}
