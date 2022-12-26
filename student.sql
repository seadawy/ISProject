-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Dec 26, 2022 at 02:59 PM
-- Server version: 10.4.27-MariaDB
-- PHP Version: 7.4.33

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `isp`
--

-- --------------------------------------------------------

--
-- Table structure for table `student`
--

CREATE TABLE `student` (
  `id` int(5) NOT NULL,
  `name` varchar(500) NOT NULL,
  `IId` varchar(14) DEFAULT NULL,
  `adress` varchar(500) NOT NULL,
  `type` varchar(10) NOT NULL,
  `img` varchar(500) NOT NULL DEFAULT 'C:\\Users\\asilah\\Desktop\\ISTkinter\\asset\\user.png',
  `rank` int(100) NOT NULL,
  `password` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;

--
-- Dumping data for table `student`
--

INSERT INTO `student` (`id`, `name`, `IId`, `adress`, `type`, `img`, `rank`, `password`) VALUES
(21, 'Atef Mohamed', '88888888888888', 'ALEX', 'Coder', '/asset/Atef.png', 4, '0'),
(23, 'seadawy', '876454334', 'LUXOR', 'Male', '/asset/seadawey.png', 2, '0'),
(24, 'moshka', '525555555', 'KFS', 'Male', '\\asset\\m.png', 2, '0'),
(25, 'seif', '74859632125', 'LUXOR', 'Female', '/asset/seif.png', 5, '0'),
(26, 'suef', '0999877', 'CAIRO', 'Female', '\\asset\\user.png', 0, '0'),
(28, 'lool', '1234567890', 'KFS', 'Male', '\\asset\\user.png', 0, '0'),
(29, 'pola', '789456321', 'LUXOR', 'Male', '\\asset\\user.png', 0, '0'),
(30, 'fathi', '098765456789', 'LUXOR', 'Male', '/asset/Tharwat.png', 0, '0'),
(31, 'ramaj', '741258963', 'ALEX', 'Female', '/asset/user.png', 2, '0'),
(32, 'er', '234556745', 'ALEX', 'Male', '/asset/user.png', 0, '0'),
(33, 'uuu', '234567890', 'LUXOR', 'Coder', 'asset/.png566864c2.png', 0, '0'),
(34, 'new', '8520796413', 'ALEX', 'Male', 'asset/117a81a8.png', 0, '0');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `student`
--
ALTER TABLE `student`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `student`
--
ALTER TABLE `student`
  MODIFY `id` int(5) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=35;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
