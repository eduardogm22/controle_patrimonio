-- MySQL dump 10.13  Distrib 8.0.38, for Win64 (x86_64)
--
-- Host: localhost    Database: asset_ctrl
-- ------------------------------------------------------
-- Server version	8.3.0

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `patrimonios`
--

DROP TABLE IF EXISTS `patrimonios`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `patrimonios` (
  `idpatrimonio` int NOT NULL AUTO_INCREMENT,
  `nome` varchar(100) NOT NULL,
  `valor_unitario` decimal(10,2) NOT NULL,
  `data_recebimento` date DEFAULT NULL,
  `num_patrimonio` varchar(30) DEFAULT NULL,
  `num_serie` varchar(30) DEFAULT NULL,
  `idnota` int DEFAULT NULL,
  `idcategoria` int NOT NULL,
  `idsetor_responsavel` int NOT NULL,
  `idsituacao` int NOT NULL,
  PRIMARY KEY (`idpatrimonio`),
  KEY `fk_ptr_info_notas` (`idnota`),
  KEY `fk_ptr_categorias` (`idcategoria`),
  KEY `fk_ptr_setores_responsaveis` (`idsetor_responsavel`),
  KEY `fk_ptr_situacoes` (`idsituacao`)
) ENGINE=MyISAM AUTO_INCREMENT=105 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `patrimonios`
--

LOCK TABLES `patrimonios` WRITE;
/*!40000 ALTER TABLE `patrimonios` DISABLE KEYS */;
INSERT INTO `patrimonios` VALUES (104,'Produto teste',25.00,'2024-11-19',NULL,'',13,7,3,1),(103,'Produto teste',25.00,'2024-11-19',NULL,'',13,7,3,1),(101,'Produto teste',25.00,'2024-11-19',NULL,'',13,7,3,1),(102,'Produto teste',25.00,'2024-11-19',NULL,'',13,7,3,1),(100,'Cadeira Presidente id100',247.00,'2024-11-19',NULL,'',12,2,3,1),(99,'Cadeira Presidenteid 99',247.00,'2024-11-19',NULL,'',12,2,3,1),(97,'Cadeira Presidente',247.00,'2024-11-19',NULL,'',12,2,3,1),(98,'Cadeira Presidente id 98',247.00,'2024-11-19',NULL,'',12,2,3,1),(96,'Cadeira Presidente',247.00,'2024-11-19',NULL,'',12,2,3,1),(95,'Cadeira Presidente',247.00,'2024-11-19',NULL,'',12,2,3,1),(94,'Cadeira Presidente',247.00,'2024-11-19',NULL,'',12,2,3,1),(93,'Cadeira Presidente',247.00,'2024-11-19',NULL,'',12,2,3,1),(92,'Mesa Professor',250.00,'2024-11-19',NULL,'',12,3,3,1),(91,'Mesa Professor',250.00,'2024-11-19',NULL,'',12,3,3,1),(90,'Mesa Professor',250.00,'2024-11-19',NULL,'',12,3,3,1),(89,'Mesa Professor',250.00,'2024-11-19',NULL,'',12,3,3,1),(88,'Mesa Professor',250.00,'2024-11-19',NULL,'',12,3,3,1),(87,'Mesa Professor',250.00,'2024-11-19',NULL,'',12,3,3,1),(86,'Mesa Professor',250.00,'2024-11-19',NULL,'',12,3,3,1),(85,'Mesa Professor id 85',250.00,'2024-11-19',NULL,'',12,3,3,1),(84,'Mesa Professor',250.00,'2024-11-19',NULL,'',12,3,3,1),(83,'Mesa Professor',250.00,'2024-11-19',NULL,'',12,3,3,1),(82,'Mesa Professor',250.00,'2024-11-19',NULL,'',12,3,3,1),(81,'Mesa Professor',250.00,'2024-11-19',NULL,'',12,3,3,1),(80,'Mesa Professor',250.00,'2024-11-19',NULL,'',12,3,3,1),(79,'Mesa Professor',250.00,'2024-11-19',NULL,'',12,3,3,1);
/*!40000 ALTER TABLE `patrimonios` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-11-19 22:09:07
