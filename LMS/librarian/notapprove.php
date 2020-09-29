<?php 
	include 'inc/connection.php';
	$id= $_GET["id"];
	mysqli_query($link, "update std_registration set status='no' where id=$id");
	mysqli_query($link, "update t_registration set status='no' where id=$id");
 ?>
 <script type="text/javascript">
 	window.location="status.php";
 </script>
