use PROJECT_1;

alter table USER
modify ID_USER int primary key not null unique auto_increment,
modify username varchar(20) not null unique,
modify password varchar(20) not null,
modify usercreate varchar(20) not null,
modify usermodify varchar(20),
modify datecreated datetime not null,
modify datemodified datetime;

alter table PROJECT_1.CHARACTER
modify ID_CHARACTER int primary key not null unique auto_increment,
modify name varchar(20) not null unique,
modify description varchar(750) not null unique,
modify usercreate varchar(20) not null,
modify usermodify varchar(20),
modify datecreated datetime not null,
modify datemodified datetime;

alter table ADVENTURE
modify ID_ADVENTURE int primary key not null unique auto_increment,
modify name varchar(20) unique not null,
modify description varchar(750) unique not null,
modify usercreate varchar(20) not null,
modify usermodify varchar(20),
modify datecreated datetime not null,
modify datemodified datetime;

alter table CHARACTER_ADVENTURE
add constraint fk_CHARACTER_ADVENTURE_character foreign key (id_character) references PROJECT_1.CHARACTER(id_character),
add constraint fk_CHARACTER_ADVENTURE_adventure foreign key (id_adventure) references ADVENTURE(id_adventure),
modify usercreate varchar(20) not null,
modify usermodify varchar(20),
modify datecreated datetime not null,
modify datemodified datetime;

alter table STEP
modify ID_STEP int primary key not null auto_increment,
modify description varchar(750) not null unique,
modify adventure_end bit(1) not null,
add constraint fk_step_adventure foreign key (id_adventure) references ADVENTURE(id_adventure),
modify usercreate varchar(20) not null,
modify usermodify varchar(20),
modify datecreated datetime not null,
modify datemodified datetime;

alter table PROJECT_1.OPTION
modify ID_OPTION int primary key not null auto_increment,
modify description varchar(750) not null unique,
modify answer varchar(50) not null,
modify next_step int not null,
add constraint fk_options_step foreign key (id_step) references STEP(id_step),
modify usercreate varchar(20) not null,
modify usermodify varchar(20),
modify datecreated datetime not null,
modify datemodified datetime;

alter table ROUND
modify ID_ROUND int primary key not null unique auto_increment,
modify date datetime not null unique,
modify time datetime not null,
add constraint fk_round_user foreign key (id_user) references USER(id_user),
add constraint fk_round_character foreign key (id_character) references PROJECT_1.CHARACTER(id_character),
add constraint fk_round_adventure foreign key (id_adventure) references ADVENTURE(id_adventure),
modify usercreate varchar(20) not null,
modify usermodify varchar(20),
modify datecreated datetime not null,
modify datemodified datetime
;