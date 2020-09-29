<?php 
     session_start();
    if (!isset($_SESSION["student"])) {
        ?>
            <script type="text/javascript">
                window.location="login.php";
            </script>
        <?php
    }
    include 'inc/header.php';
    include 'inc/connection.php';
 ?>
 <html>
	<head>
     <!-- Important Script Files -->
	<script src="inc/js/jquery-2.2.4.min.js"></script>
	<script src="inc/js/custom.js"></script>
	</head>
	<body>
		<!--dashboard area-->
		<div class="dashboard-content">
			<div class="dashboard-header">
				<div class="container">
					<div class="row">
						<div class="right">	
						<a href="dashboard.php">home</a>
						</div>
						
						<div class="right">
						<a href="profile.php">Profile</a>
						</div>
						
						<div class="right">
						<a href="logout.php">logout</a>
						</div>
					</div>
					<div class="row">
						<div class="col-md-12">
							<form action="" class="pass-content" method="post">
							
								<b>Current Password:</b>
								<input type="password" class="form-control mt-10" name="cpassword" placeholder="Current password">
								<br>
								<b>New Password:</b>
								<input type="password" class="form-control mt-10" name="npassword" placeholder="New password">
								<br>
								<b>Confirm Password:</b>
								<input type="password" class="form-control mt-10" name="conpass" placeholder="Confirm password">
								<br>
								<input type="submit" name="submit" class="btn" value="Change Password">
							</form>
							<?php
								if (isset($_POST["submit"])){
								
									$cpass    = $_POST['cpassword'];
									$npass    = $_POST['npassword'];
									$conpass  = $_POST['conpass'];
									$res = mysqli_query($link, "select password from std_registration where username='$_SESSION[student]'");								
									while($row = mysqli_fetch_array($res)){
										$pass   = $row['password'];
									}
									if($cpass != $pass){
										?>
											<div class="alert alert-warning">
												<strong style="color:#333"> Your Current password is Incorrect ! </strong>
											</div>
										<?php
									}else{
										if($npass == $conpass){
										mysqli_query($link, "update std_registration set password='$npass' where username='$_SESSION[student]'");
										
										?>
											<div class="alert alert-success">
												<strong style="color:#333"> Your Password is changed ! </strong>
											</div>
										<?php
										}else{
										?>
											<div class="alert alert-warning">
												<strong style="color:#333"> Your Password did not match ! </strong>
											</div>
										<?php
										}			
									}								
								}
							?>
	
						</div>
					</div>
				</div>					
			</div>
		</div>
	</body>
</html>