package com.student.nba.ai.repository;

import com.student.nba.ai.entity.Player;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

// repository class called PlayerRepository that extends the JpaRepository interface
public interface PlayerRepository extends JpaRepository<Player, String> {

}