package com.example.day012.exception;

public class DuplicateDocumentException extends RuntimeException{
    
    public DuplicateDocumentException(String message){
        super(message);
    }
}
