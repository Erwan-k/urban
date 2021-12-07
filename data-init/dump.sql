 SET NAMES utf8 ;
DROP TABLE IF EXISTS `Token`;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `Token` (
  `adresse_mail` varchar(255) DEFAULT NULL,
  `token_` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

LOCK TABLES `Token` WRITE;

UNLOCK TABLES;
DROP TABLE IF EXISTS `Player`;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `Player` (
  `adresse_mail` varchar(255) DEFAULT NULL,
  `mdp` varchar(255) DEFAULT NULL,
  `lastname` varchar(255) DEFAULT NULL,
  `firstname` varchar(255) DEFAULT NULL,
  `age` int(3) DEFAULT NULL,
  `avatar` int(3) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

LOCK TABLES `Player` WRITE;

UNLOCK TABLES;
DROP TABLE IF EXISTS `Match`;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `Match` (
  `reference` int(6) DEFAULT NULL,
  `adresse` varchar(255) DEFAULT NULL,
  `day` varchar(255) DEFAULT NULL,
  `hour` varchar(255) DEFAULT NULL,
  `organisateur` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

LOCK TABLES `Match` WRITE;

UNLOCK TABLES;
DROP TABLE IF EXISTS `Team`;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `Team` (
  `ref_match` int(6) DEFAULT NULL,
  `ref_player` varchar(255) DEFAULT NULL,
  `team_color` varchar(255) DEFAULT NULL,
  `date` int(10) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

LOCK TABLES `Team` WRITE;

UNLOCK TABLES;
DROP TABLE IF EXISTS `Adresse_mail_non_verif`;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `Adresse_mail_non_verif` (
  `adresse_mail` varchar(255) DEFAULT NULL,
  `code` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

LOCK TABLES `Adresse_mail_non_verif` WRITE;

UNLOCK TABLES;
DROP TABLE IF EXISTS `Changement_de_mot_de_passe`;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `Changement_de_mot_de_passe` (
  `adresse_mail` varchar(255) DEFAULT NULL,
  `code` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

LOCK TABLES `Changement_de_mot_de_passe` WRITE;

UNLOCK TABLES;
