package com.example.day012.task;

import com.example.day012.dto.ApiResponse;

import jakarta.validation.Valid;

import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;


@RestController
@RequestMapping("/tasks")
public class TaskController {
    
    private final TaskService taskService;

    public TaskController(
            TaskService taskService
    ){
        this.taskService = taskService;
    }

    @PostMapping
    public ResponseEntity<ApiResponse<TaskResult>> createTask(
        @Valid
        @RequestBody TaskCreateRequest request
    ){
        
        TaskResult result = taskService.createTask(request);

        return ResponseEntity
                .status(HttpStatus.CREATED)
                .body(ApiResponse.success(result));
    }
}

