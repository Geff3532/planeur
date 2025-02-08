<?php
$db = new PDO('mysql:host=localhost;dbname=test;charset=utf8','root','',[PDO::ATTR_ERRMODE => PDO::ERRMODE_EXCEPTION]);
$rep = $db->prepare('SELECT id,message FROM dogfight WHERE jour = :day');
$rep->execute([':day' => date_format($date,'Y-m-d')]);

$yesterday = clone $date;
$tomorrow = clone $date;
?>

<!DOCTYPE html>
<html lang='fr'>
    <head>
        <meta charset="utf-8" />
        <title>Kills du jour</title>
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
                        <a class="arrow-selector" href="/aeroclub/index.php/kills/<?=date_format(date_sub($yesterday,date_interval_create_from_date_string('1 day')),'d-m-Y')?>"><</a>
                    <?php
                }
                ?>     
                <h2>Kills du <?=date_format($date,'d-m-Y')?></h2>
                <?php
                $diff = date_diff($tomorrow,date_create('now'));
                if ($diff->invert == 0 && $diff-> days > 0)
                {
                    ?>
                    <a class="arrow-selector" href="/aeroclub/index.php/kills/<?=date_format(date_add($tomorrow,date_interval_create_from_date_string('1 day')),'d-m-Y')?>">></a>
                    <?php
                }
                ?>
            </div>
            <a href="/aeroclub/index.php/kills/<?=date_format(date_create('now'),'d-m-Y')?>">Aujourd'hui</a><br><br>
            <a href="/aeroclub/index.php">Planche</a>
        </div>
    <table class="table-logbook">
        <tr>
            <th>Message</th>
            <th>Lien</th>
        </tr>
<?php
while ($data = $rep->fetch())
{
    ?>
    <tr>
        <td><?= $data['message']?></td>
        <td><a href='/aeroclub/index.php/kills/<?=$data['id']?>'><p style='color:green;'>#</p></a></td>
    </tr>
    <?php
}
$rep->closeCursor();
?>
    </table>
    </body>
</html>