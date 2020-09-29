<?php
session_start();
include('include/config.php');
include('include/checklogin.php');
check_login();

?>
<!DOCTYPE html>
<html lang="en">
	<head>

		<title>Patient | Dashboard</title>
		<link href="http://fonts.googleapis.com/css?family=Lato:300,400,400italic,600,700|Raleway:300,400,500,600,700|Crete+Round:400italic" rel="stylesheet" type="text/css" />
		<link rel="stylesheet" href="vendor/bootstrap/css/bootstrap.min.css">
		<link rel="stylesheet" href="vendor/fontawesome/css/font-awesome.min.css">
		<link rel="stylesheet" href="vendor/themify-icons/themify-icons.min.css">
		<link rel="stylesheet" href="assets/css/styles.css">
		<link rel="stylesheet" href="assets/css/plugins.css">
		<link rel="stylesheet" href="assets/css/themes/theme-1.css" id="skin_color" />


	</head>
	<body>


<?php
	if(isset($_SESSION["username"]))
	{
		?>

	<div id="app">
		<div class="sidebar app-aside" id="sidebar">
				<div class="sidebar-container perfect-scrollbar">
					<nav>
					
						<div class="navbar-title">
							<span>Main Navigation</span>
						</div>
					
						<ul class="main-navigation-menu">
					
							<li>
								<a href="dashboard.php">
									<div class="item-content">
										<div class="item-media">
											<i class="ti-home"></i>
										</div>
										<div class="item-inner">
											<span class="title"> Dashboard </span>
										</div>
									</div>
								</a>
							</li>
							
											
							<li>
								<a href="patient-booking.php">
									<div class="item-content">
										<div class="item-media">
											<i class="ti-pencil-alt"></i>
										</div>
										<div class="item-inner">
											<span class="title">Book  Appointment </span>
										</div>
									</div>
								</a>
							</li>
					
							<li>
								<a href="appointment-history.php">
									<div class="item-content">
										<div class="item-media">
											<i class="ti-list"></i>
										</div>
										<div class="item-inner">
											<span class="title"> Appointment History </span>
										</div>
									</div>
								</a>
							</li>

						</ul>
						
					</nav>
					</div>
			</div>
<header class="navbar navbar-default navbar-static-top">
					<!-- start: NAVBAR HEADER -->
					<div class="navbar-header">

						<a href="#" class="sidebar-mobile-toggler pull-left hidden-md hidden-lg" class="btn btn-navbar sidebar-toggle" data-toggle-class="app-slide-off" data-toggle-target="#app" data-toggle-click-outside="#sidebar">
							<i class="ti-align-justify"></i>
						</a>

						<a class="navbar-brand" href="#">
							<h2 style="padding-top:20% ">HMS</h2>
						</a>
						
						<a href="#" class="sidebar-toggler pull-right visible-md visible-lg" data-toggle-class="
						app-sidebar-closed" data-toggle-target="#app">
							<i class="ti-align-justify"></i>
						</a>
						
						<a class="pull-right menu-toggler visible-xs-block" id="menu-toggler" data-toggle="collapse" href=".navbar-collapse">
							<span class="sr-only">Toggle navigation</span>
							<i class="ti-view-grid"></i>
						</a>
					</div>
					
					<div class="navbar-collapse collapse">
						<ul class="nav navbar-right">
					
								<li  style="padding-top:2% ">
								<h2>Hospital Management System</h2>
							</li>
						
						
							<li class="dropdown current-user">
								<a href class="dropdown-toggle" data-toggle="dropdown">
									<img src="assets/images/patient.png" > 
									<span class="username">
									<?php $query=mysqli_query($con,"select fullname from patientsignup where id='".$_SESSION['id']."'"); 
                               while($row=mysqli_fetch_array($query))
                             {
                                 	echo $row['fullname'];
                              }
									?> 
									<i class="ti-angle-down"></i></i></span></a>

								<ul class="dropdown-menu dropdown-dark">
									
									
									<li>
										<a href="change-password.php">
											Change Password
										</a>
									</li>
									
									<li>
										<a href="logout.php">
											Log Out
										</a>
									</li>
								</ul>
							</li>


								</ul>
					
						<div class="close-handle visible-xs-block menu-toggler" data-toggle="collapse" 
						href=".navbar-collapse">
							<div class="arrow-left"></div>
							<div class="arrow-right"></div>
						</div>
						
							</div>
				
						</header>

						<div class="main-content" >
					<div class="wrap-content container" id="container">

						<section id="page-title">
							<div class="row">
								<div class="col-sm-8">
					<h1 class="mainTitle">Patient | Dashboard</h1></div>				
							</div>
						</section>
							<div class="container-fluid container-fullw bg-white">
							<div class="row">
								<div class="col-sm-6">
									<div class="panel panel-white no-radius text-center">
										<div class="panel-body">
											<img src="assets/images/book.png" height="70" weight="100">
											<h2 class="StepTitle">Appointment</h2>
											
											<p class="links cl-effect-1">
												<a href="patient-booking.php">
													Book Appointment
												</a>
											</p>
										</div>
									</div>
								</div>
						
								<div class="col-sm-6">
									<div class="panel panel-white no-radius text-center">
										<div class="panel-body"> 
											<img src="assets/images/appointment (2).png" height="70" weight="100">
										    <h2 class="StepTitle">My History</h2>
										    <p class="cl-effect-1">
									<a href="appointment-history.php">View Appointment History</a></p>
										</div>
									</div>
								</div>


</div>
</div>				
</div>
</div>
		
		<hr>

		</div>
		

		<script src="vendor/jquery/jquery.min.js"></script>
		<script src="vendor/bootstrap/js/bootstrap.min.js"></script>
		<script src="vendor/jquery-cookie/jquery.cookie.js"></script>
		<script src="assets/js/main.js"></script>
		<script src="assets/js/form-elements.js"></script>
<script>
			jQuery(document).ready(function() {
				Main.init();
				FormElements.init();
			});
		</script>
		<?php
	}
	else{
		echo "<script>location.href='index.php'</script>";
	}
	?>
	</body>
</html>
