-- phpMyAdmin SQL Dump
-- version 4.9.0.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Sep 21, 2019 at 01:12 AM
-- Server version: 10.4.6-MariaDB
-- PHP Version: 7.3.8

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `event management`
--

-- --------------------------------------------------------

--
-- Table structure for table `events_list`
--

CREATE TABLE `events_list` (
  `Id` int(50) NOT NULL,
  `Title` varchar(100) NOT NULL,
  `Description` text NOT NULL,
  `Catagory` varchar(50) NOT NULL,
  `Tags` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `events_list`
--

INSERT INTO `events_list` (`Id`, `Title`, `Description`, `Catagory`, `Tags`) VALUES
(1, 'Dance Party', 'Dance Party at nude beach.', 'sex', 'Dance,Party,Sex'),
(10, 'Beach Side Massage', 'Sandwich Massage', 'Funny', 'Massage,Sex'),
(11, 'Rave Party', 'Rave Party with unlimited Drugs', 'Funny', 'drug,dance,trance');

-- --------------------------------------------------------

--
-- Table structure for table `event_registration`
--

CREATE TABLE `event_registration` (
  `id` int(11) NOT NULL,
  `fname` varchar(50) NOT NULL,
  `lname` varchar(50) NOT NULL,
  `city` varchar(50) NOT NULL,
  `num` varchar(20) NOT NULL,
  `email` varchar(50) NOT NULL,
  `pic` varbinary(8000) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `event_registration`
--

INSERT INTO `event_registration` (`id`, `fname`, `lname`, `city`, `num`, `email`, `pic`) VALUES
(2, 'hgiufi', 'uuyfyuy', 'gguyg', '2147483647', 'hkjhl@ok.oj', 0x7064322e706e67),
(4, 'harshil', 'umreth', 'shs', '2147483647', 'shhssh@heh.ahsg', 0x7064312e706e67),
(5, 'harshil', 'dsdsjds', 'dddd', '94545469', 'hshsh@hssj.cus', 0x726d72312e6a7067),
(6, 'dgdfg', 'dgdfg', 'cvbcvb', '0', 'hfghfg@fdgdfg.dsgds', 0x7064322e706e67),
(7, 'ghvgvh', 'ffghvh', 'gffjgy', '2147483647', 'fdghgg@hvh.ggghg', 0x70642e706e67),
(15, 'test0', 'test', 'test2', '2147483647', 'milanthakor2013@gmail.com', ''),
(20, 'Harshil', 'Umrethwala', 'surat', '8511109996', 'humrethwala@yahoo.com', 0x44312e6a7067);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `events_list`
--
ALTER TABLE `events_list`
  ADD UNIQUE KEY `Index` (`Id`),
  ADD KEY `count` (`Id`);

--
-- Indexes for table `event_registration`
--
ALTER TABLE `event_registration`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `events_list`
--
ALTER TABLE `events_list`
  MODIFY `Id` int(50) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=17;

--
-- AUTO_INCREMENT for table `event_registration`
--
ALTER TABLE `event_registration`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=21;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
