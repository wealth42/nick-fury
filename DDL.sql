create database if not exists bikepoint;
use bikepoint;
drop table if exists point;
drop table if exists addons;
CREATE TABLE IF NOT EXISTS `point` (
	`id` VARCHAR(300) unique,
	`url` VARCHAR(300) NULL,
	`commonName` VARCHAR(300) NULL,
	`placeType` VARCHAR(300) NULL,
	`children` JSON NULL,
	`childrenUrls` JSON NULL,	
	`lat` FLOAT NULL,
	`lon` FLOAT NULL,
	`bikes` int NULL,
	`spaces` int NULL,
	`docks` int NULL,
	  CONSTRAINT prkey1 PRIMARY KEY (id)
);
CREATE TABLE IF NOT EXISTS `addons` (
	`id` VARCHAR(300) not null,
	`category` VARCHAR(300) NULL,
	`skey` VARCHAR(300) not NULL,
	`sourceSystemKey` VARCHAR(300) NULL,
	`value` VARCHAR(300) NULL,
	`modified` varchar(30) NULL,
	  CONSTRAINT prkey2 PRIMARY KEY (id,skey)
);
