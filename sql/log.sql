SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for `clr_book_item`
-- ----------------------------
DROP TABLE IF EXISTS `clr_book_item`;
CREATE TABLE `clr_book_item` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `title` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL,
  `content` text COLLATE utf8_unicode_ci,
  `url` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;