<?php
    session_start();
    if (!isset($_SESSION["username"])) {
        ?>
            <script type="text/javascript">
                window.location="login.php";
            </script>
        <?php
    }
    include 'inc/header.php';
    include 'inc/connection.php';
	include 'inc/tfunction.php';
 ?>
<html>
<head>
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
							<a href="dashboard.php">Home</a>
						</div>
						
						<div class="right">
						<a href="profile.php">Profile</a>
						</div>
						
						<div class="right">
						<a href="logout.php">logout</a>
						</div>
				</div>

				<div class="addUser">
					<div class="gap-40"></div>
					<div class="reg-body user-content">
                        <?php if(isset($error_m)):?>
                            <span class="errort"> <?php echo $error_m; ?></span>
                        <?php endif ?>
                        <h4 style="text-align: center; margin-bottom: 25px;">ADD TEACHER </h4>
                        <form action="" class="form-inline" method="post">
                            <div class="form-group">
                                <label for="name" class="text-right">Name </label>
                                <input type="text" class="form-control custom" placeholder="Name" name="name" required />
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
                                <input type="password" class="form-control custom" placeholder="Password" name="password" required/>
                            </div>
                            <div class="form-group">
                                <label for="lecturer">Lecturer </label>
                                <input type="text" class="form-control custom" placeholder="lecturer / dept" name="lecturer" required />
                            </div>
                            <div class="form-group">
                                <label for="email">Email </label>
                                <input type="text" class="form-control custom" placeholder="Email" name="email" required />
                            </div>
                            <?php if(isset($e_msg)):?>
                                <span class="error"><?php echo $e_msg; ?> </span>
                            <?php endif ?>
                            <?php if(isset($error_email)):?>
                                <span class="error"><?php echo $error_email; ?> </span>
                            <?php endif ?>
                            <div class="form-group">
                                <label for="phone">Phone No </label>
                                <input type="text" class="form-control custom" placeholder="Phone No" name="phone" required />
                            </div>
                            <?php if(isset($error_phone)):?>
                                <span class="error"><?php echo $error_phone; ?></span>
                            <?php endif ?>
                            <div class="form-group">
                                <label for="session">Id No </label>
                                <input type="text" class="form-control custom" placeholder="Id No" name="idno" required />
                            </div>
                            <?php if(isset($error_id)):?>
                                <span class="error"><?php echo $error_id; ?></span>
                            <?php endif ?>
                            <div class="form-group">
                                <label for="address">Address </label>
                                <textarea name="address" id="address"  class="form-control custom" placeholder="Your address" required ></textarea>
                            </div>
                            <div class="submit">
                                <input type="submit" value="Register" class="btn change" name="submit">
                            </div>
                        </form>
					</div>
				</div>
			</div>					
		</div>
	</div>
</body>
</html>
