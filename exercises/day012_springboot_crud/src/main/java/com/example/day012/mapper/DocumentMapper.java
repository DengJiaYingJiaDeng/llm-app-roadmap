package com.example.day012.mapper;

import com.example.day012.model.Document;

import java.util.List;

public interface DocumentMapper {

    void insert(Document document);

    List<Document> findAll();

    Document findById(Long id);

    int update(Document document);

    int deleteById(Long id);
}
