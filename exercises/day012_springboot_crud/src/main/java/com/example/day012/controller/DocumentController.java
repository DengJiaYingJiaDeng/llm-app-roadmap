package com.example.day012.controller;

import com.example.day012.dto.ApiResponse;
import com.example.day012.dto.DocumentCreateRequest;
import com.example.day012.dto.DocumentUpdateRequest;
import com.example.day012.model.Document;
import com.example.day012.service.DocumentService;
import jakarta.validation.Valid;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import java.util.List;


@RestController
@RequestMapping("/documents")
public class DocumentController {

    private final DocumentService documentService;

    public DocumentController(
            DocumentService documentService
    ) {
        this.documentService = documentService;
    }


    @PostMapping
    public ResponseEntity<ApiResponse<Document>> create(
            @Valid
            @RequestBody DocumentCreateRequest request
    ) {

        Document document =
                documentService.create(request);

        return ResponseEntity
                .status(HttpStatus.CREATED)
                .body(ApiResponse.success(document));
    }


    @GetMapping
    public ApiResponse<List<Document>> list() {

        return ApiResponse.success(
                documentService.list()
        );
    }


    @GetMapping("/{id}")
    public ApiResponse<Document> getById(
            @PathVariable Long id
    ) {

        return ApiResponse.success(
                documentService.getById(id)
        );
    }


    @PutMapping("/{id}")
    public ApiResponse<Document> update(
            @PathVariable Long id,
            @Valid
            @RequestBody DocumentUpdateRequest request
    ) {

        return ApiResponse.success(
                documentService.update(id, request)
        );
    }


    @DeleteMapping("/{id}")
    public ApiResponse<Void> delete(
            @PathVariable Long id
    ) {

        documentService.delete(id);

        return ApiResponse.success(null);
    }
}
