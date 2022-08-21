-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- ホスト: 127.0.0.1
-- 生成日時: 2022-08-08 10:26:49
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
-- データベース: `order`
--

-- --------------------------------------------------------

--
-- テーブルの構造 `products`
--

CREATE TABLE `products` (
  `product_id` int(11) NOT NULL,
  `type_` int(10) NOT NULL,
  `name_` varchar(20) CHARACTER SET utf8 NOT NULL,
  `price` int(10) NOT NULL,
  `order_date` date DEFAULT NULL,
  `order_status` int(10) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- テーブルのデータのダンプ `products`
--

INSERT INTO `products` (`product_id`, `type_`, `name_`, `price`, `order_date`, `order_status`) VALUES
(1, 0, '原神', 3000, '2022-07-01', 0),
(2, 0, 'モンスト', 2000, '2022-07-02', 0),
(3, 0, 'パズドラ', 2500, '2022-07-03', 0),
(4, 0, 'モンハン', 5000, '2022-07-04', 0),
(5, 0, 'マリオート', 6000, '2022-07-05', 0),
(6, 0, 'スマブラ', 7000, '2022-07-06', 0);

-- --------------------------------------------------------

--
-- テーブルの構造 `user`
--

CREATE TABLE `user` (
  `user_id` varchar(20) NOT NULL,
  `user_name` varchar(20) CHARACTER SET utf8 NOT NULL,
  `user_password` varchar(20) NOT NULL,
  `e_mail` varchar(20) NOT NULL,
  `permission` int(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- テーブルのデータのダンプ `user`
--

INSERT INTO `user` (`user_id`, `user_name`, `user_password`, `e_mail`, `permission`) VALUES
('k-ygawa', '柳川小次郎', 'kojikoji', 'k-ygawa@yic.ac.jp', 2),
('sugi', '杉林伸繁', 'sugisugi', 'sugi@yic.ac.jp', 2),
('﻿\'hoge\'', '山口太郎', 'P@ssw0rd', 'hoge@yic.ac.jp', 1);

--
-- ダンプしたテーブルのインデックス
--

--
-- テーブルのインデックス `products`
--
ALTER TABLE `products`
  ADD PRIMARY KEY (`product_id`);

--
-- テーブルのインデックス `user`
--
ALTER TABLE `user`
  ADD PRIMARY KEY (`user_id`);

--
-- ダンプしたテーブルの AUTO_INCREMENT
--

--
-- テーブルの AUTO_INCREMENT `products`
--
ALTER TABLE `products`
  MODIFY `product_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=53;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
