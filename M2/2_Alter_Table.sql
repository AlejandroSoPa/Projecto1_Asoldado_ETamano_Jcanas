use PROJECT_1;

alter table USER
modify id_user int primary key not null unique auto_increment,
modify username varchar(20) not null unique,
modify password varchar(20) not null;

alter table ROUND
modify id_round int primary key not null unique auto_increment,
modify date datetime not null unique,
modify time datetime not null;

alter table CHARACTERS
modify id_character int primary key not null unique auto_increment,
modify name varchar(20) not null unique,
modify description varchar(150) not null unique;

alter table ADVENTURE
modify id_adventure int primary key not null unique auto_increment,
modify name varchar(20) unique not null,
modify description varchar(150) unique not null;

alter table STEP
modify id_step int primary key not null auto_increment,
modify description varchar(150) not null,
modify adventure_end bit(1) not null;

alter table OPTIONS
modify id_option int primary key not null auto_increment,
modify description varchar(150) not null,
modify answer varchar(50) not null;