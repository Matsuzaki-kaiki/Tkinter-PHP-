-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- ホスト: 127.0.0.1
-- 生成日時: 2022-08-08 10:35:15
-- サーバのバージョン： 10.4.24-MariaDB
-- PHP のバージョン: 8.1.6

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- データベース: `apr01`
--

-- --------------------------------------------------------

--
-- テーブルの構造 `plan_table`
--

CREATE TABLE `plan_table` (
  `plan_ID` int(11) NOT NULL,
  `user_ID` smallint(6) DEFAULT NULL,
  `plan_type_ID` tinyint(4) DEFAULT NULL,
  `memo` varchar(250) CHARACTER SET utf8 NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- テーブルの構造 `plan_type_table`
--

CREATE TABLE `plan_type_table` (
  `Plan_type_ID` tinyint(4) NOT NULL,
  `Plan_type` varchar(10) CHARACTER SET utf8 NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- テーブルのデータのダンプ `plan_type_table`
--

INSERT INTO `plan_type_table` (`Plan_type_ID`, `Plan_type`) VALUES
(1, '学校'),
(2, '試験'),
(3, '課題'),
(4, '行事'),
(5, '就活'),
(6, 'アルバイト'),
(7, '旅行');

-- --------------------------------------------------------

--
-- テーブルの構造 `user_table`
--

CREATE TABLE `user_table` (
  `user_ID` smallint(6) NOT NULL,
  `user_name` varchar(20) CHARACTER SET utf8 NOT NULL,
  `user_password` char(8) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- テーブルのデータのダンプ `user_table`
--

INSERT INTO `user_table` (`user_ID`, `user_name`, `user_password`) VALUES
(1, '野比のび助', 'nobi');

--
-- ダンプしたテーブルのインデックス
--

--
-- テーブルのインデックス `plan_table`
--
ALTER TABLE `plan_table`
  ADD PRIMARY KEY (`plan_ID`),
  ADD KEY `user_ID` (`user_ID`),
  ADD KEY `plan_type_ID` (`plan_type_ID`);

--
-- テーブルのインデックス `plan_type_table`
--
ALTER TABLE `plan_type_table`
  ADD PRIMARY KEY (`Plan_type_ID`);

--
-- テーブルのインデックス `user_table`
--
ALTER TABLE `user_table`
  ADD PRIMARY KEY (`user_ID`);

--
-- ダンプしたテーブルの AUTO_INCREMENT
--

--
-- テーブルの AUTO_INCREMENT `plan_table`
--
ALTER TABLE `plan_table`
  MODIFY `plan_ID` int(11) NOT NULL AUTO_INCREMENT;

--
-- テーブルの AUTO_INCREMENT `user_table`
--
ALTER TABLE `user_table`
  MODIFY `user_ID` smallint(6) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- ダンプしたテーブルの制約
--

--
-- テーブルの制約 `plan_table`
--
ALTER TABLE `plan_table`
  ADD CONSTRAINT `plan_table_ibfk_1` FOREIGN KEY (`user_ID`) REFERENCES `user_table` (`user_ID`),
  ADD CONSTRAINT `plan_table_ibfk_2` FOREIGN KEY (`plan_type_ID`) REFERENCES `plan_type_table` (`Plan_type_ID`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
