INSERT INTO `user` (`first_name`, `last_name`, `phone`, `email`, `password`, `birth_date`, `join_date`) 
VALUES 
	('Neil', 'Joseph John', '97150 123 4567', 'some@email.com', 'abc.123', '2012-02-23', '2019-11-29');
	
insert into `live_state`
values 
	(1, 'Connected', 'System is connected'),
	(2, 'Offline', 'System is offline');

insert into `indicator`
values 
	(1, 'Up', 'Arrow is up'),
	(2, 'Up Right', 'Arrow is up right'),
	(3, 'Right', 'Arrow is right'),
	(4, 'Down Right', 'Arrow is down right'),
	(5, 'Down', 'Arrow is down'),
	(6, 'Down Left', 'Arrow is down left'),
	(7, 'Left', 'Arrow is left'),
	(8, 'Up Left', 'Arrow is up left');


INSERT INTO `live_data` (`user_id`, `glucose`, `glucose_unit`, `glucose_indicator`, `state`) 
VALUES
    ((select `id` from `user` where `first_name` = 'Neil'), 104, 'mg/dl', (select `id` from `indicator` where `name` = 'Up Right'), (select `id` from `live_state` where `name` = 'Connected'));
    
CREATE TABLE `level` (
  `id` tinyint(4) NOT NULL,
  `name` varchar(30) NOT NULL,
  `description` varchar(60) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;    
    
CREATE TABLE `event` (
  `id` tinyint(4) NOT NULL,
  `name` varchar(30) NOT NULL,
  `type` varchar(30) NOT NULL,
  `description` varchar(60) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;    
    
DROP TABLE IF EXISTS `forecast_state`;    
DROP TABLE IF EXISTS `forecast_learned`;    
CREATE TABLE `forecast_state` (
  `id` tinyint(4) NOT NULL,
  `name` varchar(30) NOT NULL,
  `description` varchar(60) DEFAULT NULL,
  `low` int NOT NULL,
  `high` int NOT NULL,
  `level` tinyint(4) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `fk_fs_1` (`level`),
  CONSTRAINT `fk_fs_1` FOREIGN KEY (`level`) REFERENCES `level` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;    
    
CREATE TABLE `forecast_learned` (
  `id` tinyint(4) NOT NULL,
  `name` varchar(30) NOT NULL,
  `description` varchar(60) DEFAULT NULL,
  `low` int NOT NULL,
  `high` int NOT NULL,
  `level` tinyint(4) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `fk_fl_1` (`level`),
  CONSTRAINT `fk_fl_1` FOREIGN KEY (`level`) REFERENCES `level` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;    
    
insert into `level`
values 
	(1, 'HIGH', 'High'),
	(2, 'MED', 'Medium'),
	(3, 'LOW', 'Low');

insert into `event`
values 
	(1, 'hypoglycemia', 'glucose', 'hypoglycemia'),
	(2, 'hyperglycemia', 'glucose', 'hyperglycemia');

insert into `forecast_state`
values 
	(1, 'HYPOGLYCEMIA', 'Hypoglycemia', 0, 50, (select `id` from `level` where `name` = 'LOW')),
	(2, 'HYPERGLYCEMIA', 'Hyperglycemia', 51, 100, (select `id` from `level` where `name` = 'HIGH'));

insert into `forecast_learned`
values 
	(1, 'Learning', 'Algorith is learning', 0, 40, (select `id` from `level` where `name` = 'LOW')),
	(2, 'Learned', 'Algorith has learned', 41, 60, (select `id` from `level` where `name` = 'MED')),
	(3, 'Mastered', 'Algorithm has mastered', 61, 100, (select `id` from `level` where `name` = 'HIGH'));

delete from `user_2_forecast`;
INSERT INTO `forecast` (`interval`, `interval_unit`, `value`, `unit`, `percent`, `state`, `state_percent`, `learned`, `learned_percent`, `level`) 
VALUES
    (60, 'min', 135, 'mg/dl', 59, (select `id` from `forecast_state` where `name` = 'HYPOGLYCEMIA'), 42, (select `id` from `forecast_learned` where `name` = 'Learned'), 50, 1),
    (60, 'min', 155, 'mg/dl', 69, (select `id` from `forecast_state` where `name` = 'HYPOGLYCEMIA'), 42, (select `id` from `forecast_learned` where `name` = 'Learned'), 50, 1);
    
INSERT INTO `user_2_forecast` (`user_id`, `forecast_id`) 
VALUES
    ((select `id` from `user` where `first_name` = 'Neil'), (select `id` from `forecast` where `percent` = 59)),
    ((select `id` from `user` where `first_name` = 'Neil'), (select `id` from `forecast` where `percent` = 69));

INSERT INTO `user_2_glucose` (`user_id`, `glucose_id`) 
VALUES
    ((select `id` from `user` where `first_name` = 'Neil'), (select `id` from `glucose` where `percent` = 59)),
    ((select `id` from `user` where `first_name` = 'Neil'), (select `id` from `glucose` where `percent` = 69));

INSERT INTO `glucose` (`when`, `value`, `unit`, `event`) 
VALUES
    ((select now()-2), 110, 'mg/dl', (select `id` from `event` where `name` = 'hypoglycemia' and `type` = 'glucose')),
    ((select now()-2), 100, 'mg/dl', (select `id` from `event` where `name` = 'hyperglycemia' and `type` = 'glucose')),
    ((select now()-1), 94, 'mg/dl', (select `id` from `event` where `name` = 'hypoglycemia' and `type` = 'glucose')),
    ((select now()-3), 100, 'mg/dl', (select `id` from `event` where `name` = 'hypoglycemia' and `type` = 'glucose')),
    ((select now()), 96, 'mg/dl', (select `id` from `event` where `name` = 'hyperglycemia' and `type` = 'glucose')),
    ((select now()+1), 98, 'mg/dl', (select `id` from `event` where `name` = 'hypoglycemia' and `type` = 'glucose')),
    ((select now()+2), 94, 'mg/dl', (select `id` from `event` where `name` = 'hyperglycemia' and `type` = 'glucose')),
    ((select now()+2), 94, 'mg/dl', (select `id` from `event` where `name` = 'hypoglycemia' and `type` = 'glucose')),
    ((select now()-1), 99, 'mg/dl', (select `id` from `event` where `name` = 'hyperglycemia' and `type` = 'glucose')),
    ((select now()), 94, 'mg/dl', (select `id` from `event` where `name` = 'hypoglycemia' and `type` = 'glucose')),
    ((select now()), 94, 'mg/dl', (select `id` from `event` where `name` = 'hyperglycemia' and `type` = 'glucose')),
    ((select now()), 88, 'mg/dl', (select `id` from `event` where `name` = 'hyperglycemia' and `type` = 'glucose')),
    ((select now()), 91, 'mg/dl', (select `id` from `event` where `name` = 'hypoglycemia' and `type` = 'glucose')),
    ((select now()), 94, 'mg/dl', (select `id` from `event` where `name` = 'hypoglycemia' and `type` = 'glucose')),
    ((select now()), 99, 'mg/dl', (select `id` from `event` where `name` = 'hyperglycemia' and `type` = 'glucose')),
    ((select now()), 94, 'mg/dl', (select `id` from `event` where `name` = 'hypoglycemia' and `type` = 'glucose')),
    ((select now()), 94, 'mg/dl', (select `id` from `event` where `name` = 'hyperglycemia' and `type` = 'glucose')),
    ((select now()), 88, 'mg/dl', (select `id` from `event` where `name` = 'hyperglycemia' and `type` = 'glucose')),
    ((select now()), 91, 'mg/dl', (select `id` from `event` where `name` = 'hypoglycemia' and `type` = 'glucose')),
    ((select now()), 94, 'mg/dl', (select `id` from `event` where `name` = 'hypoglycemia' and `type` = 'glucose')),
    ((select now()), 99, 'mg/dl', (select `id` from `event` where `name` = 'hyperglycemia' and `type` = 'glucose')),
    ((select now()), 94, 'mg/dl', (select `id` from `event` where `name` = 'hypoglycemia' and `type` = 'glucose')),
    ((select now()), 94, 'mg/dl', (select `id` from `event` where `name` = 'hyperglycemia' and `type` = 'glucose')),
    ((select now()), 88, 'mg/dl', (select `id` from `event` where `name` = 'hyperglycemia' and `type` = 'glucose')),
    ((select now()), 91, 'mg/dl', (select `id` from `event` where `name` = 'hypoglycemia' and `type` = 'glucose')),
    ((select now()), 94, 'mg/dl', (select `id` from `event` where `name` = 'hypoglycemia' and `type` = 'glucose')),
    ((select now()), 99, 'mg/dl', (select `id` from `event` where `name` = 'hyperglycemia' and `type` = 'glucose')),
    ((select now()), 94, 'mg/dl', (select `id` from `event` where `name` = 'hypoglycemia' and `type` = 'glucose')),
    ((select now()), 94, 'mg/dl', (select `id` from `event` where `name` = 'hyperglycemia' and `type` = 'glucose')),
    ((select now()), 88, 'mg/dl', (select `id` from `event` where `name` = 'hyperglycemia' and `type` = 'glucose')),
    ((select now()), 91, 'mg/dl', (select `id` from `event` where `name` = 'hypoglycemia' and `type` = 'glucose'));
    
INSERT INTO `user_2_forecast` (`user_id`, `forecast_id`) 
VALUES
    ((select `id` from `user` where `first_name` = 'Neil'), (select `id` from `forecast` where `percent` = 59)),
    ((select `id` from `user` where `first_name` = 'Neil'), (select `id` from `forecast` where `percent` = 69));

insert into `activity_type`
values 
	(1, 'Eat', 'Eat Activity', '#25cb80'),
	(2, 'Exercise', 'Physical Activity', '#2d85c3'),
	(3, 'Insulin', 'Dose Activity', '#FBDF00'),
	(4, 'Rest', 'Relaxation Activity', '#F5005C');


CREATE TABLE `activity_state` (
  `id` tinyint(4) NOT NULL,
  `name` varchar(30) NOT NULL,
  `description` varchar(60) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

delete from `activity_state`;
insert into `activity_state`
values 
	(1, 'Enabled', 'Enabled'),
	(2, 'Disabled', 'Disabled'),
	(3, 'Complete', 'Complete'),
	(4, 'Incomplete', 'Incomplete');

insert into `device`
values 
	(1, 'FreeStyle Libre', 'FreeStyle Libre');

LOAD DATA LOCAL INFILE '/Users/axv/Dropbox/_SLF/_DATA/Glucose data/04012020/neil_glucose_1-4-2020.csv' 
INTO TABLE `activity` FIELDS TERMINATED BY ',' LINES TERMINATED BY '\r\n' IGNORE 2 LINES
(`device`, `serial_num`, `datetime`, `record_type`, `glucose`, `glucose_unit`, `scang`, `scang_unit`, `rai`, `rai_unit`, `food`, `carbs`, `carbs_unit`, `lai`, `lai_unit`, `stripg`, `stripg_unit`, `ketone`, `ketone_unit`, `mi`, `mi_unit`, `ci`, `ci_unit`, `uci`, `uci_unit`, `notes`, `state`, `when`, `who`)
SET `notes` = null, `state` = 1, `who` = 'sys';

insert into `activity_log`
	(`date`)
values 
	('2019-12-29 00:00:00'),
	('2019-12-30 00:00:00'),
	('2019-12-31 00:00:00');
	
insert into `activity_log_detail`
	(`time`, `value`, `radius`, `type`, `state`)
values 
	('07:00:00', 110, 5, (select `id` from `activity_type` where `name` = 'Eat'), (select `id` from `activity_state` where `name` = 'Complete')),
	('07:00:00', 60, 5, (select `id` from `activity_type` where `name` = 'Exercise'), (select `id` from `activity_state` where `name` = 'Complete')),
	('07:00:00', 10, 5, (select `id` from `activity_type` where `name` = 'Insulin'), (select `id` from `activity_state` where `name` = 'Complete')),
	('08:00:00', 40, 5, (select `id` from `activity_type` where `name` = 'Exercise'), (select `id` from `activity_state` where `name` = 'Complete')),
	('08:00:00', 90, 5, (select `id` from `activity_type` where `name` = 'Insulin'), (select `id` from `activity_state` where `name` = 'Complete')),
	('09:00:00', 140, 5, (select `id` from `activity_type` where `name` = 'Eat'), (select `id` from `activity_state` where `name` = 'Complete')),
	('09:00:00', 90, 5, (select `id` from `activity_type` where `name` = 'Exercise'), (select `id` from `activity_state` where `name` = 'Complete')),
	('09:00:00', 40, 5, (select `id` from `activity_type` where `name` = 'Insulin'), (select `id` from `activity_state` where `name` = 'Complete')),
	('10:00:00', 225, 5, (select `id` from `activity_type` where `name` = 'Rest'), (select `id` from `activity_state` where `name` = 'Complete')),
	('10:00:00', 175, 5, (select `id` from `activity_type` where `name` = 'Eat'), (select `id` from `activity_state` where `name` = 'Complete')),
	('10:00:00', 125, 5, (select `id` from `activity_type` where `name` = 'Exercise'), (select `id` from `activity_state` where `name` = 'Complete')),
	('10:00:00', 75, 5, (select `id` from `activity_type` where `name` = 'Insulin'), (select `id` from `activity_state` where `name` = 'Complete')),
	('11:00:00', 60, 5, (select `id` from `activity_type` where `name` = 'Eat'), (select `id` from `activity_state` where `name` = 'Complete')),
	('12:00:00', 125, 5, (select `id` from `activity_type` where `name` = 'Eat'), (select `id` from `activity_state` where `name` = 'Complete')),
	('12:00:00', 75, 5, (select `id` from `activity_type` where `name` = 'Exercise'), (select `id` from `activity_state` where `name` = 'Complete')),
	('12:00:00', 25, 5, (select `id` from `activity_type` where `name` = 'Insulin'), (select `id` from `activity_state` where `name` = 'Complete'));
	


CREATE TABLE `forecast` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `interval` int(3) DEFAULT '0',
  `interval_unit` varchar(10) DEFAULT NULL,
  `value` int(3) DEFAULT '0',
  `unit` varchar(10) DEFAULT NULL,
  `percent` tinyint(4) DEFAULT '1',
  `state` tinyint(4) DEFAULT '1',
  `state_percent` tinyint(4) DEFAULT '0',
  `learned` tinyint(4) DEFAULT '1',
  `learned_percent` tinyint(4) DEFAULT '0',
  `level` tinyint(4) DEFAULT '1',
  PRIMARY KEY (`id`),
  KEY `fk_f_1` (`state`),
  KEY `fk_f_2` (`learned`),
  CONSTRAINT `fk_f_1` FOREIGN KEY (`state`) REFERENCES `forecast_state` (`id`),
  CONSTRAINT `fk_f_2` FOREIGN KEY (`learned`) REFERENCES `forecast_learned` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;


CREATE TABLE `device` (
  `id` tinyint(4) NOT NULL,
  `name` varchar(30) NOT NULL,
  `description` varchar(60) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

CREATE TABLE `indicator` (
  `id` tinyint(4) NOT NULL,
  `name` varchar(30) NOT NULL,
  `description` varchar(60) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

ALTER TABLE `live_data` ADD CONSTRAINT `fk_ld_3` FOREIGN KEY (`glucose_indicator`) REFERENCES `indicator`(`id`);

CREATE TABLE `glucose_mode` (
  `id` tinyint(4) NOT NULL,
  `name` varchar(30) NOT NULL,
  `description` varchar(60) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

CREATE TABLE `glucose` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `when` timestamp DEFAULT CURRENT_TIMESTAMP,
  `value` int(3) DEFAULT '0',
  `unit` varchar(10) DEFAULT NULL,
  `event` tinyint(4),
  PRIMARY KEY (`id`),
  KEY `fk_g_1` (`event`),
  CONSTRAINT `fk_g_1` FOREIGN KEY (`event`) REFERENCES `event` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

CREATE TABLE `activity_log_detail` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `time` time NOT NULL,
  `value` int(3) NOT NULL,
  `radius` tinyint(4) DEFAULT NULL,
  `type` tinyint(4) NOT NULL,
  `state` tinyint(4) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `fk_ald_1` (`type`),
  CONSTRAINT `fk_ald_1` FOREIGN KEY (`type`) REFERENCES `activity_type` (`id`),
  KEY `fk_ald_2` (`state`),
  CONSTRAINT `fk_ald_2` FOREIGN KEY (`state`) REFERENCES `activity_state` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

CREATE TABLE `activity_action` (
  `id` tinyint(4) NOT NULL,
  `name` varchar(30) NOT NULL,
  `description` varchar(60) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

CREATE TABLE `activity_how` (
  `id` tinyint(4) NOT NULL,
  `name` varchar(30) NOT NULL,
  `description` varchar(60) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

CREATE TABLE `activity_recommended` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `when` timestamp NOT NULL,
  `type` tinyint(4) NOT NULL,
  `action` tinyint(4) DEFAULT NULL,
  `how` tinyint(4) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `fk_ar_1` (`type`),
  CONSTRAINT `fk_ar_1` FOREIGN KEY (`type`) REFERENCES `activity_type` (`id`),
  KEY `fk_ar_2` (`action`),
  CONSTRAINT `fk_ar_2` FOREIGN KEY (`action`) REFERENCES `activity_action` (`id`),
  KEY `fk_ar_3` (`how`),
  CONSTRAINT `fk_ar_3` FOREIGN KEY (`how`) REFERENCES `activity_how` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

insert into `activity_action`
values 
	(1, 'COOK', 'Cook');

insert into `activity_how`
values 
	(1, 'EAT OUT', 'Eat at a restaurant'),
	(2, 'EAT HOME', 'Eat at home');


insert into `activity_recommended`
	(`when`, `type`, `action`, `how`)
values 
	('2019-12-29 00:00:00', (select `id` from `activity_type` where `name` = 'Eat'), (select `id` from `activity_action` where `name` = 'COOK'), (select `id` from `activity_how` where `name` = 'EAT OUT'));

CREATE TABLE `user_2_glucose` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `user_id` int(11) unsigned NOT NULL,
  `glucose_id` int(11) unsigned NOT NULL,
  PRIMARY KEY (`id`),
  KEY `fk_ug_1` (`user_id`),
  KEY `fk_ug_2` (`glucose_id`),
  CONSTRAINT `fk_ug_1` FOREIGN KEY (`user_id`) REFERENCES `user` (`id`),
  CONSTRAINT `fk_ug_2` FOREIGN KEY (`glucose_id`) REFERENCES `glucose` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8;

CREATE TABLE `user_2_activity_log` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `user_id` int(11) unsigned NOT NULL,
  `activity_log_id` int(11) unsigned NOT NULL,
  PRIMARY KEY (`id`),
  KEY `fk_ual_1` (`user_id`),
  KEY `fk_ual_2` (`activity_log_id`),
  CONSTRAINT `fk_ual_1` FOREIGN KEY (`user_id`) REFERENCES `user` (`id`),
  CONSTRAINT `fk_ual_2` FOREIGN KEY (`activity_log_id`) REFERENCES `activity_log` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8;

CREATE TABLE `user_2_activity_recommended` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `user_id` int(11) unsigned NOT NULL,
  `activity_recommended_id` int(11) unsigned NOT NULL,
  PRIMARY KEY (`id`),
  KEY `fk_uar_1` (`user_id`),
  KEY `fk_uar_2` (`activity_recommended_id`),
  CONSTRAINT `fk_uar_1` FOREIGN KEY (`user_id`) REFERENCES `user` (`id`),
  CONSTRAINT `fk_uar_2` FOREIGN KEY (`activity_recommended_id`) REFERENCES `activity_recommended` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8;

delete from `activity`;

select record_type, count(*)
  from `activity` group by record_type;
  
select * from `activity` where `record_type` = 0;

select a.* from `activity` as a where id in (
	select max(id) as id from `activity` group by record_type
);
select record_type, max(id) as max from `activity` group by record_type;

select str_to_date(datetime, 'DD-MM-YYYY HH24:MI') from `activity` limit 10;

insert into `live_data` (`user_id`, `glucose`, `glucose_unit`, `glucose_indicator`, `state`) 
values ((select `id` from `user` where `first_name` = 'Neil'), (select `glucose` from `activity` where id = (select max(id) from `activity` where `record_type` = 0)), 'mg/dl', (select `id` from `indicator` where `name` = 'Up Right'), (select `id` from `live_state` where `name` = 'Offline'));


  
