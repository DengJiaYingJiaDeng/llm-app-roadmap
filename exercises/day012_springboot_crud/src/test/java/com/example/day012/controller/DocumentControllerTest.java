package com.example.day012.controller;

import com.example.day012.dto.DocumentCreateRequest;
import com.example.day012.exception.DuplicateDocumentException;
import com.example.day012.exception.ResourceNotFoundException;
import com.example.day012.model.Document;
import com.example.day012.service.DocumentService;

import org.junit.jupiter.api.Test;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.webmvc.test.autoconfigure.WebMvcTest;
import org.springframework.http.MediaType;
import org.springframework.test.context.bean.override.mockito.MockitoBean;
import org.springframework.test.web.servlet.MockMvc;

import java.time.LocalDateTime;

import static org.mockito.ArgumentMatchers.any;
import static org.mockito.BDDMockito.given;

import static org.springframework.test.web.servlet.request.MockMvcRequestBuilders.*;
import static org.springframework.test.web.servlet.result.MockMvcResultMatchers.*;


@WebMvcTest(DocumentController.class)
class DocumentControllerTest {

    @Autowired
    private MockMvc mockMvc;

    @MockitoBean
    private DocumentService documentService;


    @Test
    void createDocumentShouldReturn201() throws Exception {

        Document document = createDocument();

        given(
                documentService.create(
                        any(DocumentCreateRequest.class)
                )
        ).willReturn(document);


        mockMvc.perform(
                post("/documents")
                        .contentType(MediaType.APPLICATION_JSON)
                        .content("""
                                {
                                  "userId": 1,
                                  "title": "Spring测试",
                                  "content": "hello"
                                }
                                """)
        )
        .andExpect(status().isCreated())
        .andExpect(jsonPath("$.success").value(true))
        .andExpect(jsonPath("$.data.id").value(10))
        .andExpect(
                jsonPath("$.data.title")
                        .value("Spring测试")
        );
    }


    @Test
    void getDocumentShouldReturn200() throws Exception {

        Document document = createDocument();

        given(
                documentService.getById(10L)
        ).willReturn(document);


        mockMvc.perform(
                get("/documents/10")
        )
        .andExpect(status().isOk())
        .andExpect(jsonPath("$.success").value(true))
        .andExpect(jsonPath("$.data.id").value(10));
    }


    @Test
    void missingTitleShouldReturn400() throws Exception {

        mockMvc.perform(
                post("/documents")
                        .contentType(MediaType.APPLICATION_JSON)
                        .content("""
                                {
                                  "userId": 1,
                                  "content": "hello"
                                }
                                """)
        )
        .andExpect(status().isBadRequest())
        .andExpect(
                jsonPath("$.success").value(false)
        );
    }


    @Test
    void invalidUserIdShouldReturn400() throws Exception {

        mockMvc.perform(
                post("/documents")
                        .contentType(MediaType.APPLICATION_JSON)
                        .content("""
                                {
                                  "userId": 0,
                                  "title": "test",
                                  "content": "hello"
                                }
                                """)
        )
        .andExpect(status().isBadRequest());
    }


    @Test
    void missingDocumentShouldReturn404() throws Exception {

        given(
                documentService.getById(999L)
        ).willThrow(
                new ResourceNotFoundException(
                        "document not found: 999"
                )
        );


        mockMvc.perform(
                get("/documents/999")
        )
        .andExpect(status().isNotFound())
        .andExpect(
                jsonPath("$.success").value(false)
        );
    }


    @Test
    void duplicateDocumentShouldReturn409()
            throws Exception {

        given(
                documentService.create(
                        any(DocumentCreateRequest.class)
                )
        ).willThrow(
                new DuplicateDocumentException(
                        "document already exists"
                )
        );


        mockMvc.perform(
                post("/documents")
                        .contentType(MediaType.APPLICATION_JSON)
                        .content("""
                                {
                                  "userId": 1,
                                  "title": "Spring测试",
                                  "content": "hello"
                                }
                                """)
        )
        .andExpect(status().isConflict())
        .andExpect(
                jsonPath("$.success").value(false)
        )
        .andExpect(
                jsonPath("$.message")
                        .value("document already exists")
        );
    }


    private Document createDocument() {

        Document document = new Document();

        document.setId(10L);
        document.setUserId(1L);
        document.setTitle("Spring测试");
        document.setContent("hello");
        document.setCreatedAt(
                LocalDateTime.now()
        );

        return document;
    }
}