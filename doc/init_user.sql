CREATE TABLE "T_USER" (
	user VARCHAR(20) NOT NULL, 
	name VARCHAR(20), 
	role VARCHAR(20), 
	password VARCHAR(16), 
	PRIMARY KEY (user)
);

insert into t_user (user, name, role, password) values ('admin', 'admin', 'admin', '111111');
insert into t_user (user, name, role, password) values ('demo', 'demo', 'user', '111111');
