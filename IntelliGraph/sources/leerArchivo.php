<?php
$archivo=$_GET['archivo'];
#$hola=$_POST['hola'];
var_dump($archivo);
echo $archivo;
$linea = 0;
//Abrimos nuestro archivo
$archivo = fopen($archivo, "r");
//Lo recorremos
while (($datos = fgetcsv($archivo, ",")) == true) 
{
  $num = count($datos);
  $linea++;
  //Recorremos las columnas de esa linea
  for ($columna = 0; $columna < $num; $columna++) 
      {
         $hola = $datos[$columna].'  ';
        //echo str_replace(",","  ",$hola);
        echo $hola;
     }
}
//Cerramos el archivo
fclose($archivo);
?>