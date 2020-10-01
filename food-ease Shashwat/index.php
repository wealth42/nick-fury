<?php
	if(isset($_POST['submit'])){
		$name=$_POST['name'];
		$email=$_POST['email'];
		$phone=$_POST['phone'];
		$order=$_POST['order'];

		$to='xyz.123@mail.com'; // Receiver Email ID, Replace with your email ID
		$subject='Form Submission';
		$message="Hello, .$name."."\n"."We have received your order:".$order."\n". It will shortly be delivered to you"."\n"."Thank You.";
		$headers="From: ".$email;

		if(mail($to, $subject, $message, $headers)){
			echo "<h1>Order placed successfully! Thank you"." ".$name.", We will contact you shortly!</h1>";
		}
		else{
			echo "Something went wrong!";
		}
	}
?>