-- Run in MySQL Workbench to create the Database -->
-- Note: The above is no longer needed as I have made it possible to create the DB from the models.py file


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

-- create an index for User Attempt column
CREATE INDEX idx_UserAttempt
ON the_users (UserAttempt);


