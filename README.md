# nba-ai
openapi's gp3 implementation of an nba api

Requirements
------------
- Java 8
- Sqlite3
- sqlite3
- Datasource : https://www.kaggle.com/datasets/wyattowalsh/basketball?resource=download



Required Readings
---
importing sqlite database
https://dba.stackexchange.com/questions/153719/import-db-files-tables-into-sqlite-database

jdbc uri
https://www.sqlitetutorial.net/sqlite-java/sqlite-jdbc-driver/

connect spring-boot to sqlite
https://www.baeldung.com/spring-boot-sqlite


Data Information
sqlite> .tables
Draft                  News_Missing           Team                 
Draft_Combine          Player                 Team_Attributes      
Game                   Player_Attributes      Team_History         
Game_Inactive_Players  Player_Bios            Team_Salary          
Game_Officials         Player_Photos        
News                   Player_Salary

Schemas
---
Draft
`Draft` (
  `yearDraft` REAL,
  `numberPickOverall` REAL,
  `numberRound` REAL,
  `numberRoundPick` REAL,
  `namePlayer` TEXT,
  `slugTeam` TEXT,
  `nameOrganizationFrom` TEXT,
  `typeOrganizationFrom` TEXT,
  `idPlayer` REAL,
  `idTeam` REAL,
  `nameTeam` TEXT,
  `cityTeam` TEXT,
  `teamName` TEXT,
  `PLAYER_PROFILE_FLAG` REAL,
  `slugOrganizationTypeFrom` TEXT,
  `locationOrganizationFrom` TEXT
);

