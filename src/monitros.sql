-- MariaDB dump 10.19  Distrib 10.4.21-MariaDB, for Win64 (AMD64)
--
-- Host: localhost    Database: monitros
-- ------------------------------------------------------
<<<<<<< HEAD
-- Server version	10.6.5-MariaDB
=======
-- Server version	10.4.21-MariaDB
>>>>>>> 00f631db09c8e0d3e9ae5b6604feaddc1aa574b7

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `data_user`
--

DROP TABLE IF EXISTS `data_user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `data_user` (
  `Username` varchar(15) NOT NULL,
  `Password` varchar(50) NOT NULL,
  `Nama_lengkap` varchar(25) NOT NULL,
  `Nomor_HP` int(15) NOT NULL,
  `Alamat` varchar(25) NOT NULL,
  `Role` varchar(10) NOT NULL,
  PRIMARY KEY (`Username`),
  KEY `role_idx` (`Role`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `data_user`
--

LOCK TABLES `data_user` WRITE;
/*!40000 ALTER TABLE `data_user` DISABLE KEYS */;
INSERT INTO `data_user` VALUES ('arga34','arga','Arga Aminuddin',21921782,'Tangerang','Karyawan'),('brunofernandes','united4life','Bruno Fernandes',2147483647,'Manchester','Karyawan');
/*!40000 ALTER TABLE `data_user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `menu`
--

DROP TABLE IF EXISTS `menu`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `menu` (
  `IDMenu` int(11) NOT NULL,
  `Nama_Menu` varchar(50) NOT NULL,
  `Deskripsi` varchar(100) NOT NULL,
  PRIMARY KEY (`IDMenu`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `menu`
--

LOCK TABLES `menu` WRITE;
/*!40000 ALTER TABLE `menu` DISABLE KEYS */;
INSERT INTO `menu` VALUES (1,'Nasi goreng','Isi sosis, ayam, bakso');
/*!40000 ALTER TABLE `menu` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `peralatan`
--

DROP TABLE IF EXISTS `peralatan`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `peralatan` (
  `IDPeralatan` int(11) NOT NULL,
  `Nama_Peralatan` varchar(50) NOT NULL,
  `Tipe_Peralatan` varchar(25) NOT NULL,
  `Jumlah_Ideal` int(11) NOT NULL,
  `Jumlah_Peralatan` int(11) NOT NULL,
  `Kondisi` varchar(25) NOT NULL,
  PRIMARY KEY (`IDPeralatan`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `peralatan`
--

LOCK TABLES `peralatan` WRITE;
/*!40000 ALTER TABLE `peralatan` DISABLE KEYS */;
INSERT INTO `peralatan` VALUES (1,'Piring','AlatMakan',200,170,'Butuh Beli Baru'),(2,'Sendok','AlatMakan',200,130,'Butuh Beli Baru'),(3,'Garpu','AlatMakan',100,70,'Butuh Beli Baru'),(4,'Sumpit','AlatMakan',100,90,'Aman'),(5,'MangkokM','AlatMakan',150,145,'Aman'),(6,'Burner','AlatMeja',15,15,'Aman'),(7,'Tong','AlatMakan',30,30,'Aman'),(8,'Gunting','AlatMakan',15,15,'Aman'),(9,'Gelas','AlatMakan',80,75,'Aman'),(10,'Pitcher','AlatWaiter',10,9,'Aman'),(11,'Sapu','AlatKebersihan',10,10,'Aman'),(12,'Pel','AlatKebersihan',10,10,'Aman'),(13,'Kain Lap','AlatKebersihan',20,14,'Butuh Beli Baru'),(14,'Kotak Tissue','AlatMeja',45,20,'Butuh Beli Baru'),(15,'Condament','AlatMeja',30,29,'Aman'),(16,'Tong Sampah','AlatMeja',6,6,'Aman'),(17,'Tray','AlatWaiter',8,8,'Aman');
/*!40000 ALTER TABLE `peralatan` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `todolist`
--

DROP TABLE IF EXISTS `todolist`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `todolist` (
  `IDPekerjaan` int(11) NOT NULL,
  `Username` varchar(15) NOT NULL,
  `Role` varchar(10) NOT NULL,
  `Nama_Pekerjaan` varchar(50) NOT NULL,
  `Deskripsi` varchar(50) NOT NULL,
  `Status` varchar(25) NOT NULL,
  PRIMARY KEY (`IDPekerjaan`),
  KEY `fk_usr` (`Username`),
  KEY `fk_role` (`Role`),
  CONSTRAINT `fk_role` FOREIGN KEY (`Role`) REFERENCES `data_user` (`Role`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `fk_usr` FOREIGN KEY (`Username`) REFERENCES `data_user` (`Username`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `todolist`
--

LOCK TABLES `todolist` WRITE;
/*!40000 ALTER TABLE `todolist` DISABLE KEYS */;
INSERT INTO `todolist` VALUES (1,'arga34','Karyawan','Rekap Penjualan','Mengecek ulang dan merekap hasil penjualan','Belum Dilakukan'),(2,'brunofernandes','Karyawan','Update stok','Hitung dan validasi stok di gudang','Sudah dilakukan');
/*!40000 ALTER TABLE `todolist` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2021-11-24  8:03:00
