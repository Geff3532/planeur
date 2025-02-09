-- phpMyAdmin SQL Dump
-- version 5.0.4
-- https://www.phpmyadmin.net/
--
-- Hôte : 127.0.0.1
-- Généré le : Dim 09 fév. 2025 à 01:18
-- Version du serveur :  10.4.17-MariaDB
-- Version de PHP : 8.0.0

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de données : `test`
--

-- --------------------------------------------------------

--
-- Structure de la table `acs_planche`
--

CREATE TABLE `acs_planche` (
  `id` bigint(11) NOT NULL,
  `Reg` varchar(25) DEFAULT NULL,
  `Type` varchar(25) DEFAULT NULL,
  `Day` date DEFAULT NULL,
  `Start` time DEFAULT NULL,
  `Stop` time DEFAULT NULL,
  `Latitude` decimal(10,6) DEFAULT NULL,
  `Longitude` decimal(10,6) DEFAULT NULL,
  `Altitude` decimal(10,0) DEFAULT NULL,
  `Max_alt` decimal(10,0) DEFAULT NULL,
  `Ground_speed` decimal(10,1) DEFAULT NULL,
  `Climb_rate` decimal(10,2) DEFAULT NULL,
  `Turn_rate` decimal(10,2) DEFAULT NULL,
  `Track` decimal(10,0) DEFAULT NULL,
  `Avg_turn` decimal(10,1) DEFAULT NULL,
  `Spirale` varchar(50) DEFAULT NULL,
  `comment` varchar(50) DEFAULT NULL,
  `Kills` int(11) NOT NULL DEFAULT 0
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Déchargement des données de la table `acs_planche`
--

INSERT INTO `acs_planche` (`id`, `Reg`, `Type`, `Day`, `Start`, `Stop`, `Latitude`, `Longitude`, `Altitude`, `Max_alt`, `Ground_speed`, `Climb_rate`, `Turn_rate`, `Track`, `Avg_turn`, `Spirale`, `comment`, `Kills`) VALUES
(6023520, 'F-****', '*****', '20**-07-16', '**:04:27', '**:56:19', '**.313283', '*.689017', '80', '1374', '22.2', '0.10', '1.13', '77', '16.5', '57% spirale gauche/43% spirale droite', NULL, 0),
(375990627, 'D-****', '*****', '20**-07-14', '**:16:59', NULL, '**.042333', '*.906167', '1121', '5539', '175.9', '1.61', '2.99', '13', NULL, NULL, NULL, 0),
(2096355383, 'F-****', '*****', '20**-07-16', '**:37:41', '**:11:58', '**.314250', '*.690567', '82', '1621', '24.1', '0.10', '0.41', '59', '14.8', '20% spirale gauche/80% spirale droite', NULL, 2);

--
-- Index pour les tables déchargées
--

--
-- Index pour la table `acs_planche`
--
ALTER TABLE `acs_planche`
  ADD PRIMARY KEY (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
