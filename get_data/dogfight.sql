-- phpMyAdmin SQL Dump
-- version 5.0.4
-- https://www.phpmyadmin.net/
--
-- Hôte : 127.0.0.1
-- Généré le : Dim 09 fév. 2025 à 01:20
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
-- Structure de la table `dogfight`
--

CREATE TABLE `dogfight` (
  `id` int(11) NOT NULL,
  `jour` date NOT NULL DEFAULT current_timestamp(),
  `message` text DEFAULT NULL,
  `json` longtext CHARACTER SET utf8mb4 COLLATE utf8mb4_bin NOT NULL CHECK (json_valid(`json`))
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Déchargement des données de la table `dogfight`
--

INSERT INTO `dogfight` (`id`, `jour`, `message`, `json`) VALUES
(2, '20**-07-11', '** a descendu F-**** à 15h03 le 11-07-20**', '{\"glide\": [\"F-****\", *.6753833333333334, **.317933333333336, 682.1424000000001, 315, 114.81316149470803, -2.2098, -19.670382512302222], \"cible\": [\"F-****\", *.6760333333333333, **.31726666666667, 982.0656, 1, 85.18395852833176, -2.71272, -15.527857656266413]}'),
(3, '20**-07-11', '** a descendu F-**** à 15h09 le 11-07-20**', '{\"glide\": [\"F-****\", *.6924666666666668, **.32491666666667, 483.108, 331, 92.59125926992583, -0.19812000000000002, -25.662830173314592], \"cible\": [\"F-****\", *.6937666666666666, **.32225, 473.0496, 345, 90.7394340845273, -1.7068800000000002, -1.5412427245166964]}'),
(4, '20**-07-11', '** a descendu F-**** à 15h11 le 11-07-20**', '{\"glide\": [\"F-****\", *.6801499999999998, **.32373333333334, 665.0736, 256, 103.70221038231692, 2.6162, -13.820339620760924], \"cible\": [\"F-****\", 1.68005, 47.3232, 726.0336000000001, 244, 107.40586075311396, 2.01168, -28.431984881799302]}');

--
-- Index pour les tables déchargées
--

--
-- Index pour la table `dogfight`
--
ALTER TABLE `dogfight`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT pour les tables déchargées
--

--
-- AUTO_INCREMENT pour la table `dogfight`
--
ALTER TABLE `dogfight`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=174;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
