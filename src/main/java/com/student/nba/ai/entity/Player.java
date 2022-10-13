package com.student.nba.ai.entity;

import javax.persistence.Entity;
import javax.persistence.GeneratedValue;
import javax.persistence.GenerationType;
import javax.persistence.Id;
import java.io.Serializable;


// Table Player columns = [id, full_name, first_name, last_name, is_active]
// create an entity class for Player and add the appropriate annotations add the getters and setters for the fields
@Entity
public class Player implements Serializable {
    @Id
    @GeneratedValue(strategy = GenerationType.AUTO)
    private String id;
    private String full_name;
    private String first_name;
    private String last_name;
    private int is_active;
    // create protected no-arg constructor
    protected Player() {
    }
    // create constructor
    public Player(String id, String full_name, String first_name, String last_name, int is_active) {
        this.id = id;
        this.full_name = full_name;
        this.first_name = first_name;
        this.last_name = last_name;
        this.is_active = is_active;
    }

    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }

    public String getFull_name() {
        return full_name;
    }

    public void setFull_name(String full_name) {
        this.full_name = full_name;
    }

    public String getFirst_name() {
        return first_name;
    }

    public void setFirst_name(String first_name) {
        this.first_name = first_name;
    }

    public String getLast_name() {
        return last_name;
    }

    public void setLast_name(String last_name) {
        this.last_name = last_name;
    }

    public int isIs_active() {
        return is_active;
    }

    public void setIs_active(int is_active) {
        this.is_active = is_active;
    }
}