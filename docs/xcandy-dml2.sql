ALTER TABLE `live_data` DROP COLUMN `sys_time`;
ALTER TABLE `live_data` DROP COLUMN `user_id`;

ALTER TABLE `forecast` DROP COLUMN `state`;
ALTER TABLE `forecast` DROP COLUMN `state_percent`;
ALTER TABLE `forecast` DROP COLUMN `learned`;
ALTER TABLE `forecast` DROP COLUMN `learned_percent`;
ALTER TABLE `forecast` DROP COLUMN `level`;

CREATE TABLE `forecast1` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `since` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `when` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `interval` int(3) DEFAULT '0',
  `interval_unit` varchar(10) DEFAULT NULL,
  `value` int(3) DEFAULT '0',
  `unit` varchar(10) DEFAULT NULL,
  `percent` tinyint(4) DEFAULT '1',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=0 DEFAULT CHARSET=utf8;

insert into `forecast1` (`since`, `when`, `interval`, `interval_unit`, `value`, `unit`, `percent`)
select `since`, `when`, `interval`, `interval_unit`, `value`, `unit`, `percent` from `forecast`;

ALTER TABLE `live_data` ADD COLUMN `since` timestamp AFTER `id`;
ALTER TABLE `live_data` ADD COLUMN `when` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP AFTER `since`;
ALTER TABLE `forecast` ADD COLUMN `since` timestamp AFTER `id`;
ALTER TABLE `forecast` ADD COLUMN `when` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP AFTER `since`;
ALTER TABLE `glucose` ADD COLUMN `since` timestamp AFTER `id`;
ALTER TABLE `activity_recommended` ADD COLUMN `since` timestamp AFTER `id`;

insert into `live_data1`
(`glucose`, `glucose_unit`, `glucose_indicator`, `state`)
select `glucose`, `glucose_unit`, `glucose_indicator`, `state`
 from `live_data`;

update `live_data` set `sys_time` = '2020-06-15T15:50:19.726Z';

CREATE TABLE `live_data1` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `glucose` int(3) DEFAULT NULL,
  `glucose_unit` varchar(10) DEFAULT NULL,
  `glucose_indicator` tinyint(4) DEFAULT '1',
  `state` tinyint(4) DEFAULT '1',
  PRIMARY KEY (`id`),
  KEY `fk_ld1_1` (`state`),
  KEY `fk_ld1_2` (`glucose_indicator`),
  CONSTRAINT `fk_ld1_1` FOREIGN KEY (`state`) REFERENCES `live_state` (`id`),
  CONSTRAINT `fk_ld1_2` FOREIGN KEY (`glucose_indicator`) REFERENCES `indicator` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=0 DEFAULT CHARSET=utf8;

CREATE TABLE `user_2_livedata` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `user_id` int(11) unsigned NOT NULL,
  `livedata_id` int(11) unsigned NOT NULL,
  PRIMARY KEY (`id`),
  KEY `fk_ul_1` (`user_id`),
  KEY `fk_ul_2` (`livedata_id`),
  CONSTRAINT `fk_ul_1` FOREIGN KEY (`user_id`) REFERENCES `user` (`id`),
  CONSTRAINT `fk_ul_2` FOREIGN KEY (`livedata_id`) REFERENCES `live_data` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8;