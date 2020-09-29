<?php 
    include 'inc/connection.php';
    include 'inc/function.php';
 ?>
<!DOCTYPE html>
<html>
<head>
    <title>Library Management System</title>
    <link rel="stylesheet" href="inc/css/bootstrap.min.css">
    <link rel="stylesheet" href="inc/css/pro1.css">
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
                 
                <h4 style="text-align: center; margin-bottom: 25px;">Teacher registration form</h4>
                <form action="" class="form-inline" method="post">
					<?php if(isset($s_msg)):?>
						<span class="success"> <?php echo $s_msg; ?></span>
					<?php endif ?>
                    <div class="form-group">
                        <label for="name" class="text-right">Name </label>
                        <input type="text" class="form-control custom" placeholder="Full Name" name="name" required />
                    </div>
                    <div class="form-group">
                         <label for="username">Username </label>
                        <input type="text" class="form-control custom" placeholder="Username" name="username" required  />
                    </div>
                    <?php if(isset($error_ua)):?> 
                     <span class="error"> <?php echo $error_ua; ?></span>
                      <?php endif ?>
                      <?php if(isset($error_uname)):?> 
                     <span class="error"> <?php echo $error_uname; ?></span>
                      <?php endif ?>
                    <div class="form-group">
                         <label for="password">Password </label>
                        <input type="password" class="form-control custom" placeholder="Password" name="password" required  />
                    </div>
					<?php if(isset($error_pw)):?> 
                     <span class="error"> <?php echo $error_pw; ?></span>
                      <?php endif ?>
                    <div class="form-group">
                         <label for="lecturer">Lecturer </label>
                        <input type="text" class="form-control custom" placeholder="lecturer / dept" name="lecturer" required  />
                    </div>
                    <div class="form-group">
                         <label for="email">Email </label>
                        <input type="text" class="form-control custom" placeholder="Gmail" name="email"/ required >
                    </div>
                     <?php if(isset($e_msg)):?> 
                    <span class="error"><?php echo $e_msg; ?> </span>
                    <?php endif ?>
                    <?php if(isset($error_email)):?> 
                    <span class="error"><?php echo $error_email; ?> </span>
                    <?php endif ?>
                    <div class="form-group">
                         <label for="phone">Phone No </label>
                        <input type="text" class="form-control custom" placeholder="Phone No" name="phone" required  />
                    </div>
                     <?php if(isset($error_phone)):?> 
                    <span class="error"><?php echo $error_phone; ?></span>
                      <?php endif ?>
                    <div class="form-group">
                         <label for="session">Id No </label>
                        <input type="text" class="form-control custom" placeholder="Id No" name="idno" required  />
                    </div>
                     <?php if(isset($error_id)):?> 
                    <span class="error"><?php echo $error_id; ?></span>
                      <?php endif ?>
                    <div class="form-group">
                         <label for="address">Address </label>
                        <textarea name="address" id="address"  class="form-control custom" placeholder="Your address" required  ></textarea>
                    </div>
                    <div class=" submit mb-20">
                    	<input type="submit" value="Register" name="submit" class="btn btn-danger">
						<a href="../" class="btn btn-warning"> Back to home page </a>
                    </div>
                </form>
            </div>
        </div>
    </div>

</body>
</html>