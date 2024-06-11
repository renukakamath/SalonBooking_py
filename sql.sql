/*
SQLyog Community v13.1.6 (64 bit)
MySQL - 5.7.9 : Database - salonbooking
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
CREATE DATABASE /*!32312 IF NOT EXISTS*/`salonbooking` /*!40100 DEFAULT CHARACTER SET latin1 */;

USE `salonbooking`;

/*Table structure for table `booking_child` */

DROP TABLE IF EXISTS `booking_child`;

CREATE TABLE `booking_child` (
  `bc_id` int(11) NOT NULL AUTO_INCREMENT,
  `bm_id` int(11) DEFAULT NULL,
  `service_id` int(11) DEFAULT NULL,
  `price` varchar(20) DEFAULT NULL,
  `b_date` date DEFAULT NULL,
  `time_slot` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`bc_id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

/*Data for the table `booking_child` */

/*Table structure for table `booking_master` */

DROP TABLE IF EXISTS `booking_master`;

CREATE TABLE `booking_master` (
  `bm_id` int(11) NOT NULL AUTO_INCREMENT,
  `salon_id` int(11) DEFAULT NULL,
  `customer_id` int(11) DEFAULT NULL,
  `total_price` varchar(20) DEFAULT NULL,
  `bm_status` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`bm_id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

/*Data for the table `booking_master` */

/*Table structure for table `card` */

DROP TABLE IF EXISTS `card`;

CREATE TABLE `card` (
  `card_id` int(11) NOT NULL AUTO_INCREMENT,
  `customer_id` int(11) DEFAULT NULL,
  `card_no` varchar(20) DEFAULT NULL,
  `card_name` varchar(20) DEFAULT NULL,
  `expiry_date` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`card_id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

/*Data for the table `card` */

/*Table structure for table `category` */

DROP TABLE IF EXISTS `category`;

CREATE TABLE `category` (
  `category_id` int(11) NOT NULL AUTO_INCREMENT,
  `category_name` varchar(20) DEFAULT NULL,
  `category_description` varchar(100) DEFAULT NULL,
  `c_status` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`category_id`)
) ENGINE=MyISAM AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

/*Data for the table `category` */

insert  into `category`(`category_id`,`category_name`,`category_description`,`c_status`) values 
(1,'Hair Care','It includes a wide variety of hair care services','1');

/*Table structure for table `complaints` */

DROP TABLE IF EXISTS `complaints`;

CREATE TABLE `complaints` (
  `complaint_id` int(11) NOT NULL AUTO_INCREMENT,
  `customer_id` int(11) DEFAULT NULL,
  `salon_id` int(11) DEFAULT NULL,
  `complaint` varchar(20) DEFAULT NULL,
  `reply` varchar(20) DEFAULT NULL,
  `date` date DEFAULT NULL,
  PRIMARY KEY (`complaint_id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

/*Data for the table `complaints` */

/*Table structure for table `customer` */

DROP TABLE IF EXISTS `customer`;

CREATE TABLE `customer` (
  `customer_id` int(11) NOT NULL AUTO_INCREMENT,
  `login_id` int(11) DEFAULT NULL,
  `c_fname` varchar(20) DEFAULT NULL,
  `c_lname` varchar(20) DEFAULT NULL,
  `c_dob` date DEFAULT NULL,
  `c_housename` varchar(20) DEFAULT NULL,
  `c_city` varchar(20) DEFAULT NULL,
  `c_district` varchar(20) DEFAULT NULL,
  `c_phno` varchar(11) DEFAULT NULL,
  `c_pin` varchar(8) DEFAULT NULL,
  `c_status` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`customer_id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

/*Data for the table `customer` */

/*Table structure for table `design` */

DROP TABLE IF EXISTS `design`;

CREATE TABLE `design` (
  `design_id` int(11) NOT NULL AUTO_INCREMENT,
  `title` varchar(20) DEFAULT NULL,
  `image` varchar(1000) DEFAULT NULL,
  PRIMARY KEY (`design_id`)
) ENGINE=MyISAM AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;

/*Data for the table `design` */

insert  into `design`(`design_id`,`title`,`image`) values 
(1,'image1','static/image/c18ea9c9-89a2-4439-a890-aebc0991d8f7wallpaper 1.jpg'),
(2,'image1','static/image/167df324-7a2d-4d53-942b-df34bb8b20831678613-Disney-movies-The-Little-Mermaid-4K.jpg');

/*Table structure for table `feedback` */

DROP TABLE IF EXISTS `feedback`;

CREATE TABLE `feedback` (
  `feedback_id` int(11) NOT NULL AUTO_INCREMENT,
  `customer_id` int(11) DEFAULT NULL,
  `salon_id` int(11) DEFAULT NULL,
  `feedback` varchar(20) DEFAULT NULL,
  `date` date DEFAULT NULL,
  PRIMARY KEY (`feedback_id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

/*Data for the table `feedback` */

/*Table structure for table `login` */

DROP TABLE IF EXISTS `login`;

CREATE TABLE `login` (
  `login_id` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(20) DEFAULT NULL,
  `password` varchar(20) DEFAULT NULL,
  `usertype` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`login_id`)
) ENGINE=MyISAM AUTO_INCREMENT=29 DEFAULT CHARSET=latin1;

/*Data for the table `login` */

insert  into `login`(`login_id`,`username`,`password`,`usertype`) values 
(1,'Admin','Admin123##','admin'),
(9,'Nancy03Jac','Nancy@03Jacob','staff'),
(5,'Sans123polo','SansPolo45@','salon'),
(10,'Nancy03Jac','Nancy@03Jacob','staff'),
(8,'GreenSpa20#','Greenspa@20','salon'),
(11,'Nancy03Jac','Nancy03@Jacob','staff'),
(12,'Nancy03Jac','Nancy03@Jacob','staff'),
(13,'Nancy03Jac','Nancy03@Jacob','staff'),
(14,'Nancy03Jac','Nancy@03Jacob','staff'),
(15,'Nancy03Jac','Nancy@03Jacob','staff'),
(16,'Nancy03Jac','Nancy03@Jacob','staff'),
(17,'Nancy03Jac','Nancy03@Jacob','staff'),
(18,'Nancy03Jac','Nancy03@J','staff'),
(19,'Nancy03Jac','Nancy03@J','staff'),
(20,'Nancy03Jac','Nancy03@J','staff'),
(21,'Nancy03Jac','Nancy03@J','staff'),
(22,'Nancy03Jac','Nancy@03Jac','staff'),
(23,'Nancy03Jac','Nancy@03Jac','staff'),
(24,'Nancy03Jac','Nancy@03Jac','staff'),
(25,'Nancy03Jac','Nancy@03Jac','staff'),
(26,'Nancy03Jac','Nancy03@Jac','staff'),
(27,'Nancy03Jac','Nancy03@Jac','staff'),
(28,'Dev13Ram','Dev#13Ram','staff');

/*Table structure for table `payment` */

DROP TABLE IF EXISTS `payment`;

CREATE TABLE `payment` (
  `payment_id` int(11) NOT NULL AUTO_INCREMENT,
  `bm_id` int(11) DEFAULT NULL,
  `card_id` int(11) DEFAULT NULL,
  `payment_date` date DEFAULT NULL,
  PRIMARY KEY (`payment_id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

/*Data for the table `payment` */

/*Table structure for table `rating` */

DROP TABLE IF EXISTS `rating`;

CREATE TABLE `rating` (
  `rating_id` int(11) NOT NULL AUTO_INCREMENT,
  `customer_id` int(11) DEFAULT NULL,
  `salon_id` int(11) DEFAULT NULL,
  `rating` varchar(20) DEFAULT NULL,
  `date` date DEFAULT NULL,
  PRIMARY KEY (`rating_id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

/*Data for the table `rating` */

/*Table structure for table `salon` */

DROP TABLE IF EXISTS `salon`;

CREATE TABLE `salon` (
  `salon_id` int(11) NOT NULL AUTO_INCREMENT,
  `login_id` int(11) DEFAULT NULL,
  `salon_name` varchar(100) DEFAULT NULL,
  `salon_place` varchar(100) DEFAULT NULL,
  `salon_phone` varchar(11) DEFAULT NULL,
  `salon_email` varchar(20) DEFAULT NULL,
  `salon_address` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`salon_id`)
) ENGINE=MyISAM AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;

/*Data for the table `salon` */

insert  into `salon`(`salon_id`,`login_id`,`salon_name`,`salon_place`,`salon_phone`,`salon_email`,`salon_address`) values 
(1,5,'Sans Polo','Palarivattam','09812873456','sanspolo13@gmail.com','Palarivattom, Cohin - 682025'),
(2,8,'Green Spa Beauty Salon','Palarivattam','09946327456','GreenSpa46@gmail.com','Palarivattam - Ernakulam, Hair Straightening Kochi, Kerala, India');

/*Table structure for table `service` */

DROP TABLE IF EXISTS `service`;

CREATE TABLE `service` (
  `service_id` int(11) NOT NULL AUTO_INCREMENT,
  `category_id` int(11) DEFAULT NULL,
  `service_name` varchar(30) DEFAULT NULL,
  `staff_id` int(11) DEFAULT NULL,
  `s_status` varchar(20) DEFAULT NULL,
  `price` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`service_id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

/*Data for the table `service` */

/*Table structure for table `staff` */

DROP TABLE IF EXISTS `staff`;

CREATE TABLE `staff` (
  `staff_id` int(11) NOT NULL AUTO_INCREMENT,
  `login_id` int(11) DEFAULT NULL,
  `salon_id` int(11) DEFAULT NULL,
  `s_fname` varchar(20) DEFAULT NULL,
  `s_lname` varchar(20) DEFAULT NULL,
  `s_joindate` date DEFAULT NULL,
  `s_dob` date DEFAULT NULL,
  `s_gender` varchar(20) DEFAULT NULL,
  `s_housename` varchar(20) DEFAULT NULL,
  `s_city` varchar(20) DEFAULT NULL,
  `s_district` varchar(20) DEFAULT NULL,
  `s_pin` varchar(8) DEFAULT NULL,
  `s_phno` varchar(11) DEFAULT NULL,
  `s_status` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`staff_id`)
) ENGINE=MyISAM AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;

/*Data for the table `staff` */

insert  into `staff`(`staff_id`,`login_id`,`salon_id`,`s_fname`,`s_lname`,`s_joindate`,`s_dob`,`s_gender`,`s_housename`,`s_city`,`s_district`,`s_pin`,`s_phno`,`s_status`) values 
(1,27,2,'Nancy','Jacob','2012-06-22','1997-02-03','Male','Rose ville','Paravur','Ernakulam','689456','9081273645','active'),
(2,28,1,'Ram','Dev','2022-09-07','1995-06-13','Female','Puthupilly','Aluva','Ernakulam','654321','9807564312','active');

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
