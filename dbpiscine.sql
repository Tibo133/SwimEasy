-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- Hôte : 127.0.0.1:3306
-- Généré le : mar. 06 juin 2023 à 21:54
-- Version du serveur : 5.7.36
-- Version de PHP : 7.4.26

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de données : `dbpiscine`
--

-- --------------------------------------------------------

--
-- Structure de la table `avis`
--

DROP TABLE IF EXISTS `avis`;
CREATE TABLE IF NOT EXISTS `avis` (
  `NomPiscine` varchar(30) NOT NULL,
  `Jour` date NOT NULL,
  `Heure` varchar(5) NOT NULL,
  `Duree` varchar(5) NOT NULL,
  `Commentaire` varchar(250) NOT NULL,
  `ID_Avis` int(11) NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (`ID_Avis`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8;

--
-- Déchargement des données de la table `avis`
--

INSERT INTO `avis` (`NomPiscine`, `Jour`, `Heure`, `Duree`, `Commentaire`, `ID_Avis`) VALUES
('Charial', '2023-06-14', '13:40', '01:00', 'Tres agreable', 1),
('Poitier', '2023-10-12', '10:00', '02:00', 'Incroyable', 2),
('Molitor', '2022-07-01', '09:30', '01:30', 'Super sympa', 3),
('ChatGPT', '2022-05-04', '18:50', '01:00', 'Pas ouf a eviter', 4),
('Splash', '2021-02-23', '15:15', '02:00', 'Toujours au top', 5),
('Jean Bouin', '2022-08-17', '14:20', '01:30', 'Exceptionnel', 6),
('Pailleron', '2022-09-05', '16:45', '02:30', 'Experience incroyable', 7),
('Georges Hermant', '2022-11-30', '12:10', '01:30', 'A ne pas manquer', 8),
('Josephine Baker', '2022-12-15', '17:30', '01:30', 'Magnifique', 9),
('Keller', '2023-01-20', '19:45', '02:00', 'Vaut le detour', 10);

-- --------------------------------------------------------

--
-- Structure de la table `events`
--

DROP TABLE IF EXISTS `events`;
CREATE TABLE IF NOT EXISTS `events` (
  `EventID` int(11) NOT NULL AUTO_INCREMENT,
  `Participant` varchar(50) NOT NULL,
  `email` varchar(50) NOT NULL,
  `Niveau` varchar(50) NOT NULL,
  `RDVID` int(11) NOT NULL,
  PRIMARY KEY (`EventID`),
  KEY `RDVID` (`RDVID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Structure de la table `piscines`
--

DROP TABLE IF EXISTS `piscines`;
CREATE TABLE IF NOT EXISTS `piscines` (
  `Nom` varchar(30) NOT NULL,
  `Adresse` varchar(60) NOT NULL,
  `NbBassin` enum('1','2','3','4','5','6','7','8','9','10') NOT NULL,
  `Tarif` float NOT NULL,
  `HoraireO` varchar(5) NOT NULL,
  `HoraireF` varchar(5) NOT NULL,
  `ID_Piscine` int(11) NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (`ID_Piscine`)
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=utf8;

--
-- Déchargement des données de la table `piscines`
--

INSERT INTO `piscines` (`Nom`, `Adresse`, `NbBassin`, `Tarif`, `HoraireO`, `HoraireF`, `ID_Piscine`) VALUES
('Charial', '102 Rue Antoine Charial', '2', 15, '08:00', '18:00', 1),
('Balard', '181 Rue JeanPoitier', '4', 5, '13:00', '20:30', 2),
('Aquaboulevard', '4 Rue Louis Armand', '1', 20, '08:30', '19:30', 3),
('Georges Hermant', '18 rue Jean Bertin', '6', 13, '14:00', '20:10', 4),
('Molitor', '3 Avenue de la Porte Molitor', '3', 12, '09:00', '20:00', 5),
('JosÃ©phine Baker', 'Quai FranÃ§ois Mauriac', '7', 15, '10:00', '21:00', 6),
('Keller', '14 Rue de l Ingenieur Keller', '5', 18, '07:30', '22:00', 7),
('Pailleron', '32 Rue Edouard Pailleron', '1', 25, '06:30', '21:30', 8),
('Jean Bouin', '20 Rue Jean Bouin', '4', 10, '08:00', '19:30', 9),
('Olympique', '1 Boulevard de Bercy', '2', 30, '07:00', '22:30', 10),
('Roger Le Gall', '34 Boulevard Carnot', '6', 20, '09:30', '20:30', 11),
('RhÃ´ne', '8 Quai Claude Bernard', '3', 22, '07:00', '21:00', 12);

-- --------------------------------------------------------

--
-- Structure de la table `rdv`
--

DROP TABLE IF EXISTS `rdv`;
CREATE TABLE IF NOT EXISTS `rdv` (
  `Pseudo` varchar(50) NOT NULL,
  `NomPiscine` varchar(50) NOT NULL,
  `Adresse` varchar(50) NOT NULL,
  `Jour` date NOT NULL,
  `Heure` varchar(5) NOT NULL,
  `Mess` varchar(60) NOT NULL,
  `DureeRDV` varchar(5) NOT NULL,
  `ID_RDV` int(11) NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (`ID_RDV`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8;

--
-- Déchargement des données de la table `rdv`
--

INSERT INTO `rdv` (`Pseudo`, `NomPiscine`, `Adresse`, `Jour`, `Heure`, `Mess`, `DureeRDV`, `ID_RDV`) VALUES
('Michel', 'Charial', '120 rue Antoine Charial', '2023-06-28', '15:00', 'On va faire des acl sous l eau', '01:00', 2),
('Molliex', 'Splash', '5 rue Jean', '2023-11-12', '17:20', 'On va faire des maths sous l eau', '02:30', 3),
('Bergeron', 'Jean Bouin', '200 rue Antoinette', '2023-07-12', '17:30', 'Venez m affronter', '01:20', 4),
('Jamont', 'Sunshine', '152 rue loinloin', '2023-06-25', '09:00', 'Venez nombreux', '00:50', 5),
('Duccini', 'Splash', '18 rue loin', '2023-06-29', '17:50', 'On va s entrainer tous ensemble', '01:00', 6);

--
-- Contraintes pour les tables déchargées
--

--
-- Contraintes pour la table `events`
--
ALTER TABLE `events`
  ADD CONSTRAINT `events_ibfk_1` FOREIGN KEY (`RDVID`) REFERENCES `rdv` (`ID_RDV`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
