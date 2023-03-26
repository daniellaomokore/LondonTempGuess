-- Run in MySQL Workbench to create the Database


-- Part 1 Create the Database
CREATE DATABASE tempGuess_user;

USE tempGuess_user;

-- Part 2 Creating the Database Table

CREATE TABLE the_user (
    UserAttempt int(10) AUTO_INCREMENT NOT NULL UNIQUE,
	UserGuess int(10) NOT NULL,
    ActualTemp int(10) NOT NULL,
    DateTime DATETIME NOT NULL,
    CONSTRAINT pk_the_user PRIMARY KEY (UserAttempt)

);