
<!DOCTYPE html>
<html>

<meta http-equiv="refresh" content="10">

<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>CSL</title>
<link rel="stylesheet" href="CSL.css">

<?php include_once ("pic.php");?>
<?php ini_set('date.timezone','Asia/Seoul');?>

<body>

	<div>
		<div class="title">
			<h1>
				<?php include_once ("realtime.php");?>
			</h1>
		</div>

		<hr>

		<div class="title">
		<h3>temperature and humidity in last 2 hours</h3>
		</div>

		<div class="pic">
			<img title="" alt="temp_2hours" src="pic/temp_2hours.png">
			<br>
			<img title="" alt="hum_2hours" src="pic/hum_2hours.png">
		</div>

		<div class="title">
		<h3>temperature and humidity in last 24 hours</h3>
		</div>

		<div class="pic">
			<img title="" alt="temp_2hours" src="pic/temp_24hours.png">
			<br>
			<img title="" alt="hum_2hours" src="pic/hum_24hours.png">
		<div>

 	</div>
</body>
</html>
