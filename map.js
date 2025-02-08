//Definir la map

var marker;
var polyline;

const init_map = (callback) =>  
{
    let xhr_object = new XMLHttpRequest(); 
        
    xhr_object.open("GET", "http://localhost:3000/api/"+document.location.href.substring(document.location.href.lastIndexOf('/')+1), true); 
        
    xhr_object.onreadystatechange = () => 
    { 
        if (xhr_object.readyState == 4 && xhr_object.status == 200) 
        {
            let json = JSON.parse(xhr_object.responseText); 
            display(json);
            callback(json);
        }
        if (xhr_object.readyState == 4 && xhr_object.status != 200) 
        {
            console.log(error);
        }
    } 
    
    xhr_object.send(); 
}

init_map(json => 
{
    let mapOptions = 
    {
        center : [json['Latitude'],json['Longitude']], 
        zoom   : 13
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

    let gliderIcon = L.icon({
        iconUrl    : '/aeroclub/glider.png',
        iconSize   : [82,67], 
        iconAnchor : [41,33]
    });

    marker = new L.Marker([json['Latitude'],json['Longitude']],{icon:gliderIcon,alt:"image's glider"}).addTo(map);
    
    polyline = new L.Polyline(marker.getLatLng(), {color: 'blue'}).addTo(map);

    update(json);
});

const update = (json) => 
{
    marker.setLatLng([json['Latitude'], json['Longitude']]);
    marker.setRotationAngle(json['Track']);
    polyline.addLatLng(marker.getLatLng());
}

const xhr_request = () =>  
{
    let xhr_object = new XMLHttpRequest(); 
        
    xhr_object.open("GET", "http://localhost:3000/api/"+document.location.href.substring(document.location.href.lastIndexOf('/')+1), true); 
        
    xhr_object.onreadystatechange = () => 
    { 
        if (xhr_object.readyState == 4 && xhr_object.status == 200) 
        {
            let json = JSON.parse(xhr_object.responseText); 
            display(json);
            update(json);
        }
        if (xhr_object.readyState == 4 && xhr_object.status != 200) 
        {
            console.log(error);
        }
    } 
    
    xhr_object.send(); 
}

const display = (json) => 
{
    document.getElementById('Reg').textContent = json['Reg'] || null;
    document.getElementById('Type').textContent = json['Type'] || null;
    document.getElementById('Day').textContent = json['Day'].split('T')[0] || null;
    document.getElementById('Ground_speed').textContent = `Vitesse sol : ${json['Ground_speed']} km/h` || null;
    document.getElementById('Climb_rate').textContent = `Variomètre : ${json['Climb_rate']} m/s` || null;
    document.getElementById('Altitude').textContent = `Altitude (QNH) : ${json['Altitude']} m` || null;
    document.getElementById('Distance').textContent = `Distance : ${distance(json['Latitude'],json['Longitude'],47.316681, 1.690537)} km` || null;
    document.getElementById('Track').textContent = `Cap : ${json['Track']}` || null;
    document.getElementById('Turn_rate').textContent = (json['Turn_rate'] > 10) ? `Turn Rate : ${Math.round(json['Turn_rate'])}` : null;
    document.getElementById('info-supp').textContent = (json['Avg_turn'] != null && json['Spirale'] != null) ? 'Inclinaison moyenne : ' + (json['Avg_turn']) + ' degres\n' + (json['Spirale']) : "Pas d'informations complementaires";
}

const distance = (lat1,long1,lat2,long2) => 
{
    lat1 = Math.PI*(90-lat1)/180
    lat2 = Math.PI*(90-lat2)/180
    long1 = Math.PI*long1/180
    long2 = Math.PI*long2/180
    let x = Math.cos(lat1)*Math.cos(lat2) + Math.sin(lat1)*Math.sin(lat2)*Math.cos(long2-long1);
    return Math.round(6371*Math.acos(x)*10)/10;
}

window.setInterval('xhr_request()',5000);