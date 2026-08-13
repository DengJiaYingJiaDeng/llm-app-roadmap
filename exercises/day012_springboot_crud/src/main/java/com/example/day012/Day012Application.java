package com.example.day012;

import org.mybatis.spring.annotation.MapperScan;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;

@SpringBootApplication
@MapperScan("com.example.day012.mapper")
public class Day012Application {

    public static void main(String[] args) {
        SpringApplication.run(Day012Application.class, args);
    }
}
