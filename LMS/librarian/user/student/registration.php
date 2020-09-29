<?php 
    include 'inc/connection.php';
    include 'inc/function.php';
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
          <!--  background-image: url(inc/img/3.jpg); -->
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
                <h4 style="text-align: center; margin-bottom: 25px;">Student registration form</h4>
				
				<form action="" class="form-inline" method="post">
				
					 <div class="form-group">
					 	<label for="name" class="text-right">Name </label>
                        <input type="text" class="form-control custom" placeholder="Your Name" name="name" required />
                    </div>
                    <div class="form-group">
                    	 <label for="username">Username </label>
                        <input type="text" class="form-control custom" placeholder="Username" name="username" required />
                    </div>
                     <?php if(isset($error_ua)):?> 
                     <span class="error"> <?php echo $error_ua; ?></span>
                      <?php endif ?>
                      <?php if(isset($error_uname)):?> 
                     <span class="error"> <?php echo $error_uname; ?></span>
                      <?php endif ?>
                    <div class="form-group">
                    	 <label for="password">Password </label>
                        <input type="password" class="form-control custom" placeholder="Password" name="password" required />
                    </div>
					<?php if(isset($error_pw)):?> 
                     <span class="error"> <?php echo $error_pw; ?></span>
                      <?php endif ?>
                    <div class="form-group">
                    	 <label for="email">Email </label>
                        <input type="text" class="form-control custom" placeholder="Gmail" name="email" required />
                    </div>
                    <?php if(isset($e_msg)):?> 
                    <span class="error"><?php echo $e_msg; ?> </span>
                    <?php endif ?>
                    <?php if(isset($error_email)):?> 
                    <span class="error"><?php echo $error_email; ?> </span>
                    <?php endif ?>
                    <div class="form-group">
                    	 <label for="phone">Phone No</label>
                        <input type="text" class="form-control custom" placeholder="Phone No" name="phone" required />
                    </div>
                    <?php if(isset($error_phone)):?> 
                    <span class="error"><?php echo $error_phone; ?></span>
                      <?php endif ?>
                    <div class="form-group">
					    <label for="sem">Select Semester </label>
					    <select class="form-control custom" name="sem" required >
							<option>1th</option>
							<option>2nd</option>
							<option>3rd</option>
							<option>4th</option>
							<option>5th</option>
							<option>6th</option>
					    </select>
					</div>
                    <div class="form-group">
					    <label for="dept">Course </label>
					    <select class="form-control custom" name="dept" required >
							<option>B.Com</option>
							<option>BCA</option>
							<option>BSc.IT</option>
							<option>BMS</option>
							<option>BTM</option>
							<option>Other</option>
					    </select>
					</div>
                    <div class="form-group">
                    	 <label for="regno">Registration No </label>
                        <input type="text" class="form-control custom" placeholder="Registration No" name="regno" required />
                    </div>
                    <?php if(isset($error_reg)):?> 
                    <span class="error"><?php echo $error_reg; ?></span>
                      <?php endif ?>
                    <div class="form-group">
                    	 <label for="address">Address </label>
                        <textarea name="address" id="address"  class="form-control custom" placeholder="Your address" required ></textarea>
                    </div>
                    <div class="submit">
                    	<input type="submit" value="Register" name="submit" class="btn btn-danger">
						<a href="../" class="btn btn-warning"> Back to home page </a>
                    </div>
				</form>
			</div>
		</div>
	</div>
	
</body>
</html>