
-- Part 1 Create the Database
CREATE DATABASE tempGuess_user;
USE tempGuess_user;


-- Part 2 Creating the Database Table
CREATE TABLE the_user (
    UserAttempt int AUTO_INCREMENT NOT NULL UNIQUE,
	UserGuess int NOT NULL,
    ActualTemp int NOT NULL,
    DateTime DATETIME NOT NULL,
    CONSTRAINT pk_the_user PRIMARY KEY (UserAttempt),
    INDEX idx_UserAttempt (UserAttempt) -- create an index for User Attempt column

);




