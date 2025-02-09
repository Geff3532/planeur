# planeur

# 1ere planche de vol

A l'aide des données recupérer via get_data_planche.py dans le dossier du meme nom, on recupere toutes les données flarm en live, filtré par les immatriculations de planeur rentrées dans acs.sql
On les traite pour detecter les decollages et atterissages, via une classe objet defini dans acs__class.py, et on stocke tout ca en base de données. Un peu de statistiques (angle moyen d'inclinaison, % de spirale gauche/droite, altitude maximale)
index.php et tout ce qui en découle (logbook.php / css) sert a l'affichage des vols par jour 
on peut aussi voir la position en temps réel sur une carte dynamique si il est en vol

# 2nd option dogfight

En utilisant dogfight.py au lieu de get_data_planche, en plus de générer une planche journalière, calcule si un planeur a virtuellement "shooté" un autre sous certaines conditions (hauteur sol mini, distance mini et maxi, angle d'ouverture par rapport a l'axe du tireur, delta hauteur max, temps de respawn ect)
Peut generer un message whatsapp a chaque kill
Genere la planche de vol comme la partie 1 avec toutes les stats et meme possibilités, + la possibilite de voir le detail de la journee avec toute les killmaps sur fond de carte dynamique, compteur par vol ect

données anonymes en exemple + les structures de base de données dans les fichiers.sql
