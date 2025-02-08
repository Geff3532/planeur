const distance = (lat1,long1,lat2,long2) => 
{
    lat1 = Math.PI*(90-lat1)/180
    lat2 = Math.PI*(90-lat2)/180
    long1 = Math.PI*long1/180
    long2 = Math.PI*long2/180
    let x = Math.cos(lat1)*Math.cos(lat2) + Math.sin(lat1)*Math.sin(lat2)*Math.cos(long2-long1);
    return Math.round(6371*Math.acos(x)*1000);
}

let mapOptions = 
{
    center : [json['glide'][2],json['glide'][1]], 
    zoom   : 15
}

let map = new L.Map('map', mapOptions);
let layer = new L.TileLayer('http://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png');
map.addLayer(layer);

// Tracer 5 cercles de 10,20,30,40,50 km de rayon autour de romo

for (var i = 1; i < 6; i++)
{
    let circle = new L.Circle([47.316681, 1.690537],{radius: 10000*i,fill: false,weight:2,color:'red'}).addTo(map);
}

// Definir l'image du planeur

let glideIcon = L.icon({
    iconUrl    : '/aeroclub/glider.png',
    iconSize   : [62,50], 
    iconAnchor : [31,25]
});

let cibleIcon = L.icon({
    iconUrl    : '/aeroclub/glider.png',
    iconSize   : [62,50], 
    iconAnchor : [31,25]
});

glide = new L.Marker([json['glide'][2],json['glide'][1]],{icon:glideIcon,alt:"image's glider"}).addTo(map);
cible = new L.Marker([json['cible'][2],json['cible'][1]],{icon:cibleIcon,alt:"image's glider"}).addTo(map);
glide.bindPopup(json['glide'][0]);
cible.bindPopup(json['cible'][0]);
glide.setRotationAngle(json['glide'][4]);
cible.setRotationAngle(json['cible'][4]);

document.getElementById('distance').textContent = `Distance : ${distance(json['cible'][2],json['cible'][1],json['glide'][2],json['glide'][1])} m` || null;