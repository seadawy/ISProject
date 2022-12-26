-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Dec 26, 2022 at 03:00 PM
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
-- Table structure for table `admin`
--

CREATE TABLE `admin` (
  `user` varchar(500) NOT NULL,
  `password` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;

--
-- Dumping data for table `admin`
--

INSERT INTO `admin` (`user`, `password`) VALUES
('', '');

-- --------------------------------------------------------

--
-- Table structure for table `history`
--

CREATE TABLE `history` (
  `studentId` int(11) NOT NULL,
  `quizId` varchar(11) NOT NULL,
  `score` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;

--
-- Dumping data for table `history`
--

INSERT INTO `history` (`studentId`, `quizId`, `score`) VALUES
(31, '1a998fb8', 2);

-- --------------------------------------------------------

--
-- Table structure for table `matrial`
--

CREATE TABLE `matrial` (
  `idFile` int(100) NOT NULL,
  `file` varchar(1000) NOT NULL,
  `filename` varchar(1000) NOT NULL,
  `date` date NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;

--
-- Dumping data for table `matrial`
--

INSERT INTO `matrial` (`idFile`, `file`, `filename`, `date`) VALUES
(1, 'C:/Users/asilah/Desktop/FCI/Hours.pdf', 'assign', '2022-12-20');

-- --------------------------------------------------------

--
-- Table structure for table `questions`
--

CREATE TABLE `questions` (
  `quizId` varchar(11) NOT NULL,
  `ques` varchar(500) NOT NULL,
  `ans` int(1) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;

--
-- Dumping data for table `questions`
--

INSERT INTO `questions` (`quizId`, `ques`, `ans`) VALUES
('3ea00f20', 'ds', 0),
('3ea00f20', 'erty', 1),
('3ea00f20', 'ghjkl', 1),
('3ea00f20', 'jicjc', 0),
('1a998fb8', 'what is your name?', 1),
('1a998fb8', 'hallo', 1),
('1a998fb8', 'hahahaha', 0),
('f2d28521', 'p1', 0),
('f2d28521', 'p2', 1),
('f2d28521', 'p3', 1),
('f2d28521', 'p4', 1),
('f2d28521', 'p5', 0);

-- --------------------------------------------------------

--
-- Table structure for table `quiz`
--

CREATE TABLE `quiz` (
  `idQuiz` varchar(100) NOT NULL,
  `name` varchar(500) NOT NULL,
  `time` int(10) NOT NULL,
  `QN` int(5) NOT NULL,
  `date` date NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;

--
-- Dumping data for table `quiz`
--

INSERT INTO `quiz` (`idQuiz`, `name`, `time`, `QN`, `date`) VALUES
('1a998fb8', 'test2', 10, 3, '2022-12-21'),
('3ea00f20', 'sd', 5, 4, '2022-12-21'),
('f2d28521', 'test5', 5, 5, '2022-12-21');

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
-- Indexes for table `admin`
--
ALTER TABLE `admin`
  ADD UNIQUE KEY `user` (`user`);

--
-- Indexes for table `matrial`
--
ALTER TABLE `matrial`
  ADD PRIMARY KEY (`idFile`);

--
-- Indexes for table `quiz`
--
ALTER TABLE `quiz`
  ADD UNIQUE KEY `idQuiz` (`idQuiz`);

--
-- Indexes for table `student`
--
ALTER TABLE `student`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `matrial`
--
ALTER TABLE `matrial`
  MODIFY `idFile` int(100) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT for table `student`
--
ALTER TABLE `student`
  MODIFY `id` int(5) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=35;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
