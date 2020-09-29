<?php 
	include 'inc/connection.php';
?>
<!DOCTYPE html>
<html>
<head>
    <title>Library Management System</title>
	
    <!-- Main CSS Files -->
	<link rel="stylesheet" href="inc/css/bootstrap.min.css">
    <link rel="stylesheet" href="inc/css/pro1.css">
	
	<!-- For Fonts -->
    <link href="https://fonts.googleapis.com/css?family=Montserrat:400,500,600" rel="stylesheet">
    <style>
        .registration{
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
    <div class="registration">
        <div class="reg-wrapper">
            <div class="reg-header text-center">
                <h2>Library management system</h2>
            </div>
            <div class="gap-40"></div>
            <div class="reg-body">
                <h4 style="text-align: center; margin-bottom: 25px;">Librarian registration form</h4>
                <form action="" class="form-inline" method="post">
                    <div class="form-group">
                        <label for="name" class="text-right">Name </label>
                        <input type="text" class="form-control custom" placeholder="Your Name" name="name" required />
                    </div>
					 
                    <div class="form-group">
                         <label for="username">Username </label>
                        <input type="text" class="form-control custom" placeholder="Username" name="username" required />
                    </div>
                    <div class="form-group">
                         <label for="password">Password </label>
                        <input type="password" class="form-control custom" placeholder="Password" name="password" required />
                    </div>
                    <div class="form-group">
                         <label for="email">Email </label>
                        <input type="text" class="form-control custom" placeholder="Email" name="email" required />
                    </div>
                    <div class="form-group">
                         <label for="phone">Phone No </label>
                        <input type="text" class="form-control custom" placeholder="Phone No" name="phone" required />
                    </div>
                    <div class="form-group">
                         <label for="address">Address </label>
                        <textarea name="address" id="address"  class="form-control custom" placeholder="Your address" required ></textarea>
                    </div>
                   <div class="submit">
                    	<input type="submit" value="Register" name="submit" class="btn btn-danger">
						<a href="user/index.php" class="btn btn-warning"> Back to home page </a>
                    </div>
                </form>
            </div>
			<?php 
                if (isset($_POST["submit"])) {
                    $photo = "upload/avatar.jpg";
                    mysqli_query($link, "insert into lib_registration values('','$_POST[name]','$_POST[username]','$_POST[password]','$_POST[email]','$_POST[phone]','$_POST[address]','$photo')");                  
                }
             ?>
        </div>
    </div>
    <script src="inc/js/jquery-2.2.4.min.js"></script>
    <script src="inc/js/bootstrap.min.js"></script>
    <script src="inc/js/custom.js"></script>
</body>
</html>