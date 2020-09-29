<?php
	session_start();

	$_SESSION["fees"]=$_POST["fees"];
	
$conn=new mysqli('localhost','root','','hospitalmanagement');

if($conn->connect_error)
{
	die('connection failed:'.$conn->connect_error);
}
else
{
	$stmt=$conn->prepare("INSERT INTO appointment(doctor,date,timeslot,contact,address,disease,fees,patient) 
						VALUES(?,?,?,?,?,?,?,?)");
	$stmt->bind_param("ssssssis",$_SESSION["doctor"],$_SESSION["date"],$_SESSION["timeslot"],$_SESSION["contact"],
								$_SESSION["address"],$_SESSION["disease"],$_SESSION["fees"],$_SESSION["email"]);
	$stmt->execute();
	echo '<script> window.location="receipt.php"; </script>';
	$stmt->close();
	$conn->close();
}


?>