<?php

$uri = rtrim(dirname($_SERVER["SCRIPT_NAME"]), '/');
$uri = trim(str_replace( $uri, '', $_SERVER['REQUEST_URI'] ), '/');
$uri = urldecode($uri);
$uri = substr($uri,10);

$regles = array( 
    'track' => "track/[0-9]{11}",
    'cible'   => "[0-9]{2}-[0-9]{2}-[0-9]{4}/[A-Z]-[A-Z]{4}", 
    'logbook' => "[0-9]{2}-[0-9]{2}-[0-9]{4}",
    'kills' => "kills/[0-9]{2}-[0-9]{2}-[0-9]{4}",        
    'visu_kills' => "kills/[0-9]+",           
    'accueil' => ""                                  
);

foreach ($regles as $action => $regle) 
{
    if (preg_match('~^'.$regle.'$~i',$uri)) 
    {
        if ($action == "accueil")
        {
            $date = date_create("now");
            require_once('logbook.php');
        }

        if ($action == "logbook")
        {
            list($day,$month,$year) = explode('-',$uri);
            $date = date_create_from_format('d-m-Y',$uri);

            if (!checkdate($month,$day,$year) || date_diff($date,date_create("now"))->invert)
            {
                require_once('404.php');
                exit();
            }

            require_once('logbook.php');
        }

        if ($action == "cible")
        {
            list($date,$reg) = explode('/',$uri);
            list($day,$month,$year) = explode('-',$date);
            $date = date_create_from_format('d-m-Y',$date);
            $db = new PDO('mysql:host=localhost;dbname=test;charset=utf8','root','',[PDO::ATTR_ERRMODE => PDO::ERRMODE_EXCEPTION]);
            $rep = $db->prepare("SELECT Immatriculation FROM acs");
            $rep->execute();
            $acs = array();
            foreach ($rep->fetchAll() as $row) 
            {
                array_push($acs,$row[0]);
            }

            if (!checkdate($month,$day,$year) || date_diff($date,date_create("now"))->invert || !in_array($reg,$acs))
            {
                require_once('404.php');
                exit();
            }
            
            require_once('cible.php');
        }

        if ($action == "track")
        {            
            require_once('track.php');
        }

        if ($action == "kills")
        {
            list($noting,$date) = explode('/',$uri);
            list($day,$month,$year) = explode('-',$date);
            $date = date_create_from_format('d-m-Y',$date);

            if (!checkdate($month,$day,$year) || date_diff($date,date_create("now"))->invert)
            {
                require_once('404.php');
                exit();
            }

            require_once('kills.php');
        }

        if ($action == "visu_kills")
        {
            require_once('visu_kills.php');
        }

        exit();

    }
}

include_once('404.php');