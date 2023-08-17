-- phpMyAdmin SQL Dump
-- version 5.0.2
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Sep 04, 2020 at 02:16 PM
-- Server version: 10.4.13-MariaDB
-- PHP Version: 7.4.7

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `library`
--

-- --------------------------------------------------------

--
-- Table structure for table `books`
--

CREATE TABLE `books` (
  `Book_ID` varchar(100) NOT NULL,
  `Book_name` varchar(100) NOT NULL,
  `Type` varchar(100) NOT NULL,
  `Author` varchar(100) NOT NULL,
  `Copies` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `books`
--

INSERT INTO `books` (`Book_ID`, `Book_name`, `Type`, `Author`, `Copies`) VALUES
('#E des11', 'End and Means', 'fiction', 'Huxlay', '4'),
('#GeoTo8', 'Games of Throne', 'fiction', 'George RR Martin', '96'),
('#Hl4', 'Hamlet', 'fiction', 'William Shakespeare', '101'),
('#Hl8', 'Hamlet', 'fiction', 'William Shakespeare', '85'),
('#hrpt9', 'harry potter', 'friction', 'jk', '23'),
('#PasLt1', 'Paradise Lost', 'fiction', 'John Milton', '31'),
('#Rea lt6', 'Romeo and Juliet', 'fiction', 'William Shakespeare', '94'),
('#T a  YnGl6', 'The Diary of a Young Girl', 'non_fiction', 'Anne Frank', '47'),
('#T in0', 'The Shining', 'non_fiction', 'Stephen King', '61'),
('#T ptcoBnEnt5', 'The Importance of Being Earnest', 'fiction', 'Oscar Wilde', '44');

-- --------------------------------------------------------

--
-- Table structure for table `book_returned`
--

CREATE TABLE `book_returned` (
  `Student_name` varchar(100) NOT NULL,
  `Book_id` varchar(100) NOT NULL,
  `Book_name` varchar(100) NOT NULL,
  `Return_date` varchar(100) NOT NULL,
  `id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `book_returned`
--

INSERT INTO `book_returned` (`Student_name`, `Book_id`, `Book_name`, `Return_date`, `id`) VALUES
('Ram', 'harry potter', '2020/8/9', '2020/7/8', 36),
('Punam', 'Games of Throne', '2020/8/9', '2021/7/10', 37);

-- --------------------------------------------------------

--
-- Table structure for table `issue`
--

CREATE TABLE `issue` (
  `id` int(11) NOT NULL,
  `Student_name` varchar(100) NOT NULL,
  `Book_id` varchar(100) NOT NULL,
  `Issue_date` varchar(100) NOT NULL,
  `Expiry_date` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `issue`
--

INSERT INTO `issue` (`id`, `Student_name`, `Book_id`, `Issue_date`, `Expiry_date`) VALUES
(11, 'Shyam', '#T cmt8', '2020/7/8', '2021/7/7'),
(18, 'Ram', '#hrpt9', '2020/8/9', '2021/01/9'),
(19, 'Ram', '#hrpt9', '2020/8/9', '2021/01/9'),
(20, 'Ram', '#hrpt9', '2020/8/9', '2021/01/9'),
(21, 'Ram', '#hrpt9', '2020/8/9', '2021/01/9'),
(22, 'Ram', '#hrpt9', '2020/8/9', '2021/01/9'),
(23, 'Ram', '#hrpt9', '2020/8/9', '2021/01/9'),
(24, 'Ram', '#hrpt9', '2020/8/9', '2021/01/9');

-- --------------------------------------------------------

--
-- Table structure for table `user_details`
--

CREATE TABLE `user_details` (
  `User_id` int(11) NOT NULL,
  `Username` varchar(100) NOT NULL,
  `Password` varchar(100) NOT NULL,
  `First_name` varchar(100) NOT NULL,
  `last_name` varchar(100) NOT NULL,
  `Date_of_Birth` varchar(100) NOT NULL,
  `City` varchar(100) NOT NULL,
  `Province` varchar(100) NOT NULL,
  `Number` varchar(100) NOT NULL,
  `Email` varchar(100) NOT NULL,
  `Gender` varchar(100) NOT NULL,
  `Marital` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `user_details`
--

INSERT INTO `user_details` (`User_id`, `Username`, `Password`, `First_name`, `last_name`, `Date_of_Birth`, `City`, `Province`, `Number`, `Email`, `Gender`, `Marital`) VALUES
(1, 'laxu', '', 'laxmi', 'sapkota', '2000/8/9', 'kritipur', '3', '+97798746561231', 'sapkotalaxu111@gmail.com', 'Female', 'Unmarried'),
(3, 'sita', 'sapkota', 'sita', 'sapkota', '2000/8/9', 'bagbazar', '3', '+977987456133123', 'sita@sapkota@gmail.com', 'Female', 'Married'),
(4, 'Jerry', 'Sapkota', 'Jerry', 'sapkota', '2000/8/9', 'Bagbazar', '4', '+9779874565612', 'jerry@gmail.com', 'Female', 'Unmarried'),
(6, 'Alu', 'student', 'alisha', 'Adhikari', '2000/8/9', 'putalisadak', '4', '4522125', 'alisha@adhikari', 'female', 'married'),
(7, 'Tom', 'sapkota', 'Tommy', 'sapkota', '2000/7/8', 'kritipur', '7', '+97798745612356', 'tommy@gmail.com', 'Male', 'Unmarried'),
(8, '', '', 'Alisha', 'Adhikari', '', '', '', '+', '', '-', '-'),
(9, 'Ali', 'adhikari', 'Alisha', 'Adhikari', '1995/8/9', 'dillibazar', '3', '+9779874561231', 'alisha.adhikari@gmail.com', 'Female', 'Unmarried');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `books`
--
ALTER TABLE `books`
  ADD UNIQUE KEY `Book_ID` (`Book_ID`);

--
-- Indexes for table `book_returned`
--
ALTER TABLE `book_returned`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `issue`
--
ALTER TABLE `issue`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `user_details`
--
ALTER TABLE `user_details`
  ADD PRIMARY KEY (`User_id`),
  ADD UNIQUE KEY `Username` (`Username`),
  ADD UNIQUE KEY `Number` (`Number`),
  ADD UNIQUE KEY `Email` (`Email`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `book_returned`
--
ALTER TABLE `book_returned`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=38;

--
-- AUTO_INCREMENT for table `issue`
--
ALTER TABLE `issue`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=25;

--
-- AUTO_INCREMENT for table `user_details`
--
ALTER TABLE `user_details`
  MODIFY `User_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=18;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
