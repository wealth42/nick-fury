<?php
session_start();
	$_SESSION["doctor"]=$_POST["doctor"];
	$_SESSION["date"]=$_POST["date"];
	$_SESSION["timeslot"]=$_POST["timeslot"];
	$_SESSION["contact"]=$_POST["contact"];
	$_SESSION["address"]=$_POST["address"];
	$_SESSION["disease"]=$_POST["disease"];
?>
<html>
<head>
	<link rel="stylesheet" href="patient-booking.css">
	<title> Payment </title>
</head>
<body>
		<div class="container">
			<form action="data2.php" method="POST">
				<h2> Make Payment</h2>
				<br>
					<hr>
				<br>
				<div class="row">
					<img src="payment.png"/>
					<br>
					<br>
				</div>
				<div class="row">
					<div class="col-25">
						Card Holder :
					</div>
					<div class="col-75">
						<input type="text" name="holder" placeholder="Enter Card-holder name" required>
					</div>
				</div>
				<br>
				<div class="row">
					<div class="col-25">
						Card.No :
					</div>
					<div class="col-75">
						<input type="tel" name="card" required>
					</div>
				</div>
				<br>
				<div class="row">
					<div class="col-25">
						Card Type :
					</div>
					<div class="col-75">
						<input list="Card-type" name="type" placeholder="Your Card-type" required>
						<datalist id="Card-type">
							<option>Paypal</option>
							<option>Discover</option>
							<option>Visa</option>
							<option>Mastercard</option>
							<option>American Express</option>
						</datalist>
					</div>
				</div>
				<br>
				<div class="row">
					<div class="col-25">
						Card Expiry :
					</div>
					<div class="col-35">
						<input type="number" min="1" max="12" name="expiry" placeholder="Month" required>
					</div>
					<div class="col-45">
						<input type="number" min="2020" max="2050" name="expiry" placeholder="Year" required>
					</div>
				</div>
				<br>
				<div class="row">
					<div class="col-25">
						Amount  :
					</div>
					<div class="col-75">
						<input type="number" name="fees" min="100.00" max="10000.00" placeholder="Amount in Rupees" required>
					</div>
					
				</div>
				<br>
				<br>
				<div class="row">
					<div class="col-25">
						<button class="button">Make Payment </button>
					</div>
				</div>
				
			</form>
		</div>
</body>
</html>