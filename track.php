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
            <div class="menu">
            <img class="img-menu" src="/aeroclub/menu.png" alt="image">
                <div class="info-complementaire">
                    <p id="info-supp"></p>
                </div>
            </div>
            <div class="info-principale">
                <h3 id="Reg"></h3>
                <h4 id="Type"></h4>
                <p id="Day"></p>
                <p id="Ground_speed"></p>
                <p id="Climb_rate"></p>
                <p id="Altitude"></p>
                <p id="Track"></p>
                <p id="Distance"></p>
                <p id="Turn_rate"></p>
            </div>
        </div>
    </div>
    <script type="application/javascript" src="http://localhost//aeroclub//node_modules//leaflet-rotatedmarker//leaflet.rotatedMarker.js"></script>
    <script src="http://localhost//aeroclub//map.js"></script>
</body>
</html>