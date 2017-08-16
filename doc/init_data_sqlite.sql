-- DROP TABLE IF EXISTS T_BASIC_BOOK;
-- DROP TABLE IF EXISTS T_BASIC_SHOP;
-- DROP TABLE IF EXISTS T_BASIC_SHOPBOOK;
-- DROP TABLE IF EXISTS T_BUSINESS_TEMPLATE;
-- DROP TABLE IF EXISTS T_BUSINESS_TEMPLATE_DATA;
-- DROP TABLE IF EXISTS T_CONFIG_CATEGORY;
-- DROP TABLE IF EXISTS T_CONFIG_DATATYPE;
-- DROP TABLE IF EXISTS T_DATA;

CREATE TABLE `T_BASIC_BOOK` (
  `id` int(11) NOT NULL,
  `book` varchar(20) DEFAULT NULL,
  `name` varchar(32) DEFAULT NULL,
  PRIMARY KEY (`id`)
);

CREATE TABLE `T_BASIC_SHOP` (
  `id` int(11) NOT NULL,
  `shop` varchar(20) DEFAULT NULL,
  `name` varchar(32) DEFAULT NULL,
  `url` varchar(1024) DEFAULT NULL,
  PRIMARY KEY (`id`)
);

CREATE TABLE `T_BASIC_SHOPBOOK` (
  `id` int(11) NOT NULL,
  `book` varchar(20) DEFAULT NULL,
  `shop` varchar(20) DEFAULT NULL,
  `url` varchar(1024) DEFAULT NULL,
  PRIMARY KEY (`id`)
);

CREATE TABLE `T_BUSINESS_TEMPLATE` (
  `id` int(11) NOT NULL,
  `name` varchar(20) DEFAULT NULL,
  `date` datetime DEFAULT NULL,
  PRIMARY KEY (`id`)
);

CREATE TABLE `T_BUSINESS_TEMPLATE_DATA` (
  `temp_id` int(11) NOT NULL,
  `shop` varchar(20) NOT NULL,
  `book` varchar(20) NOT NULL,
  PRIMARY KEY (`temp_id`,`shop`,`book`)
);

CREATE TABLE `T_CONFIG_CATEGORY` (
  `id` int(11) NOT NULL,
  `name` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`id`)
);

CREATE TABLE `T_CONFIG_DATATYPE` (
  `id` int(11) NOT NULL,
  `name` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`id`)
);

CREATE TABLE `T_DATA` (
  `shop` varchar(20) DEFAULT NULL,
  `book` varchar(20) DEFAULT NULL,
  `datatype` varchar(20) DEFAULT NULL,
  `value` int(11) DEFAULT NULL,
  `date` datetime DEFAULT NULL
);

insert into T_CONFIG_DATATYPE values ('price', '售价'), ('sale', '销量'), ('discount', '折扣'), ('comment', '评论数'), ('investment', '直通车投入');
