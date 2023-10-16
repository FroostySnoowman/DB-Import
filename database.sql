-- MySQL Export

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";

-- Table structure for table `Test`
--
CREATE TABLE `Test` (
  `Testing_Column` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- Dumping data for table `Test`
--
INSERT INTO Test VALUES ('1');

COMMIT;