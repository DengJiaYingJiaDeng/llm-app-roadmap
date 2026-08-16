package com.example.day012.mapper;

import com.example.day012.model.Document;
import org.apache.ibatis.annotations.Mapper;
import org.apache.ibatis.annotations.Param;

import java.util.List;

@Mapper
public interface DocumentMapper {

    void insert(Document document);

    List<Document> findAll();

    Document findById(Long id);

    int update(Document document);

    int deleteById(Long id);

    int countByUserIdAndTitle(
            @Param("userId") Long userId,
            @Param("title") String title
    );
}