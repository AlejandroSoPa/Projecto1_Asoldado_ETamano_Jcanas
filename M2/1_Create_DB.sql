drop database if exists PROJECT_1;
create database PROJECT_1;

use PROJECT_1;

alter database PROJECT_1 character set utf8mb4;

create table if not exists USER (
 ID_USER Int,
 username varchar(20),
 password varchar(20),
 usercreate varchar(20),
 usermodify varchar(20),
 datecreated datetime,
 datemodified datetime
 );
 
 create table if not exists PROJECT_1.CHARACTER (
 ID_CHARACTER int,
 name varchar(20),
 description varchar(750),
 usercreate varchar(20),
 usermodify varchar(20),
 datecreated datetime,
 datemodified datetime
 );
 
 create table if not exists ADVENTURE (
 ID_ADVENTURE int,
 name varchar(20),
 description varchar(750),
 usercreate varchar(20),
 usermodify varchar(20),
 datecreated datetime,
 datemodified datetime
 );
 
 create table if not exists CHARACTER_ADVENTURE (
 ID_CHARACTER int,
 ID_ADVENTURE int,
 usercreate varchar(20),
 usermodify varchar(20),
 datecreated datetime,
 datemodified datetime
 );
 
 create table if not exists STEP (
 ID_STEP int,
 description varchar(750),
 adventure_end bit(1),
 ID_ADVENTURE int,
 usercreate varchar(20),
 usermodify varchar(20),
 datecreated datetime,
 datemodified datetime
 );
 
 create table if not exists PROJECT_1.OPTION (
 ID_OPTION int,
 description varchar(750),
 answer varchar(50),
 next_step int,
 ID_STEP int,
 usercreate varchar(20),
 usermodify varchar(20),
 datecreated datetime,
 datemodified datetime
 );

 create table if not exists ROUND (
 ID_ROUND int,
 date datetime,
 time datetime,
 ID_USER int,
 ID_CHARACTER int,
 ID_ADVENTURE int,
 usercreate varchar(20),
 usermodify varchar(20),
 datecreated datetime,
 datemodified datetime
 );
 
 create table if not exists ROUND_OPTION (
 ID_ROUND int,
 ID_OPTION int,
 usercreate varchar(20),
 usermodify varchar(20),
 datecreated datetime,
 datemodified datetime
 );