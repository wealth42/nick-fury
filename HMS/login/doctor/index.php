<?php
session_start();
include("include/config.php");
error_reporting(0);
if(isset($_POST['submit']))
{
$ret=mysqli_query($con,"SELECT * FROM doctorsignup  WHERE email='".$_POST['username']."' and password='".md5($_POST['password'])."'");

$num=mysqli_fetch_array($ret);
if($num>0)
{
$extra="dashboard.php";
$_SESSION['dlogin']=$_POST['username'];
$_SESSION['id']=$num['id'];
$uip=$_SERVER['REMOTE_ADDR'];
$status=1;
$host=$_SERVER['HTTP_HOST'];
$uri=rtrim(dirname($_SERVER['PHP_SELF']),'/\\');
header("location:http://$host$uri/$extra");
exit();
}
else
{
$host  = $_SERVER['HTTP_HOST'];
$_SESSION['dlogin']=$_POST['username'];
$uip=$_SERVER['REMOTE_ADDR'];
$status=0;
$_SESSION['errmsg']="Invalid username or password";
$extra="index.php";
$uri  = rtrim(dirname($_SERVER['PHP_SELF']),'/\\');
header("location:http://$host$uri/$extra");
exit();
}
}
?>


<!DOCTYPE html>
<html lang="en">
	<head>
		<title>Doctor Login</title>
		

		<link rel="stylesheet" href="vendor/bootstrap/css/bootstrap.min.css">
		<link rel="stylesheet" href="vendor/fontawesome/css/font-awesome.min.css">
		<link rel="stylesheet" href="vendor/themify-icons/themify-icons.min.css">
		<link rel="stylesheet" href="assets/css/styles.css">
		<link rel="stylesheet" href="assets/css/plugins.css">
		<link rel="stylesheet" href="assets/css/themes/theme-1.css" id="skin_color" />

	</head>

	<body class="login">
		<div class="row">
			<div class="main-login col-xs-10 col-xs-offset-1 col-sm-8 col-sm-offset-2 col-md-4 col-md-offset-4">
				<div class="logo margin-top-30">
				<a href="../../index.php">	
				<h2 style="text-align: center;color: blue;font-family:Numans;">Doctor Login</h2>
				</a></div>

				<div class="box-login">
					<form class="form-login" method="post">
						<fieldset>
							<legend style="font-family:Numans;">Sign in to your account</legend>

							<p style="color:blue">Please enter your name and password to log in.<br />
								
		<span style="color:red;"><?php echo $_SESSION['errmsg']; ?><?php echo $_SESSION['errmsg']="";?></span>
							</p>
	
							<div class="form-group">
							<span class="input-icon">
				<input type="text" class="form-control" name="username" placeholder="Username">
				<i class="fa fa-user"></i> </span>
							</div>
				
							<div class="form-group form-actions">
								<span class="input-icon">
						<input type="password" class="form-control password" name="password" placeholder="Password">
									<i class="fa fa-lock"></i>
						
									 </span>
							</div>
						
							<div class="form-actions">
<button type="submit" class="btn btn-primary pull-right" name="submit">Login <i class="fa fa-arrow-circle-right"></i>
								</button>
<input type="button" class="btn btn-primary pull-left" value="Go Back!" onclick="location.href = '../../index.php';" /></div>
					
<br><br>
<p style="color:#28288a;float:center;text-align:center;">New To Doctor Login ?</p>
<button class="but2"><a href="../../Signup/doctorsignup/signupdoctor.php">Signup Here !</button></a>
		
						</fieldset>					
					

					</form>
			
				</div>

			</div>
		</div>

<script src="vendor/jquery/jquery.min.js"></script>
		<script src="vendor/bootstrap/js/bootstrap.min.js"></script>
		<script src="vendor/jquery-cookie/jquery.cookie.js"></script>	
		<script src="assets/js/main.js"></script>
		<script src="assets/js/form-elements.js"></script>
		<script src="assets/js/login.js"></script>
		<script>
			jQuery(document).ready(function() {
				Main.init();
				Login.init();
			});
		</script>
	
	</body>
</html>