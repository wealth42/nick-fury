<?php 
    session_start();
    include 'inc/connection.php';
 ?>
<!DOCTYPE html>
<html>
<head>
	
	<title>Library Management System</title>
	<!-- Main css file -->
	<link rel="stylesheet" href="inc/css/bootstrap.min.css">
	<link rel="stylesheet" href="inc/css/pro1.css">
	
	<!-- For Fonts -->
	<link href="https://fonts.googleapis.com/css?family=Montserrat:400,500,600" rel="stylesheet">
    <style>
        .login{
           <!-- background-image: url(inc/img/3.jpg); -->
            margin-bottom: 30px;
            padding: 50px;
            padding-bottom: 70px;
        }
        .reg-header h2{
            color: #000000;
            z-index: 999999;
        }
        .login-body h4{
            margin-bottom: 20px;
        }
    </style>
</head>
<body>
	<div class="login registration">
		<div class="wrapper">
			<div class="reg-header text-center">
				<h2>Library management system</h2>
                <div class="gap-40"></div>
			</div>
			<div class="gap-30"></div>
			<div class="login-content">
				<div class="login-body">
                    <h4>Student's Login Form</h4>
					<form action="" method="post">
						<div class="mb-20">
							<input type="text" name="username" class="form-control" placeholder="Username" required />
						</div>
						<div class="mb-20">
							<input type="password" name="password" class="form-control" placeholder="Password" required />
						</div>
						<div class="mb-20">
							<input class="btn btn-danger submit" type="submit" name="login" value="Login">
							<a class="btn btn-warning" href="../"> Back to home page </a>
						</div>
					</form>
				</div>
				<div class="login-footer text-center">
					<div class="separator">
		                <p class="change_link">New to the site?
		                    <a href="registration.php" class="text-right"> Create Account </a>
		                </p>
	                </div>
				</div>
                <?php 
                    if (isset($_POST["login"])) {
                        $count=0;
						$password=$_POST["password"];
                        $res= mysqli_query($link, "select * from std_registration where username='$_POST[username]' && password= '".md5($password)."'");
						$rej= mysqli_query($link, "select * from std_registration where username='$_POST[username]' && password= '".md5($password)."' && status= 'yes'");
                        $count = mysqli_num_rows($res);
                        $countrej = mysqli_num_rows($rej);
                        if ($count==0) {
                            ?>
                                <div class="alert alert-warning">
									<strong style="color:#333">Invalid !</strong> <span style="color: red;font-weight: bold; ">Username Or Password.</span>
                                </div>
                            <?php
                        }
                        else{
                            if ($countrej==1) {
								$_SESSION["student"] = $_POST["username"];
								?>
								<script type="text/javascript">
									window.location="dashboard.php";
								</script>
								<?php
							}
							else{
								?>
							  <div class="alert alert-warning">
								 <span style="color: red;font-weight: bold; ">Sorry ! Your permission is not yet accepted by Librarian</span>
                               </div><?php
							}							
                        }
                    }
                 ?>
			</div>
		</div>
	</div>

</body>
</html>