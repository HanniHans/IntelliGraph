<?php


echo '36525';
date_default_timezone_set('America/mexico_city');
//$ho= $h-$h1;
echo '<br>';
//echo $ho;
$date1 = new DateTime("2001-01-01");
$date2 = new DateTime("2100-12-31");
$diff = $date1->diff($date2);
// will output 2 days

echo 'Total de días en el siglo 21: ';
$diasiglo =$diff->days;
echo $diasiglo . ' days '.'<br>';

$date3 = new DateTime("2019-11-03");
$diff3=$date2->diff($date3);
//echo $diff3;
//$dias1 =$date2->diff($date3)/100;
//echo $dias1.'h';


//$c2=(int) $dias1;
//$c1=settype($dias1, "string");
//echo $c2 . ' days ';

//$dife1= (int)$dias1-(int)$diff;
//$dife1= $diff->diff($diff3);
//echo $dife1;
$date1 = strtotime('2001-01-01 18:00:00');
$date2 = strtotime('2100-12-31 18:00:00');
$subTime = $date2 - $date1;
$y = ($subTime/(60*60*24*365));
$d = ($subTime/(60*60*24))%365;
$h = ($subTime/(60*60))%24;
$m = ($subTime/60)%60;

echo '<br>'."Difference between ".date('Y-m-d H:i:s',$date1)." and ".date('Y-m-d H:i:s',$date2)." is:\n".$d;

?>