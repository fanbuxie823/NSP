<?php
error_reporting (E_ALL & ~E_NOTICE);
include_once("class/pData.class.php");
include_once("class/pDraw.class.php");
include_once("class/pImage.class.php");
ini_set('date.timezone','Asia/Seoul');

if(!file_exists('pic/temp_24hours.png'))
    {
      $myData = new pData();
     $sql =<<<EOF
     SELECT * FROM DATA_24HOURS ORDER BY ID ASC;
EOF;

   $ret = $db->query($sql);
   while($row = $ret->fetchArray(SQLITE3_ASSOC))
     {
       $time=round($row['ID']/7200)*7200;
       $time_t24[]=date("H:00",$time);
       $temp24[] = $row['TEMP'];
     }
   $myData->addPoints($time_t24,"Timestamp");#添加坐标信息
   $myData->setAbscissa("Timestamp");

   $myData->addPoints($temp24,"Data");#添加数据
   $myData->setSerieDescription("Serie1","Temperature");#数据描述
   $myData->setSerieOnAxis("Serie1",0);

   $myData->setAxisPosition(0,AXIS_POSITION_LEFT);
   $myData->setAxisName(0,"Temperature");#设置坐标轴信息
   $myData->setAxisUnit(0,"℃");

   $myPicture = new pImage(900,300,$myData,TRUE);

   $myPicture->setShadow(TRUE,array("X"=>1,"Y"=>1,"R"=>50,"G"=>50,"B"=>50,"Alpha"=>20));

   $myPicture->setFontProperties(array("FontName"=>"fonts/Forgotte.ttf","FontSize"=>14));
   $TextSettings = array("Align"=>TEXT_ALIGN_MIDDLEMIDDLE
   , "R"=>28, "G"=>28, "B"=>28);
   $myPicture->drawText(450,25,"temperature",$TextSettings);

   $myPicture->setShadow(FALSE);
   $myPicture->setGraphArea(50,50,875,260);
   $myPicture->setFontProperties(array("R"=>0,"G"=>0,"B"=>0,"FontName"=>"fonts/pf_arma_five.ttf","FontSize"=>6));

   $Settings = array("Pos"=>SCALE_POS_LEFTRIGHT
   , "Mode"=>SCALE_MODE_FLOATING
   , "LabelingMethod"=>LABELING_DIFFERENT
   , "GridR"=>255, "GridG"=>255, "GridB"=>255, "GridAlpha"=>50, "TickR"=>0, "TickG"=>0, "TickB"=>0, "TickAlpha"=>50, "LabelRotation"=>0, "LabelSkip"=>1, "CycleBackground"=>1, "DrawXLines"=>1, "DrawSubTicks"=>1, "SubTickR"=>255, "SubTickG"=>0, "SubTickB"=>0, "SubTickAlpha"=>50, "DrawYLines"=>ALL);
   $myPicture->drawScale($Settings);

   $myPicture->setShadow(TRUE,array("X"=>1,"Y"=>1,"R"=>50,"G"=>50,"B"=>50,"Alpha"=>10));

   $Config = "";
   $myPicture->drawSplineChart($Config);

   $myPicture->render("pic/temp_24hours.png");
}
?>
