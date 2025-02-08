<?php
$db = new PDO('mysql:host=localhost;dbname=test;charset=utf8','root','');
$rep = $db->prepare("SELECT id,Reg,Type,Start,Stop,Max_alt,Kills FROM acs_planche WHERE day = :day ORDER BY Start ASC");
$rep->execute([':day' => date_format($date,'Y-m-d')]);

$yesterday = clone $date;
$tomorrow = clone $date;
?>

<!DOCTYPE html>
<html lang='fr'>
    <head>
        <meta charset="utf-8" />
        <title>Planche de vol</title>
        <link rel="stylesheet" type="text/css" href="/aeroclub/logbook.css" media="all"/>
    </head>
        
    <body>
        <div id="header">
            <div id="selector">
                <?php
                $diff = date_diff($yesterday,date_create('now'));
                if ($diff->invert == 0 && $diff->y < 2)
                {
                    ?>
                        <a class="arrow-selector" href="/aeroclub/index.php/<?=date_format(date_sub($yesterday,date_interval_create_from_date_string('1 day')),'d-m-Y')?>"><</a>
                    <?php
                }
                ?>     
                <h2>Planche de vol du <?=date_format($date,'d-m-Y')?></h2>
                <?php
                $diff = date_diff($tomorrow,date_create('now'));
                if ($diff->invert == 0 && $diff-> days > 0)
                {
                    ?>
                    <a class="arrow-selector" href="/aeroclub/index.php/<?=date_format(date_add($tomorrow,date_interval_create_from_date_string('1 day')),'d-m-Y')?>">></a>
                    <?php
                }
                ?>
            </div>
            <a href="/aeroclub/index.php">Aujourd'hui</a><br><br>
            <a href="/aeroclub/index.php/kills/<?=date_format(date_create('now'),'d-m-Y')?>">Kills</a>
        </div>
    <table class="table-logbook">
        <tr>
            <th>Immat</th>
            <th>Type</th>
            <th>Début</th>
            <th>Fin</th>
            <th>Duree</th>
            <th>Max Altitude QNH</th>
            <th>SAR</th>
            <th>Kills</th>
        </tr>
<?php
while ($data = $rep->fetch())
{
    $start = new DateTime($data['Start']);
    if ($data['Stop'] != Null) $stop = new DateTime($data['Stop']);
    else $stop = Null
    ?><tr>
    <td><a href="/aeroclub/index.php/<?=date_format($date,'d-m-Y')?>/<?=$data['Reg']?>"><?=$data['Reg']?></a></td>
    <td><?=$data['Type']?></td>
    <td><?=$start->format('H\hi')?></td>
    <td><?php if ($stop!=Null) {echo($stop->format('H\hi'));}
    else { echo(Null); }?></td>
    <td><?php if ($stop != Null) { echo(date_diff($start,$stop)->format('%H:%I')); }
    else { echo(Null); }?></td>
    <td><?=$data['Max_alt']?> m</td>
    <td>
    <?php
    if ($stop == Null)
    {
        echo("<a href='/aeroclub/index.php/track/".$data['id']."'><p style='color:red;'>#</p></a>");
    }
    else
    {
        echo("<a href='/aeroclub/index.php/track/".$data['id']."'><p style='color:green;'>#</p></a>");
    }
    ?>
    </td>
    <td><?=$data['Kills']?></td>
    </tr>
<?php
}
$rep->closeCursor();
?>
    </table>
    </body>
</html>