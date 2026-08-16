package com.example.day012.task;

import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

import org.springframework.http.MediaType;
import org.springframework.stereotype.Service;
import org.springframework.web.client.RestClient;
import org.springframework.web.client.RestClientException;

import ch.qos.logback.classic.spi.STEUtil;

import java.util.UUID;


@Service
public class TaskService {
    
    private static final Logger log = LoggerFactory.getLogger(TaskService.class);

    private final RestClient aiRestClient;

    public TaskService(
             RestClient aiRestClient
    ){
        this.aiRestClient = aiRestClient;
    }

    public TaskResult createTask(
            TaskCreateRequest request
    ){
        String taskId = UUID.randomUUID().toString();

        String requestId = UUID.randomUUID().toString();
    
        log.info(
                "request_id={} service=java-business "
                        + "event=task_created task_id={}",
                requestId,
                taskId
        );

        AiTaskResponse aiResponse;

        try {

            aiResponse =
                    aiRestClient
                            .post()
                            .uri("/ai/tasks/mock")
                            .header(
                                    "X-Request-ID",
                                    requestId
                            )
                            .contentType(
                                    MediaType.APPLICATION_JSON
                            )
                            .body(
                                    new AiTaskRequest(
                                            taskId,
                                            request.prompt()
                                    )
                            )
                            .retrieve()
                            .body(
                                    AiTaskResponse.class
                            );

        } catch (RestClientException exception) {

            log.error(
                    "request_id={} service=java-business "
                            + "event=ai_call_failed task_id={}",
                    requestId,
                    taskId,
                    exception
            );

            throw new AiServiceException(
                    "python ai service call failed"
            );
        }

                if (aiResponse == null) {

            throw new AiServiceException(
                    "python ai service returned empty response"
            );
        }


        log.info(
                "request_id={} service=java-business "
                        + "event=ai_response task_id={} status={}",
                requestId,
                taskId,
                aiResponse.status()
        );


        return new TaskResult(
                requestId,
                taskId,
                aiResponse.status(),
                aiResponse.result()
        );
    }
}
