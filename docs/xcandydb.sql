# ************************************************************
# Sequel Pro SQL dump
# Version 4541
#
# http://www.sequelpro.com/
# https://github.com/sequelpro/sequelpro
#
# Host: 127.0.0.1 (MySQL 5.7.28)
# Database: xcandydb
# Generation Time: 2020-04-05 23:25:21 +0000
# ************************************************************


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;


# Dump of table activity
# ------------------------------------------------------------

DROP TABLE IF EXISTS `activity`;

CREATE TABLE `activity` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `device` varchar(30) DEFAULT NULL,
  `serial_num` varchar(40) DEFAULT NULL,
  `datetime` varchar(40) NOT NULL,
  `record_type` varchar(5) DEFAULT NULL,
  `glucose` int(3) DEFAULT '0',
  `glucose_unit` varchar(10) DEFAULT NULL,
  `scang` int(3) DEFAULT '0',
  `scang_unit` varchar(10) DEFAULT NULL,
  `rai` int(3) DEFAULT '0',
  `rai_unit` varchar(10) DEFAULT NULL,
  `food` varchar(20) DEFAULT NULL,
  `carbs` int(3) DEFAULT '0',
  `carbs_unit` varchar(10) DEFAULT NULL,
  `lai` int(3) DEFAULT '0',
  `lai_unit` varchar(10) DEFAULT NULL,
  `stripg` int(3) DEFAULT '0',
  `stripg_unit` varchar(10) DEFAULT NULL,
  `ketone` int(3) DEFAULT '0',
  `ketone_unit` varchar(10) DEFAULT NULL,
  `mi` int(3) DEFAULT '0',
  `mi_unit` varchar(10) DEFAULT NULL,
  `ci` int(3) DEFAULT '0',
  `ci_unit` varchar(10) DEFAULT NULL,
  `uci` int(3) DEFAULT '0',
  `uci_unit` varchar(10) DEFAULT NULL,
  `notes` varchar(200) DEFAULT NULL,
  `state` tinyint(4) DEFAULT '1',
  `when` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `who` varchar(30) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `fk_a_1` (`state`),
  CONSTRAINT `fk_a_1` FOREIGN KEY (`state`) REFERENCES `activity_state` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;



# Dump of table activity_2_activity_log_detail
# ------------------------------------------------------------

DROP TABLE IF EXISTS `activity_2_activity_log_detail`;

CREATE TABLE `activity_2_activity_log_detail` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `activity_log_id` int(11) unsigned NOT NULL,
  `activity_log_detail_id` int(11) unsigned NOT NULL,
  PRIMARY KEY (`id`),
  KEY `fk_aad_1` (`activity_log_id`),
  KEY `fk_aad_2` (`activity_log_detail_id`),
  CONSTRAINT `fk_aad_1` FOREIGN KEY (`activity_log_id`) REFERENCES `activity_log` (`id`),
  CONSTRAINT `fk_aad_2` FOREIGN KEY (`activity_log_detail_id`) REFERENCES `activity_log_detail` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;



# Dump of table activity_log
# ------------------------------------------------------------

DROP TABLE IF EXISTS `activity_log`;

CREATE TABLE `activity_log` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `date` date NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;



# Dump of table activity_log_detail
# ------------------------------------------------------------

DROP TABLE IF EXISTS `activity_log_detail`;

CREATE TABLE `activity_log_detail` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `time` time NOT NULL,
  `value` int(3) NOT NULL,
  `radius` tinyint(4) DEFAULT NULL,
  `type` tinyint(4) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `fk_al_1` (`type`),
  CONSTRAINT `fk_al_1` FOREIGN KEY (`type`) REFERENCES `activity_type` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;



# Dump of table activity_state
# ------------------------------------------------------------

DROP TABLE IF EXISTS `activity_state`;

CREATE TABLE `activity_state` (
  `id` tinyint(4) NOT NULL,
  `name` varchar(30) NOT NULL,
  `description` varchar(60) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;



# Dump of table activity_type
# ------------------------------------------------------------

DROP TABLE IF EXISTS `activity_type`;

CREATE TABLE `activity_type` (
  `id` tinyint(4) NOT NULL,
  `name` varchar(30) NOT NULL,
  `description` varchar(60) DEFAULT NULL,
  `color` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;



# Dump of table batch_history
# ------------------------------------------------------------

DROP TABLE IF EXISTS `batch_history`;

CREATE TABLE `batch_history` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `user_id` int(11) unsigned NOT NULL,
  `filename` varchar(100) DEFAULT NULL,
  `state` tinyint(4) DEFAULT '1',
  `when` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `who` varchar(30) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `fk_bh_1` (`user_id`),
  CONSTRAINT `fk_bh_1` FOREIGN KEY (`user_id`) REFERENCES `user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;



# Dump of table batch_state
# ------------------------------------------------------------

DROP TABLE IF EXISTS `batch_state`;

CREATE TABLE `batch_state` (
  `id` tinyint(4) NOT NULL,
  `name` varchar(30) NOT NULL,
  `description` varchar(60) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;



# Dump of table forecast
# ------------------------------------------------------------

DROP TABLE IF EXISTS `forecast`;

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



# Dump of table forecast_learned
# ------------------------------------------------------------

DROP TABLE IF EXISTS `forecast_learned`;

CREATE TABLE `forecast_learned` (
  `id` tinyint(4) NOT NULL,
  `name` varchar(30) NOT NULL,
  `description` varchar(60) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;



# Dump of table forecast_state
# ------------------------------------------------------------

DROP TABLE IF EXISTS `forecast_state`;

CREATE TABLE `forecast_state` (
  `id` tinyint(4) NOT NULL,
  `name` varchar(30) NOT NULL,
  `description` varchar(60) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;



# Dump of table live_data
# ------------------------------------------------------------

DROP TABLE IF EXISTS `live_data`;

CREATE TABLE `live_data` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `user_id` int(11) unsigned NOT NULL,
  `glucose` int(3) DEFAULT NULL,
  `glucose_unit` varchar(10) DEFAULT NULL,
  `glucose_indicator` tinyint(4) DEFAULT '1',
  `state` tinyint(4) DEFAULT '1',
  PRIMARY KEY (`id`,`user_id`),
  KEY `fk_ld_1` (`user_id`),
  KEY `fk_ld_2` (`state`),
  CONSTRAINT `fk_ld_1` FOREIGN KEY (`user_id`) REFERENCES `user` (`id`),
  CONSTRAINT `fk_ld_2` FOREIGN KEY (`state`) REFERENCES `live_state` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;



# Dump of table live_state
# ------------------------------------------------------------

DROP TABLE IF EXISTS `live_state`;

CREATE TABLE `live_state` (
  `id` tinyint(4) NOT NULL,
  `name` varchar(30) NOT NULL,
  `description` varchar(60) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;



# Dump of table privacy
# ------------------------------------------------------------

DROP TABLE IF EXISTS `privacy`;

CREATE TABLE `privacy` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `user_id` int(11) unsigned NOT NULL,
  `terms` tinyint(1) NOT NULL,
  `advertising` tinyint(1) NOT NULL,
  `partners` tinyint(1) NOT NULL,
  `research` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`,`user_id`),
  KEY `fk_p_1` (`user_id`),
  CONSTRAINT `fk_p_1` FOREIGN KEY (`user_id`) REFERENCES `user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;



# Dump of table user
# ------------------------------------------------------------

DROP TABLE IF EXISTS `user`;

CREATE TABLE `user` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `first_name` varchar(40) NOT NULL,
  `last_name` varchar(40) NOT NULL,
  `phone` varchar(20) DEFAULT NULL,
  `email` varchar(80) NOT NULL,
  `password` varchar(100) NOT NULL,
  `birth_date` date DEFAULT NULL,
  `join_date` date DEFAULT NULL,
  PRIMARY KEY (`id`,`email`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;



# Dump of table user_2_forecast
# ------------------------------------------------------------

DROP TABLE IF EXISTS `user_2_forecast`;

CREATE TABLE `user_2_forecast` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `user_id` int(11) unsigned NOT NULL,
  `forecast_id` int(11) unsigned NOT NULL,
  PRIMARY KEY (`id`),
  KEY `fk_uf_1` (`user_id`),
  KEY `fk_uf_2` (`forecast_id`),
  CONSTRAINT `fk_uf_1` FOREIGN KEY (`user_id`) REFERENCES `user` (`id`),
  CONSTRAINT `fk_uf_2` FOREIGN KEY (`forecast_id`) REFERENCES `forecast` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;




/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
