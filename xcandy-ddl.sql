CREATE TABLE `user` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `first_name` varchar(40) NOT NULL,
  `last_name` varchar(40) NOT NULL,
  `phone` varchar(20),
  `email` varchar(80) NOT NULL,
  `password` varchar(100) NOT NULL,
  `birth_date` date,
  `join_date` date,
  PRIMARY KEY (`id`, `email`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

CREATE TABLE `privacy` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `user_id` int(11) unsigned NOT NULL,
  `terms` boolean NOT NULL,
  `advertising` boolean NOT NULL,
  `partners` boolean NOT NULL,
  `research` boolean NOT NULL,
  PRIMARY KEY (`id`, `user_id`),
  CONSTRAINT fk_p_1 FOREIGN KEY (`user_id`) REFERENCES `user`(`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

CREATE TABLE `live_state` (
  `id` tinyint NOT NULL,
  `name` varchar(30) NOT NULL,
  `description` varchar(60) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

CREATE TABLE `live_data` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `user_id` int(11) unsigned NOT NULL,
  `glucose` int(3) DEFAULT NULL,
  `glucose_unit` varchar(10) DEFAULT NULL,
  `glucose_indicator` tinyint DEFAULT 1,
  `state` tinyint DEFAULT 1,
  PRIMARY KEY (`id`, `user_id`),
  CONSTRAINT fk_ld_1 FOREIGN KEY (`user_id`) REFERENCES `user`(`id`),
  CONSTRAINT fk_ld_2 FOREIGN KEY (`state`) REFERENCES `live_state`(`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

CREATE TABLE `forecast_state` (
  `id` tinyint NOT NULL,
  `name` varchar(30) NOT NULL,
  `description` varchar(60) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

CREATE TABLE `forecast_learned` (
  `id` tinyint NOT NULL,
  `name` varchar(30) NOT NULL,
  `description` varchar(60) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

CREATE TABLE `forecast` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `interval` int(3) DEFAULT 0,
  `interval_unit` varchar(10) DEFAULT NULL,
  `value` int(3) DEFAULT 0,
  `unit` varchar(10) DEFAULT NULL,
  `percent` tinyint DEFAULT 1,
  `state` tinyint DEFAULT 1,
  `state_percent` tinyint DEFAULT 0,
  `learned` tinyint DEFAULT 1,
  `learned_percent` tinyint DEFAULT 0,
  `level` tinyint DEFAULT 1,
  PRIMARY KEY (`id`),
  CONSTRAINT fk_f_1 FOREIGN KEY (`state`) REFERENCES `forecast_state`(`id`),
  CONSTRAINT fk_f_2 FOREIGN KEY (`learned`) REFERENCES `forecast_learned`(`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

CREATE TABLE `user_2_forecast` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `user_id` int(11) unsigned NOT NULL,
  `forecast_id` int(11) unsigned NOT NULL,
  PRIMARY KEY (`id`),
  CONSTRAINT fk_uf_1 FOREIGN KEY (`user_id`) REFERENCES `user`(`id`),
  CONSTRAINT fk_uf_2 FOREIGN KEY (`forecast_id`) REFERENCES `forecast`(`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

CREATE TABLE `activity_state` (
  `id` tinyint NOT NULL,
  `name` varchar(30) NOT NULL,
  `description` varchar(60) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

CREATE TABLE `activity_type` (
  `id` tinyint NOT NULL,
  `name` varchar(30) NOT NULL,
  `description` varchar(60) DEFAULT NULL,
  `color` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

CREATE TABLE `activity` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `device` varchar(30) DEFAULT NULL,
  `serial_num` varchar(40) DEFAULT NULL,
  `datetime` varchar(40) NOT NULL,
  `record_type` varchar(5) DEFAULT NULL,
  `glucose` int(3) DEFAULT 0,
  `glucose_unit` varchar(10) DEFAULT NULL,
  `scang` int(3) DEFAULT 0,
  `scang_unit` varchar(10) DEFAULT NULL,
  `rai` int(3) DEFAULT 0,
  `rai_unit` varchar(10) DEFAULT NULL,
  `food` varchar(20) DEFAULT NULL,
  `carbs` int(3) DEFAULT 0,
  `carbs_unit` varchar(10) DEFAULT NULL,
  `lai` int(3) DEFAULT 0,
  `lai_unit` varchar(10) DEFAULT NULL,
  `stripg` int(3) DEFAULT 0,
  `stripg_unit` varchar(10) DEFAULT NULL,
  `ketone` int(3) DEFAULT 0,
  `ketone_unit` varchar(10) DEFAULT NULL,
  `mi` int(3) DEFAULT 0,
  `mi_unit` varchar(10) DEFAULT NULL,
  `ci` int(3) DEFAULT 0,
  `ci_unit` varchar(10) DEFAULT NULL,
  `uci` int(3) DEFAULT 0,
  `uci_unit` varchar(10) DEFAULT NULL,
  `notes` varchar(200) DEFAULT NULL,
  `state` tinyint DEFAULT 1,
  `when` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `who` varchar(30) DEFAULT NULL,
  PRIMARY KEY (`id`),
  CONSTRAINT fk_a_1 FOREIGN KEY (`state`) REFERENCES `activity_state`(`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

CREATE TABLE `activity_log` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `date` date NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

CREATE TABLE `activity_log_detail` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `time` time NOT NULL,
  `value` int(3) NOT NULL,
  `radius` tinyint DEFAULT NULL,
  `type` tinyint NOT NULL,
  PRIMARY KEY (`id`),
  CONSTRAINT fk_al_1 FOREIGN KEY (`type`) REFERENCES `activity_type`(`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

CREATE TABLE `activity_2_activity_log_detail` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `activity_log_id` int(11) unsigned NOT NULL,
  `activity_log_detail_id` int(11) unsigned NOT NULL,
  PRIMARY KEY (`id`),
  CONSTRAINT fk_aad_1 FOREIGN KEY (`activity_log_id`) REFERENCES `activity_log`(`id`),
  CONSTRAINT fk_aad_2 FOREIGN KEY (`activity_log_detail_id`) REFERENCES `activity_log_detail`(`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

CREATE TABLE `batch_state` (
  `id` tinyint NOT NULL,
  `name` varchar(30) NOT NULL,
  `description` varchar(60) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

CREATE TABLE `batch_history` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `user_id` int(11) unsigned NOT NULL,
  `filename` varchar(100) DEFAULT NULL,
  `state` tinyint DEFAULT 1,
  `when` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `who` varchar(30) DEFAULT NULL,
  PRIMARY KEY (`id`),
  CONSTRAINT fk_bh_1 FOREIGN KEY (`user_id`) REFERENCES `user`(`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;



