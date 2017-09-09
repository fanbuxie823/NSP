<?php

ini_set('date.timezone','Asia/Seoul');

$myfile = fopen("cache.txt", "r") or die("Unable to open file!");

$temperature= str_replace(PHP_EOL,'',fgets($myfile));

$humidity=str_replace(PHP_EOL,'',fgets($myfile));

$time=str_replace(PHP_EOL,'',fgets($myfile));
$date=date("H:i:s",$time);

$feel=round(1.04*$temperature+0.2*$humidity/100*6.105*exp((17.27*$temperature)/(237.7+$temperature))-2.7);

echo "Temperature: ".$temperature."℃ <br>"."Humidity: ".$humidity."% <br>"."Feel like: ".$feel."℃ <br>".
									"Last refresh time: ".$date;
?>
