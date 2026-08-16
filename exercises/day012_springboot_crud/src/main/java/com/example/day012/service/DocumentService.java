package com.example.day012.service;

import com.example.day012.dto.DocumentCreateRequest;
import com.example.day012.dto.DocumentUpdateRequest;
import com.example.day012.exception.ResourceNotFoundException;
import com.example.day012.mapper.DocumentMapper;
import com.example.day012.model.Document;
import com.example.day012.exception.DuplicateDocumentException;
import org.springframework.stereotype.Service;
import org.springframework.transaction.annotation.Transactional;

import java.util.List;

@Service
public class DocumentService {

    private final DocumentMapper documentMapper;

    public DocumentService(DocumentMapper documentMapper) {
        this.documentMapper = documentMapper;
    }


    @Transactional
    public Document create(DocumentCreateRequest request) {

        int count =
                documentMapper.countByUserIdAndTitle(request.userId(), request.title());
        if(count > 0){
            throw new DuplicateDocumentException("document already exists");
        }

        Document document = new Document();

        document.setUserId(request.userId());
        document.setTitle(request.title());
        document.setContent(request.content());

        documentMapper.insert(document);

        return getById(document.getId());
    }


    public List<Document> list() {
        return documentMapper.findAll();
    }


    public Document getById(Long id) {

        Document document =
                documentMapper.findById(id);

        if (document == null) {
            throw new ResourceNotFoundException(
                    "document not found: " + id
            );
        }

        return document;
    }


    @Transactional
    public Document update(
            Long id,
            DocumentUpdateRequest request
    ) {

        getById(id);

        Document document = new Document();

        document.setId(id);
        document.setTitle(request.title());
        document.setContent(request.content());

        documentMapper.update(document);

        return getById(id);
    }


    @Transactional
    public void delete(Long id) {

        getById(id);

        documentMapper.deleteById(id);
    }
}
