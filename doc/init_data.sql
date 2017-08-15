
-- grant all privileges on *.* to kdb@localhost identified by 'kdb';

drop database kdb;
create database kdb default charset utf8;

use kdb;

-- DROP TABLE IF EXISTS T_BASIC_BOOK;
-- DROP TABLE IF EXISTS T_BASIC_SHOP;
-- DROP TABLE IF EXISTS T_BASIC_SHOPBOOK;
-- DROP TABLE IF EXISTS T_BUSINESS_TEMPLATE;
-- DROP TABLE IF EXISTS T_BUSINESS_TEMPLATE_DATA;
-- DROP TABLE IF EXISTS T_CONFIG_CATEGORY;
-- DROP TABLE IF EXISTS T_CONFIG_DATATYPE;
-- DROP TABLE IF EXISTS T_DATA;

CREATE TABLE `T_BASIC_BOOK` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `book` varchar(20) DEFAULT NULL,
  `name` varchar(32) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8;

CREATE TABLE `T_BASIC_SHOP` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `shop` varchar(20) DEFAULT NULL,
  `name` varchar(32) DEFAULT NULL,
  `url` varchar(1024) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;

CREATE TABLE `T_BASIC_SHOPBOOK` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `book` varchar(20) DEFAULT NULL,
  `shop` varchar(20) DEFAULT NULL,
  `url` varchar(1024) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8;

CREATE TABLE `T_BUSINESS_TEMPLATE` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(20) DEFAULT NULL,
  `date` datetime DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;

CREATE TABLE `T_BUSINESS_TEMPLATE_DATA` (
  `temp_id` int(11) NOT NULL,
  `shop` varchar(20) NOT NULL,
  `book` varchar(20) NOT NULL,
  PRIMARY KEY (`temp_id`,`shop`,`book`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

CREATE TABLE `T_CONFIG_CATEGORY` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

CREATE TABLE `T_CONFIG_DATATYPE` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

CREATE TABLE `T_DATA` (
  `shop` varchar(20) DEFAULT NULL,
  `book` varchar(20) DEFAULT NULL,
  `datatype` varchar(20) DEFAULT NULL,
  `value` int(11) DEFAULT NULL,
  `date` datetime DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;



insert into T_CONFIG_DATATYPE values ('price', '售价'), ('sale', '销量'), ('discount', '折扣'), ('comment', '评论数'), ('investment', '直通车投入');



insert into T_BASIC_BOOK (book, name) values ('9787115394392', 'Python参考手册(第4版·修订版)'), ('9787115454898', 'Python高性能编程'), ('9787115414779', 'Python核心编程 第3版'), ('9787115339409', 'Python数据分析基础教程：NumPy学习指南(第2版)');

insert into T_BASIC_SHOP (shop, name, url) values ('rmydcbs', '人民邮电出版社官方旗舰店', 'rmydcbs.tmall.com'), ('winshare', '新华文轩网络书店', 'winshare.tmall.com');

insert into T_BASIC_SHOPBOOK (book, shop, url) values
('9787115394392', 'rmydcbs', 'https://detail.tmall.com/item.htm?spm=a1z10.3-b.w4011-9986777119.15.79c15d8JGRW05&id=539853070197&rn=934e2d1ecc4ab188c0bb95e26877b606&abbucket=4'),
('9787115394392', 'winshare', 'https://detail.tmall.com/item.htm?spm=a1z10.3-b-s.w4011-15011179809.182.56695febowhWBN&id=541143731300&rn=03fe8410363b4538f2f02b7d90e22ba4&abbucket=4'),
('9787115454898', 'rmydcbs', 'https://detail.tmall.com/item.htm?spm=a1z10.3-b.w4011-9986777119.23.79c15d8JGRW05&id=553391639537&rn=934e2d1ecc4ab188c0bb95e26877b606&abbucket=4'),
('9787115454898', 'winshare', 'https://detail.tmall.com/item.htm?spm=a1z10.3-b-s.w4011-15011179809.158.56695febowhWBN&id=554411773451&rn=03fe8410363b4538f2f02b7d90e22ba4&abbucket=4'),
('9787115414779', 'rmydcbs', 'https://detail.tmall.com/item.htm?spm=a1z10.3-b.w4011-9986777119.85.79c15d8JGRW05&id=531816970861&rn=934e2d1ecc4ab188c0bb95e26877b606&abbucket=4'),
('9787115339409', 'winshare', 'https://detail.tmall.com/item.htm?spm=a1z10.3-b-s.w4011-15011179809.37.56695febhnM8kb&id=37215987064&rn=b0839a25c9ec7531185bbb7755cda98c&abbucket=4');

-- insert into T_BUSINESS_TEMPLATE (name) values ('竞品页模板-python');
-- insert into T_BUSINESS_TEMPLATE_DATA (temp_id, shop, book) values (1, 'rmydcbs', '9787115394392'), (1, 'winshare', '9787115394392');

-- insert into T_DATA values ('rmydcbs', '9787115394392', 'price', 5, '2017/08/01');
-- insert into T_DATA values ('rmydcbs', '9787115454898', 'sale', 10, '2017-08-01');
-- insert into T_DATA values ('winshare', '9787115394392', 'sale', 10, '2017-08-01');
