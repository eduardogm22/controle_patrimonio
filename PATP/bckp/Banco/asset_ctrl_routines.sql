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
-- Temporary view structure for view `principal_patrimonio_view`
--

DROP TABLE IF EXISTS `principal_patrimonio_view`;
/*!50001 DROP VIEW IF EXISTS `principal_patrimonio_view`*/;
SET @saved_cs_client     = @@character_set_client;
/*!50503 SET character_set_client = utf8mb4 */;
/*!50001 CREATE VIEW `principal_patrimonio_view` AS SELECT 
 1 AS `Patrimônio`,
 1 AS `Categoria`,
 1 AS `Núm. Patrimônio`,
 1 AS `Data de Aquisição`,
 1 AS `Situação`*/;
SET character_set_client = @saved_cs_client;

--
-- Temporary view structure for view `usuario_nome_view`
--

DROP TABLE IF EXISTS `usuario_nome_view`;
/*!50001 DROP VIEW IF EXISTS `usuario_nome_view`*/;
SET @saved_cs_client     = @@character_set_client;
/*!50503 SET character_set_client = utf8mb4 */;
/*!50001 CREATE VIEW `usuario_nome_view` AS SELECT 
 1 AS `idpessoa`,
 1 AS `usuario`,
 1 AS `nome`*/;
SET character_set_client = @saved_cs_client;

--
-- Final view structure for view `principal_patrimonio_view`
--

/*!50001 DROP VIEW IF EXISTS `principal_patrimonio_view`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8mb4 */;
/*!50001 SET character_set_results     = utf8mb4 */;
/*!50001 SET collation_connection      = utf8mb4_0900_ai_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`root`@`localhost` SQL SECURITY DEFINER */
/*!50001 VIEW `principal_patrimonio_view` AS select `ptr`.`nome` AS `Patrimônio`,`cat`.`nome` AS `Categoria`,`ptr`.`num_patrimonio` AS `Núm. Patrimônio`,`nta`.`data_aquisicao` AS `Data de Aquisição`,`sit`.`nome` AS `Situação` from ((((`patrimonios` `ptr` join `categorias` `cat` on((`ptr`.`idcategoria` = `cat`.`idcategoria`))) left join `info_notas` `nta` on((`ptr`.`idnota` = `nta`.`idnota`))) left join `setores_responsaveis` `srp` on((`ptr`.`idsetor_responsavel` = `srp`.`idsetor_responsavel`))) left join `situacoes` `sit` on((`ptr`.`idsituacao` = `sit`.`idsituacao`))) */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;

--
-- Final view structure for view `usuario_nome_view`
--

/*!50001 DROP VIEW IF EXISTS `usuario_nome_view`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8mb4 */;
/*!50001 SET character_set_results     = utf8mb4 */;
/*!50001 SET collation_connection      = utf8mb4_0900_ai_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`root`@`localhost` SQL SECURITY DEFINER */
/*!50001 VIEW `usuario_nome_view` AS select `usr`.`idpessoa` AS `idpessoa`,`usr`.`usuario` AS `usuario`,`pss`.`nome` AS `nome` from (`usuarios` `usr` join `pessoas` `pss` on((`usr`.`idpessoa` = `pss`.`idpessoa`))) */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-11-19 22:09:09
