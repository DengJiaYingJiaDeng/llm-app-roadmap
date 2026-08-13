package com.example.day012.dto;

import jakarta.validation.constraints.NotBlank;
import jakarta.validation.constraints.Size;

public record DocumentUpdateRequest(

        @NotBlank
        @Size(max = 200)
        String title,

        String content

) {
}
