create table COMMENT (
	id NOT NULL AUTO_INCREMENT,
	username VARCHAR(50),
	value VARCHAR(250)
);
insert into COMMENT (username, value) values ("test", "A message from the past");
insert into COMMENT (username, value) values ("Ekko", "A message from the past");
insert into COMMENT (username, value) values ("test_3", "I'm from the futur for a change");


