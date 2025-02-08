<?php
$uri = rtrim(dirname($_SERVER["SCRIPT_NAME"]), '/');
$uri = trim(str_replace( $uri, '', $_SERVER['REQUEST_URI'] ), '/');
$uri = urldecode($uri);
$id = substr($uri,16);

$db = new PDO('mysql:host=localhost;dbname=test;charset=utf8','root','',[PDO::ATTR_ERRMODE => PDO::ERRMODE_EXCEPTION]);
$rep = $db->prepare('SELECT json FROM dogfight WHERE id = :id');
$rep->execute([':id' => $id]);

$data = $rep->fetch();
$data = json_decode($data[0]);

$glide = $data->glide;
$cible = $data->cible;

?>

<!DOCTYPE html>
<html lang="fr">
 <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Track</title>
    <link rel="stylesheet" href="https://unpkg.com/leaflet@1.7.1/dist/leaflet.css"/>
    <link rel="stylesheet" href="/aeroclub/track.css">
    <script src="https://unpkg.com/leaflet@1.7.1/dist/leaflet.js"></script>
 </head>
 <body>
    <div id="container">
        <div id="map"></div>
        <div id="map_information">
            <div class="info-principale">
                <h4 id="distance"></h4>
                <h3><?=$glide[0]?></h3>
                <p>Altitude : <?=round($glide[3])?> m<br>Vitesse :  <?=round($glide[5])?> km/h<br>Vz : <?=round($glide[6]*10)/10?> m/s</p>
                <h3><?=$cible[0]?></h3>
                <p>Altitude : <?=round($cible[3])?> m<br>Vitesse :  <?=round($cible[5])?> km/h<br>Vz : <?=round($cible[6]*10)/10?> m/s</p>
            </div>
        </div>
    </div>
    <script type="application/javascript" src="http://localhost//aeroclub//node_modules//leaflet-rotatedmarker//leaflet.rotatedMarker.js"></script>
    <script type="application/javascript">
        let json = {
            "glide":[
                "<?=$glide[0]?>",<?=$glide[1]?>,<?=$glide[2]?>,<?=$glide[3]?>,<?=$glide[4]?>,<?=$glide[5]?>,<?=$glide[6]?>,<?=$glide[7]?>
            ],
            "cible": [
                "<?=$cible[0]?>",<?=$cible[1]?>,<?=$cible[2]?>,<?=$cible[3]?>,<?=$cible[4]?>,<?=$cible[5]?>,<?=$cible[6]?>,<?=$cible[7]?>
            ] 
        }
    </script>
    <script src="http://localhost//aeroclub//kills.js"></script>
</body>
</html>