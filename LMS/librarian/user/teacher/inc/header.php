<?php
    include 'inc/connection.php';
    $not=0;
    $res = mysqli_query($link,"select * from message where rusername='$_SESSION[teacher]' && read1='n'");
    $not= mysqli_num_rows($res);
 ?>
<!DOCTYPE html>
<html>
<head>
	<title>Library Management System</title>
	<!-- Main CSS files -->
	<link rel="stylesheet" href="inc/css/bootstrap.min.css">
	<link rel="stylesheet" href="inc/css/pro1.css">
	<!-- For Icons -->
	<link rel="stylesheet" href="inc/css/fontawesome-all.min.css">
	<!-- For Fonts -->
	<link href="https://fonts.googleapis.com/css?family=Montserrat:400,500,600" rel="stylesheet">
	
</head>
<body>
	<div class="main-content">
		<div class="wrapper">
			<div class="left-sidebar">
				<div class="p-title">
					<h3><a href="dashboard.php"><i class="fas fa-book"></i><span>PROJECT NAME</span></a></h3>
				</div>
				<div class="gap-40"></div>
				<div class="profile">
					<div class="profile-pic">
						<?php
                            $res = mysqli_query($link, "select * from t_registration where username='".$_SESSION['teacher']."'");
                            while ($row = mysqli_fetch_array($res)){
                                ?><img src="<?php echo $row["photo"]; ?> " height="" width="" alt="something wrong" class="rounded-circle"></a> <?php
                            }
                        ?>
					</div>
					<div class="profile-info text-center">
						<span>Welcome !</span>
						<h2><?php echo $_SESSION["teacher"]; ?></h2>
					</div>
				</div>
				<div class="gap-30"></div>
				<div class="sidebar-menu">
					
	                <ul>
						<li class="menu <?php if($page=='dashboard'){ echo 'active';} ?>">
      						<a href="dashboard.php"><i class="fas fa-home"></i>Dashboard</a>
    					</li>
                        <li class="menu menu-toggle1">
      						<a><i class="fas fa-id-card"></i>My profile <span class="fa fa-chevron-down"></span></a>
                            <ul class="menus1">
                                <li><a href="changepass.php">change password</a></li>
                                <li><a href="profile.php">profile</a></li>
                            </ul>
	   					</li>
    					<li class="menu <?php if($page=='ibook'){ echo 'active';} ?>">
      						<a href="my-issued-books.php"><i class="fas fa-book"></i>my issued books</a>
    					</li>
    					<li class="menu <?php if($page=='books'){ echo 'active';} ?>">
      						<a href="books.php"><i class="fas fa-book"></i>books</a>
    					</li>	       	                    
    					<li class="menu <?php if($page=='rbook'){ echo 'active';} ?>">
      						<a href="request-book.php"><i class="fas fa-book"></i>request book</a>
    					</li>	   
						<li class="menu <?php if($page=='notifications'){ echo 'active';} ?>">
      						<a href="notifications.php"><i class="fas fa-bell"></i>Notifications</a>
    					</li>							
    				</ul>
				</div>
			</div>
			<div class="content">
				<div class="inner">
					<div class="heading text-center">
						<h3>Library Management System</h3>
					</div>
					<div class="header-profile text-right">
						<ul>
							<li class="icon">
								<a href="notifications.php" ><i class="fas fa-bell"></i></a>
								<span class="count" onclick="window.location='notifications.php'"><b><?php echo $not; ?></b></span>

							</li>
							
						</ul>
					</div>															
				</div>
			
		