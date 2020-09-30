<?php
	session_start();
?>
<html>
<head>
	<link rel="stylesheet" href="patient-booking.css">
	<title> Receipt </title>
</head>
<body>
	<?php
	if(isset($_SESSION["username"]))
	{
		?>
		<div class="container">
			<h2>Receipt</h2>
			<br>
			<hr>
			<br>
			<form action="dashboard.php">
				<div class="row">
					<div class="col-25">Patient : </div>
					<div class="col-75">
					<?php echo $_SESSION["username"]; ?>
					</div>
				</div>
				<br>
				<div class="row">
					<div class="col-25">Doctor :</div>
					<div class="col-75">
					<?php echo $_SESSION["doctor"]; ?>
					</div>
				</div>
				<br>
				<div class="row">
					<div class="col-25">Date : </div>
					<div class="col-75">
					<?php echo $_SESSION["date"]; ?>
					</div>
				</div>
				<br>
				<div class="row">
					<div class="col-25">Timeslot : </div>
					<div class="col-75">
					<?php echo $_SESSION["timeslot"]; ?>
					</div>
				</div>
				<br>
				<div class="row">
					<div class="col-25">Contact : </div>
					<div class="col-75">
					<?php echo $_SESSION["contact"]; ?>
					</div>
				</div>
				<br>
				<div class="row">
					<div class="col-25">Address : </div>
					<div class="col-75">
					<?php echo $_SESSION["address"]; ?>
					</div>
				</div>
				<br>
				<div class="row">
					<div class="col-25">Disease	: </div>
					<div class="col-75">
					<?php echo $_SESSION["disease"]; ?>
					</div>
				</div>
				<br>
				<div class="row">
					<div class="col-25">
						<button class="button" >Print Receipt</button>
					</div>
				</div>
  
			</form>
		</div>
		<?php
	}
	else{
		echo "<script>location.href='index.php'</script>";
	}
	?>

</body>
</html>