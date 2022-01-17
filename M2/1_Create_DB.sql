drop database if exists PROJECT_1;
create database PROJECT_1;

use PROJECT_1;

create table USER (
 id_user Int,
 username varchar(20),
 password varchar(20)
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
 
 create table CHARACTER_ADVENTURE (
 id_character int,
 id_adventure int
 );
 
 create table STEP (
 id_step int,
 description varchar(150),
 adventure_end bit(1),
 id_adventure int
 );
 
 create table OPTIONS (
 id_option int,
 description varchar(150),
 answer varchar(50),
 id_step int
 );

 create table ROUND (
 id_round int,
 date datetime,
 time datetime,
 id_user int,
 id_characters int,
 id_adventure int
 );
 
 create table ROUND_OPTIONS (
 id_round int,
 id_options int
 );