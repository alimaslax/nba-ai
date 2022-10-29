# nba-ai

[Open Ai](https://openai.com/api/)'s gp3 implementation of an nba api

## Requirements

- Java 8
- sqlite3
- Datasource : https://www.kaggle.com/datasets/wyattowalsh/basketball?resource=download

# Nerdctl

nerdctl compose -f sql-compose.yaml up -d
nerdctl ps | nerdctl stop
Required Readings

# MySql Containers

The configuration for the mysql container can be found here, etc/my.cnf

## Nerctl commands

```Bash
nerdctl compose -f sql-compose.yaml up -d --remove-orphans
```

Start Container

```Bash
nerdctl compose -f sql-compose.yaml down
```

Stop Container

```Bash
nerdctl exec -it nba-ai bash
```

Login into pod

```Bash
nerdctl exec CONTAINER /usr/bin/mysqldump -u root --password=$SQLPASS DATABASE > backup.sql
```

Make a back up the database

```Bash
cat backup.sql | nerdctl exec -i CONTAINER /usr/bin/mysql -u root --password=$SQLPASS DATABASE
```

restore a backup to the database

Readings
https://dev.mysql.com/doc/refman/8.0/en/identifier-case-sensitivity.html

https://hub.docker.com/_/mysql
ip addr show eth0

Note
https://stackoverflow.com/questions/6134006/are-table-names-in-mysql-case-sensitive

---

JAVA PROJECT
importing sqlite database
https://dba.stackexchange.com/questions/153719/import-db-files-tables-into-sqlite-database

jdbc uri
https://www.sqlitetutorial.net/sqlite-java/sqlite-jdbc-driver/

connect spring-boot to sqlite
https://www.baeldung.com/spring-boot-sqlite

Data Information
sqlite> .tables
Draft News_Missing Team  
Draft_Combine Player Team_Attributes  
Game Player_Attributes Team_History  
Game_Inactive_Players Player_Bios Team_Salary  
Game_Officials Player_Photos  
News Player_Salary

## Schemas

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
