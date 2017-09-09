<?php
error_reporting (E_ALL & ~E_NOTICE);
include_once("class/pData.class.php");
include_once("class/pDraw.class.php");
include_once("class/pImage.class.php");
ini_set('date.timezone','Asia/Seoul');

if(!(file_exists('pic/temp_2hours.png') and file_exists('pic/hum_2hours.png')
      and file_exists('pic/temp_24hours.png') and file_exists('pic/hum_24hours.png')))
    {


      /* Connect to the SQLlie database */
      class MyDB extends SQLite3
      {
         function __construct()
         {
            $this->open('DATA.db');
         }
      }


      $db = new MyDB();
      if(!$db){
         echo $db->lastErrorMsg();
      }
      /*
      else {
         echo "Opened database successfully\n";
      }
      */
      include_once("temp_2hours.php");
      include_once("hum_2hours.php");
      include_once("temp_24hours.php");
      include_once("hum_24hours.php");
      $db->close();

  }

?>
