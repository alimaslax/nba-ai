package com.example.restservice;

import java.util.Map;
import java.util.concurrent.atomic.AtomicLong;

import org.springframework.web.bind.annotation.*;

@RestController
public class AnswerController {

    private static final String template = "Hello, %s!";
    private final AtomicLong counter = new AtomicLong();

    // create a new controller method with url stats that is a POST method
    @RequestMapping(value = "/stats", method = RequestMethod.POST)
    public Answer process(@RequestBody Map<String, Object> payload) throws Exception {
        // return a new Answer object with the id and content where
        // the content is the value of the payload key "msg"
        // and the id is the next value of the counter
        return new Answer(counter.incrementAndGet(), payload.get("msg").toString());
    }

}
