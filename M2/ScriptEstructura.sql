drop database if exists PROJECT_1;
create database PROJECT_1;

use PROJECT_1;

create table USER (
 id_user Int,
 username varchar(20),
 password varchar(20)
 );
 
 create table ROUND (
 id_round int,
 date datetime,
 time datetime
 );
 
 create table CHARACTERS (
 id_character int,
 name varchar(20),
 description varchar(150)
 );
 
 create table ADVENTURE (
 id_adventure int,
 name varchar(20),
 description varchar(150)
 );
 
 create table STEP (
 id_step int,
 description varchar(150),
 adventure_end bit(1));
 
 create table OPTIONS (
 id_option int,
 description varchar(150),
 answer varchar(50)
 );