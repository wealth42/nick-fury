<?php 
	session_start();
	unset($_SESSION["username"]);

 ?>
 <script type="text/javascript">
 	window.location="login.php";
 </script>