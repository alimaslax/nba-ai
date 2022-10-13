package com.student.nba.ai.controllers;

import java.util.Map;
import java.util.concurrent.atomic.AtomicLong;

import com.student.nba.ai.entity.Player;
import com.student.nba.ai.models.Answer;
import com.student.nba.ai.repository.PlayerRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;

import javax.sql.DataSource;

@RestController
public class AnswerController {

    // autowire the PlayerRepository
    @Autowired
    private PlayerRepository playerRepository;

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
    @GetMapping(path="/all")
    public @ResponseBody Iterable<Player> getAllPlayers() {
        // This returns a JSON or XML with the users
        return playerRepository.findAll();
    }

}
