<?php
session_start();
?>
<html>
<head>
	<!-- BASIC CSS  -->
	<link rel="stylesheet" href="patient-booking.css">

	<title>Book Appointment</title>
</head>

<body>

	<script>
		$( function() {
			$( "#datepicker" ).datepicker();
		} );
	</script>
	<?php
	if(isset($_SESSION["username"]))
	{
		?>
		<div class="container">
			<h2> Book Appointment </h2>
			<br> <hr> <br>	
			<form action="payment.php" method="POST">
				<div class="row">
					<div class="col-25">
						Doctor :
					</div>
					<div class="col-75">
						<input list="Doctor" name="doctor" placeholder="Select your Doctor " required>
						<datalist id="Doctor">
							<option>Dr. Monaksh Shah</option>
							<option>Dr. Anjila Aneja</option>
							<option>Mr. Swaroop Gopal</option>
							<option>Mrs. Nina Patel</option>
							<option>Dr. Amit Shrivastava</option>
							<option>Mrs. Nareshi Trehan</option>
						</datalist>
					</div>
				</div>
				<br>
				<div class="row">
					<div class="col-25">
						Date :
					</div>
					<div class="col-75">
						<input type="date" name="date" required>
					</div>
				</div>
				<br>
				<div class="row">
					<div class="col-25">
						Timeslot :
					</div>
					<div class="col-75">
						<input list="Timeslot" name="timeslot" placeholder="Select your Timeslot " required>
						<datalist id="Timeslot">
							<option>9:00-10:00 a.m.</option>
							<option>10:00-11:00 a.m.</option>
							<option>11:00-12:00 a.m.</option>
							<option>1:00-2:00 p.m.</option>
							<option>2:00-3:00 p.m.</option>
							<option>3:00-4:00 p.m.</option>
							<option>5:00-6:00 p.m.</option>
							<option>6:00-7:00 p.m.</option>
							<option>7:00-8:00 p.m.</option>
							<option>8:00-9:00 p.m.</option>
						</datalist>
					</div>
				</div>
				<br>
				<div class="row">
					<div class="col-25">
						Contact.No :
					</div>
					<div class="col-75">
						<input type="tel" name="contact" required>
					</div>
				</div>
				<br>
				<div class="row">
					<div class="col-25">
						Address :
					</div>
					<div class="col-75">
						<textarea name="address" placeholder="Your Address..." style="height:70px" required></textarea>
					</div>
				</div>
				<br>
				<div class="row">
					<div class="col-25">
						Disease :
					</div>
					<div class="col-75">
						<textarea name="disease" style="height:50px" required></textarea>
					</div>
				</div>
				<br>
				<br>
				<div class="row">
					<div class="col-25">
						<button class="button">Book</button>
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