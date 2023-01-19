-- Creation TED Database.

Create Database TED;

-- Creating tedauthor table into TED database.

Create table TED.tedauthor(
Author_id varchar(50) primary key,
Author varchar(255));


-- Creating tedshows table into TED database.

Create table TED.tedshows(
Title_id int primary key,
Title varchar(255),
Author_id varchar(50),
show_date date,
Views int,
Likes int,
Link varchar(255),
CONSTRAINT FK_author FOREIGN KEY (Author_id)
REFERENCES tedauthor(Author_id));

