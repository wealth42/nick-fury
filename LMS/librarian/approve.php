<?php
    session_start();
    if (!isset($_SESSION["username"])) {
    ?>
        <script type="text/javascript">
            window.location="login.php";
        </script>
    <?php
    }

	include 'inc/connection.php';
	$id= $_GET["id"];
	mysqli_query($link, "update std_registration set status='yes' where id=$id");
    mysqli_query($link, "update t_registration set status='yes' where id=$id");
 ?>

 <script type="text/javascript">
 	window.location="status.php";
 </script>


 