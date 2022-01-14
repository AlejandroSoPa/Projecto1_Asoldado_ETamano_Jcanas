drop database if exists PROJECT_1;
create database PROJECT_1;

use PROJECT_1;

create table USER (
 id_user Int auto_increment primary key,
 username varchar(40) unique not null,
 password varchar(20) not null
 );
 
 create table ROUND (
 id_round int auto_increment primary key,
 date datetime not null,
 time datetime not null
 );
 
 create table CHARACTERS (
 id_character int auto_increment primary key,
 name varchar(45) unique not null,
 description varchar(45) unique not null
 );
 
 create table ADVENTURE (
 id_adventure int auto_increment primary key,
 name varchar(45) unique not null,
 description varchar(45) unique not null
 );
 
 create table STEP (
 id_step int auto_increment primary key,
 description varchar(45) unique not null,
 adventure_end bit(1) not null);
 
 create table OPTIONS (
 id_option int auto_increment primary key,
 description varchar(45) not null,
 answer varchar(45) not null
 );