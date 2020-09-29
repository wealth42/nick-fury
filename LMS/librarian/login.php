<?php 
    session_start();
    include 'inc/connection.php';
 ?>
<!DOCTYPE html>
<html>
<head>
	<title>Library Management System</title>
	
	<!-- Main CSS File -->
	<link rel="stylesheet" href="inc/css/bootstrap.min.css">
	<link rel="stylesheet" href="inc/css/pro1.css">
	
	<!-- For Fonts -->
	<link href="https://fonts.googleapis.com/css?family=Montserrat:400,500,600" rel="stylesheet">
    <style>
        .login{
            <!-- background-image: url(inc/img/3.jpg);-->
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
				<div class="gap-30"></div>
                <div class="gap-30"></div>
			</div>
			<div class="gap-30"></div>
			<div class="login-content">
				<div class="login-body">
                    <h4>Librarian Login Form</h4>
					<form action="" method="post">
						<div class="mb-20">
							<input type="text" name="username" class="form-control" placeholder="Username" required />
						</div>
						<div class="mb-20">
							<input type="password" name="password" class="form-control" placeholder="Password" required />
						</div>
						<div class="mb-20">
							<input class="btn btn-danger submit" type="submit" name="login" value="Login">
                            <a href="user/index.php" class="btn btn-warning"> Back to home page </a>
						</div>
					</form>
				</div>
                 <?php 
                    if (isset($_POST["login"])) {
                        $count=0;
                        $res= mysqli_query($link, "select * from lib_registration where username='$_POST[username]' && password= '$_POST[password]' ");
                        $count = mysqli_num_rows($res);
                        if ($count==0) {
                            ?>
                                <div class="alert alert-warning">
                                    <strong style="color:#333">Invalid!</strong> <span style="color: red;font-weight: bold; ">Username Or Password.</span>
                                </div>
                            <?php
                        }
                        else{
                            $_SESSION["username"] = $_POST["username"];
                            ?>
                            <script type="text/javascript">
                                window.location="dashboard.php";
                            </script>
                            <?php  
                        }
                    }
                 ?>
			</div>
		</div>
	</div>
	<script src="inc/js/jquery-2.2.4.min.js"></script>
	<script src="inc/js/bootstrap.min.js"></script>
	<script src="inc/js/custom.js"></script>
</body>
</html>